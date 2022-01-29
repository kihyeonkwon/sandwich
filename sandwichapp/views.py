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