from django.shortcuts import render
from sandwichapp import serializers
from sandwichapp.models import Bread, Topping, Cheese, Sauce, Sandwich
from sandwichapp.serializers import BreadSerializer, ToppingSerializer, CheeseSerializer, SauceSerializer, SandwichSerializer
from rest_framework.views import APIView
from rest_framework.response import Response




class Bread(APIView):
    def get(self, request, format=None):
        breads = Bread.objects.all()
        serializer = BreadSerializer(breads, many=True)
        return Response(serializer.data)