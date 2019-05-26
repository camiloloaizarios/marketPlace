from django.urls import path
from products import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('productDetails/', views.productDetails, name="productDetails"),
    path('checkout/', views.checkout, name="checkout"),
]