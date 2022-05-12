from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, OrderMenu
from user.models import User
from user.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, 'user/users.html', {'users': users})
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JSONParser(serializer.errors, status = 400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            request.session['user_sq'] = User.objects.all().get(user_name=name).id
            return render(request, 'user/success.html')
        except:
            return render(request, 'user/fail.html')
        
    elif request.method == 'GET':
        return render(request, 'user/login.html')