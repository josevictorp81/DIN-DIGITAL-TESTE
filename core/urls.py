from django.urls import path

from . import views

urlpatterns = [
    path('product/create/', views.ProductCreateAPIView.as_view(), name='create-product'),
    path('product/list/', views.ProductListAPIView.as_view(), name='list-product'),
    path('product/list/<int:pk>/', views.ProductRetrieveAPIView.as_view(), name='list-product-id'),
    path('product/update/<int:pk>/', views.ProductUpdateAPIView.as_view(), name='update-product'),
]