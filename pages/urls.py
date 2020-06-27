from django.urls import path, include
from .views import demoPage, shopPage, landing, homePage
urlpatterns = [
    path('demo/',demoPage, name='demo'),
    path('shop/', shopPage, name="shop"),
    path('home/',homePage,name="home"),
    path('', landing, name='landing'),
]