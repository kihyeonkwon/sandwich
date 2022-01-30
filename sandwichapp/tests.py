from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from .models import Bread, Cheese, Sauce, Topping, Sandwich
from .serializers import BreadSerializer, CheeseSerializer, CheeseSerializer, SauceSerializer, SandwichSerializer

# Create your tests here.



class SandwichTest(APITestCase):
    def setUp(self):
        Bread.objects.create(name="식빵", inventory_count=2, price=500)
        Sauce.objects.create(name="올리브", inventory_count=3, price=300)
        Sauce.objects.create(name="불닭", inventory_count=3, price=400)
        Topping.objects.create(name="토마토", inventory_count=3, price=1000)
        Topping.objects.create(name="베이컨", inventory_count=3, price=800)
        Topping.objects.create(name="햄", inventory_count=3, price=700)
        Cheese.objects.create(name="모짜렐라", inventory_count=3, price=800)
        Cheese.objects.create(name="체다", inventory_count=3, price=900)

    #샌드위치 만들기
    def test_create_sandwich(self):
        url = '/sandwichapp/sandwich/'
        data = {"bread":1,"toppings":[1],"cheese":1,"sauces":[1]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sandwich.objects.count(), 1)


    #토핑과 소스 두가지로 샌드위치 만들기
    def test_create_sandwich_two_toppings(self):
        url = '/sandwichapp/sandwich/'
        data = {"bread":1,"toppings":[1,2],"cheese":1,"sauces":[1,2]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sandwich.objects.get(pk=1).toppings.count(), 2)

    #세가지 토핑으로 샌드위치 만들기 시도
    def test_create_sandwich_three_toppings(self):
        url = '/sandwichapp/sandwich/'
        data = {"bread":1,"toppings":[1,2,3],"cheese":1,"sauces":[1,2]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Sandwich.objects.count(), 0)

    #없는 식빵
    def test_create_sandwich_no_bread(self):
        url = '/sandwichapp/bread/1/'
        response = self.client.delete(url)

        url = '/sandwichapp/sandwich/'
        data = {"bread":1,"toppings":[1,2],"cheese":1,"sauces":[1,2]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Sandwich.objects.count(), 0)


    #식빵 재고 소진
    def test_create_sandwich_zero_bread(self):
        url = '/sandwichapp/sandwich/'
        data = {"bread":1,"toppings":[1,2],"cheese":1,"sauces":[1,2]}
        response = self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Sandwich.objects.count(), 2)

    #식빵 제거 시 샌드위치 유지
    def test_create_sandwich_no_bread(self):
        url = '/sandwichapp/sandwich/'
        data = {"bread":1,"toppings":[1,2],"cheese":1,"sauces":[1,2]}
        response = self.client.post(url, data, format='json')
        url = '/sandwichapp/bread/1/'
        response = self.client.delete(url)
        self.assertEqual(Bread.objects.count(), 0)
        self.assertEqual(Sandwich.objects.get(pk=1).bread.name, "식빵")
        

    #식빵 이름변경시 샌드위치 식빵 변경
    def test_create_sandwich_no_bread(self):
        url = '/sandwichapp/sandwich/'
        data = {"bread":1,"toppings":[1,2],"cheese":1,"sauces":[1,2]}
        response = self.client.post(url, data, format='json')

        url = '/sandwichapp/bread/1/'
        data = {"name":"호밀빵", "inventory_count":2, "price":500}
        response = self.client.put(url, data,format='json')
        self.assertEqual(Bread.objects.get(pk=1).name, "호밀빵")
        self.assertEqual(Sandwich.objects.get(pk=1).bread.name, "호밀빵")



    #가격총합 확인
    def test_sandwich_price(self):
        url = '/sandwichapp/sandwich/'
        data = {"bread":1,"toppings":[1,2],"cheese":1,"sauces":[1,2]}
        response = self.client.post(url, data, format='json')

        sandwich_price = Sandwich.objects.get(pk=1).price
        ingredients_price = Bread.objects.get(pk=1).price + Topping.objects.get(pk=1).price + Topping.objects.get(pk=2).price + Cheese.objects.get(pk=1).price + Sauce.objects.get(pk=1).price + Sauce.objects.get(pk=2).price

        self.assertEqual(sandwich_price, ingredients_price)