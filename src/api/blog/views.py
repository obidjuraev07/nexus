import django_filters.rest_framework
from rest_framework.filters import SearchFilter
from django.contrib.admindocs.views import BookmarkletsView
from django.core.serializers import serialize
from django.views.static import serve
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import Blog
from .serializers import BlogSerializers

# class BlogGenericAPIView(GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializers
#
#     def get(self, request):
#         books = self.get_queryset()
#         serializer = self.get_serializer(books, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"data": 'invalid'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def list(self):
#         pass

# class BlogGenericAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializers
#     # filter_backends = ['created_at']
#
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class BlogDetailGenericAPIView(GenericAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializers
#
#     # def get(self, request, *args, **kwargs):
#     #     return self.retrieve(self, request,*args, **kwargs)
#
#     def get(self, request):
#         book = self.get_object()
#         serializer = self.get_serializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)


class BlogGenericAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    filter_backends = [SearchFilter]
    lookup_field = ['title', 'description']



class BlogDetailGenericAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers
    lookup_field = ['slug']