from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, OrderMenu
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def timeinput(request, shop_id):
    if request.method == 'GET':
        orders = Order.objects.filter(shop=shop_id)
        return render(request, 'owner/orders.html', {'orders': orders, 'shop_id': shop_id})
        
    elif request.method == 'POST':
        order = Order.objects.get(pk=int(request.POST['order_id']))
        order.estimated_time = int(request.POST['estimated_time'])
        order.save()
        return render(request, 'owner/time_input_success.html', {'order': order, 'shop_id': shop_id})
        