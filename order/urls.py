from django.urls import path
from order import views

urlpatterns = [
    path('shops/', views.shops),
    path('menus/', views.menus),
]
