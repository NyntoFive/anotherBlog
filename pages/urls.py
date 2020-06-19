from django.urls import path, include
from .views import demoPage, shopPage, landing
urlpatterns = [
    path('demo/',demoPage, name='demo'),
    path('shop/', shopPage, name="shop"),
    path('', landing, name='landing'),
]