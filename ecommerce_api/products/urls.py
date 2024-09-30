from django.urls import path
from .views import (
    CreateProductView,
    ReadProductView,
    UpdateProductView,
    DeleteProductView,
    CreateUserView,
    ReadUserView,
    UpdateUserView,
    DeleteUserView,
    SearchProductView,
    ListProductView,
    RetrieveProductView,
    ObtainTokenPairView,
    VerifyTokenView,
    RefreshTokenView
)

urlpatterns = [
    path('products/', CreateProductView.as_view()),
    path('products/<pk>/', ReadProductView.as_view()),
    path('products/<pk>/update/', UpdateProductView.as_view()),
    path('products/<pk>/delete/', DeleteProductView.as_view()),
    path('users/', CreateUserView.as_view()),
    path('users/<pk>/', ReadUserView.as_view()),
    path('users/<pk>/update/', UpdateUserView.as_view()),
    path('users/<pk>/delete/', DeleteUserView.as_view()),
    path('search/', SearchProductView.as_view()),
    path('products/', ListProductView.as_view()),
    path('products/<pk>/', RetrieveProductView.as_view()),
    path('token/', ObtainTokenPairView.as_view()),
    path('token/verify/', VerifyTokenView.as_view()),
    path('token/refresh/', RefreshTokenView.as_view())
]