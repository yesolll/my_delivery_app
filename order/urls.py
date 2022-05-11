from django.urls import path
from order import views

urlpatterns = [
    path('shops/', views.shops, name="shops"),
    path('menus/<int:shop_id>', views.menus, name="menus"),
    path('order/', views.order, name="order"),
]
