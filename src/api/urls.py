from django.urls import path, include

urlpatterns = [
    path('category/', include('api.category.urls'), name='category'),
    path('blog/', include('api.blog.urls'), name='blog'),
    path('region/', include('api.region.urls'), name='region'),
    # path('user/', region, name='region'),
]
