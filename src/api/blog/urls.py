from django.urls import path
from .views import BlogGenericAPIView, BlogDetailGenericAPIView

# serializers
urlpatterns = [
    path('', BlogGenericAPIView.as_view()),
    path('<slug:slug>/', BlogDetailGenericAPIView.as_view()),
]