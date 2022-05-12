from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, OrderMenu
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def orders(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        return render(request, 'delivery/orders.html', {'orders': orders})
    elif request.method == 'POST':
        order = Order.objects.get(pk=int(request.POST['order_id']))
        order.delivery_finish = 1
        order.save()
        return render(request,'delivery/delivery_finish_success.html')
