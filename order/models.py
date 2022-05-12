from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=50)
    shop_address = models.CharField(max_length=100)

class Menu(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=30)

class Order(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    estimated_time = models.IntegerField(default = -1)
    delivery_address = models.CharField(max_length=100)
    delivery_finish = models.BooleanField(default = 0)

class OrderMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_menu_name = models.CharField(max_length=30)