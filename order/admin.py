from django.contrib import admin

from .models import Shop, Menu, Order, OrderMenu

admin.site.register(Shop)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderMenu)