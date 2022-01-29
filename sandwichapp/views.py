from django.shortcuts import render, get_object_or_404
from sandwichapp import serializers
from sandwichapp.models import Bread, Topping, Cheese, Sauce, Sandwich
from sandwichapp.serializers import BreadSerializer, ToppingSerializer, CheeseSerializer, SauceSerializer, SandwichSerializer
from rest_framework.response import Response
from rest_framework import status, generics, filters
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class BreadViewSet(viewsets.ModelViewSet):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer


class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

class CheeseViewSet(viewsets.ModelViewSet):
    queryset = Cheese.objects.all()
    serializer_class = CheeseSerializer

class SauceViewSet(viewsets.ModelViewSet):
    queryset = Sauce.objects.all()
    serializer_class = SauceSerializer


class SandwichViewSet(viewsets.ModelViewSet):
    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['bread', 'toppings', 'cheese', 'sauces',]
    ordering_fields=['price']

    def create(self, request, format=None):
        enough_ingredients = True
        price = 0

        bread_id = request.data["bread"]
        bread=get_object_or_404(Bread, pk=bread_id)
        if bread.inventory_count <=0 :
            enough_ingredients = False
            message="not enough bread"

        topping_ids = request.data["toppings"]
        toppings = []
        for id in topping_ids:
            topping=get_object_or_404(Topping, pk=id)
            toppings.append(topping)
            if topping.inventory_count <=0 :
                enough_ingredients = False
                message="not enough topping"

        cheese_id = request.data["cheese"]
        cheese=get_object_or_404(Cheese, pk=cheese_id)
        if cheese.inventory_count <=0 :
            enough_ingredients = False
            message = "not enough cheese"

        sauce_ids = request.data["sauces"]
        sauces = []
        for id in sauce_ids:
            sauce=get_object_or_404(Sauce, pk=id)
            sauces.append(sauce)
            if sauce.inventory_count <=0 :
                enough_ingredients = False
                message = "not enough sauce"


        #재료부족
        if not enough_ingredients:
            return Response({"Fail":message}, status=status.HTTP_400_BAD_REQUEST)


        #2개이하
        if len(sauces) > 2:
            return Response({"Fail":"Choose under 3 sauces"}, status=status.HTTP_400_BAD_REQUEST)

        if len(toppings)>2:
            return Response({"Fail":"Choose under 3 toppings"}, status=status.HTTP_400_BAD_REQUEST)


        
        #갯수차감
        #가격계산
        bread.inventory_count -= 1
        price += bread.price
        bread.save()
        
        cheese.inventory_count -= 1
        price += cheese.price
        cheese.save()

        for sauce in sauces:
            sauce.inventory_count -=1
            price += sauce.price
            sauce.save()
        for topping in toppings:
            topping.inventory_count -=1
            price += topping.price
            topping.save()

        serializer = SandwichSerializer(data={"price":price})
        if serializer.is_valid():
            serializer.save(bread=bread, cheese=cheese, toppings=toppings, sauces = sauces)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        sandwich_id = pk
        sandwich = get_object_or_404(Sandwich, pk=sandwich_id)

        bread = sandwich.bread
        cheese = sandwich.cheese
        toppings = sandwich.toppings
        sauces = sandwich.sauces
        price = sandwich.price

        bread.inventory_count += 1
        bread.save()

        cheese.inventory_count += 1
        cheese.save()


        topping_list = []
        for topping in toppings.all():
            topping.inventory_count += 1
            topping_list.append(topping.name)
            topping.save()
        
        sauce_list = []
        for sauce in sauces.all():
            sauce.inventory_count += 1
            sauce_list.append(sauce.name)
            sauce.save()

        sandwich.delete()

        return Response({"bread":bread.name, "cheese":cheese.name, "toppings":topping_list, "sauces":sauce_list, "price":price},status.HTTP_200_OK)