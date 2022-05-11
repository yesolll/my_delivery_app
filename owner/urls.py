from django.urls import path
from owner import views

urlpatterns = [
    # path('orders/<int:shop_id>', views.orders, name="orders"),
    path('timeinput/<int:shop_id>', views.timeinput, name="timeinput"),
]
