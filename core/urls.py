from django.urls import path

from . import views

urlpatterns = [
    path('product/create/', views.ProductCreateAPIView.as_view(), name='create-product'),
    path('product/list/', views.ProductListAPIView.as_view(), name='list-product'),
]