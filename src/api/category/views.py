
from django.shortcuts import get_object_or_404
from category.models import Category
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CategorySerializer


@api_view(['GET', 'POST'])
def get_list_ctg(request):
    if request.method == "GET":
        categories = Category.objects.all()
        result = CategorySerializer(categories, many=True)
        print(result.data)
        return Response({"data": result.data})

    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        print(serializer, serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def detail_ctg(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response({'error': 'Could not found'})

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        print(serializer.is_valid(), serializer)
        if serializer.is_valid():
            serializer.save()
            print(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Could not edit"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HelloView(APIView):
    def get(self, request):
        return Response({"data": "Salom 408"}, status=status.HTTP_200_OK)
    def post(self, request):
        pass


class CategoryDetailView(APIView):
    def get_object(self, pk):
        # try:
        #     category = Category.objects.get(pk=pk)
        # except Category.DoesNotExist:
        #     return Response({"data": 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        # return category
        category = get_object_or_404(Category, pk=pk)
        print('CATEGORY', category)
        return category

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"data": "invalid"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)