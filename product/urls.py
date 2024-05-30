from django.urls import path
from . import views
urlpatterns = [
    path('product', views.ProductAPI.as_view()),
    path('product/<int:id>', views.ProductAPI.as_view()),
]
