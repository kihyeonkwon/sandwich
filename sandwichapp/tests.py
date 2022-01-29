from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from .models import Bread, Cheese
from .serializers import BreadSerializer, CheeseSerializer

# Create your tests here.



class BreadViewsTest(APITestCase):
    def test_create_bread(self):       
        url = reverse('bread-list')
        data = {'name':'새빵', 'inventory_count':10, 'price':10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bread.objects.count(), 1)
        self.assertEqual(Bread.objects.get().name, '새빵')

    def test_create_cheese(self):       
        url = reverse('cheese-list')
        data = {'name':'새치즈', 'inventory_count':10, 'price':10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cheese.objects.count(), 1)
        self.assertEqual(Cheese.objects.get().name, '새치즈')






    # def test_can_browse_all_breads(self):
    #     # (2) 
    #     response = self.client.get(reverse("breads:bread-list"))

    #     # (3) 
    #     self.assertEquals(status.HTTP_200_OK, response.status_code)
    #     self.assertEquals(len(self.breads), len(response.data))

    #     for bread in self.breads:
    #         # (4) 
    #         self.assertIn(
    #             BreadSerializer(instance=bread).data,
    #             response.data
    #         )

    # def test_can_read_a_specific_film(self):
    #     # (5) 
    #     response = self.client.get(
    #         reverse("films:film-detail", args=[self.film.id])
    #     )

    #     self.assertEquals(status.HTTP_200_OK, response.status_code)
    #     self.assertEquals(
    #         FilmSerializer(instance=film).data,
    #         response.data
    #     )