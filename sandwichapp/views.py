from django.shortcuts import render
from sandwichapp import serializers
from sandwichapp.models import Bread, Topping, Cheese, Sauce, Sandwich
from sandwichapp.serializers import BreadSerializer, ToppingSerializer, CheeseSerializer, SauceSerializer, SandwichSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics




class BreadView(APIView):
    def get(self, request, format=None):
        breads = Bread.objects.all()
        serializer = BreadSerializer(breads, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BreadSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        bread = generics.get_object_or_404(Bread, pk = request.data['id'])
        serializer = BreadSerializer(bread, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        bread = generics.get_object_or_404(Bread, pk = request.data['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ToppingView(APIView):
    def get(self, request, format=None):
        toppings = Topping.objects.all()
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToppingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        topping = generics.get_object_or_404(Topping, pk = request.data['id'])
        serializer = ToppingSerializer(topping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        topping = generics.get_object_or_404(Topping, pk = request.data['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheeseView(APIView):
    def get(self, request, format=None):
        cheeses = Cheese.objects.all()
        serializer = CheeseSerializer(cheeses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CheeseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        cheese = generics.get_object_or_404(Cheese, pk = request.data['id'])
        serializer = CheeseSerializer(cheese, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        cheese = generics.get_object_or_404(Cheese, pk = request.data['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SauceView(APIView):
    def get(self, request, format=None):
        sauces = Sauce.objects.all()
        serializer = SauceSerializer(sauces, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SauceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None):
        sauce = generics.get_object_or_404(Sauce, pk = request.data['id'])
        serializer = SauceSerializer(sauce, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        sauce = generics.get_object_or_404(Sauce, pk = request.data['id']).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SandwichView(APIView):
    def get(self, request, format=None):
        sandwiches = Sandwich.objects.all()
        serializer = SandwichSerializer(sandwiches, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        enough_ingredients = True

        bread_id = request.data["bread"]
        bread=Bread.objects.get(pk=bread_id)
        if bread.inventory_count <=0 :
            enough_ingredients = False

        topping_ids = request.data["toppings"]
        toppings = []
        for id in topping_ids:
            topping = Topping.objects.get(pk=id)
            toppings.append(topping)
            if topping.inventory_count <=0 :
                enough_ingredients = False

        cheese_id = request.data["cheese"]
        cheese=Cheese.objects.get(pk=cheese_id)
        if cheese.inventory_count <=0 :
            enough_ingredients = False

        sauce_ids = request.data["sauces"]
        sauces = []
        for id in sauce_ids:
            sauce = Sauce.objects.get(pk=id)
            sauces.append(sauce)
            if sauce.inventory_count <=0 :
                enough_ingredients = False


        #재료부족
        if not enough_ingredients:
            return Response({"Fail":"Not enough ingredients"}, status=status.HTTP_400_BAD_REQUEST)


        #2개이하
        if len(sauces) > 2:
            return Response({"Fail":"Choose under 3 sauces"}, status=status.HTTP_400_BAD_REQUEST)

        if len(toppings)>2:
            return Response({"Fail":"Choose under 3 toppings"}, status=status.HTTP_400_BAD_REQUEST)


        
        #갯수차감
        bread.inventory_count -= 1
        bread.save()
        
        cheese.inventory_count -= 1
        cheese.save()

        for sauce in sauces:
            sauce.inventory_count -=1
            sauce.save()
        for topping in toppings:
            topping.inventory_count -=1
            topping.save()

        serializer = SandwichSerializer(data={})
        if serializer.is_valid():
            serializer.save(bread=bread, cheese=cheese, toppings=toppings, sauces = sauces)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
