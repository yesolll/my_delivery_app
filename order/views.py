from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, OrderMenu
from user.models import User
from order.serializers import ShopSerializer, MenuSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def shops(request):
    if request.method == 'GET' :
        # shops = Shop.objects.all()
        # serializer = ShopSerializer(shops, many=True)
        # return JsonResponse(serializer.data, safe=False)
        # if User.objects.all().get(id=request.session['user_sq']).user_type==0:
            shops = Shop.objects.all()
            return render(request, 'order/shops.html', {'shops': shops})
        # else:
        #     return render(request, 'order/fail.html')

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def menus(request, shop_id):
    if request.method == 'GET' :
        shop = Shop.objects.get(pk=shop_id)
        menus = Menu.objects.filter(shop=shop_id)
        return render(request, 'order/menus.html', {'menus': menus, 'shop': shop})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MenuSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

from django.utils import timezone
@csrf_exempt
def order(request):
    if request.method == 'POST':
        shop_id = request.POST['shop_id']
        delivery_address = request.POST['address']
        delivery_msg = request.POST['msg']
        order_date = timezone.now()
        order_menu_names = request.POST.getlist('menu')

        shop = Shop.objects.get(pk=int(shop_id))

        shop.order_set.create(shop=int(shop_id), order_date=order_date, delivery_address=delivery_address, delivery_msg=delivery_msg)

        order = Order.objects.get(pk=shop.order_set.latest('id').id)
        
        for order_menu_name in order_menu_names:
            order.ordermenu_set.create(order_menu_name=order_menu_name)

        return render(request, 'order/order_result_success.html')
        
    elif request.method == 'GET':
        orders = Order.objects.all()
        return render(request, 'order/orders.html', {'orders': orders})