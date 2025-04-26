from django.urls import path
from .views import get_list_ctg, detail_ctg, HelloView, CategoryDetailView

# serializers
urlpatterns = [
    path('', get_list_ctg, name='category-list'),
    path('<int:pk>/', detail_ctg, name='category-detail'),
    path('test/', HelloView.as_view()),
    path('test/<int:pk>/', CategoryDetailView.as_view()),
]