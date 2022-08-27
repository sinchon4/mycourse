
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import auth
from django.contrib.auth import login, authenticate
import json
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']: 
            username=request.POST.get('username')
            if User.objects.filter(username=username).exists(): 
                return render(request, 'alert.html')
            password=request.POST.get('password')
            last_name=request.POST.get('last_name')
            user = User.objects.create_user(username=username, password=password, last_name=last_name) #email=email
            auth.login(request, user)
            return redirect('/')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        jsonObject = json.loads(request.body)
        username = jsonObject.get("username")
        password = jsonObject.get("password")
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            msg= ""
        else:
            msg = "❗아이디와 비밀번호를 다시 확인해주세요"
        data = {'msg': msg}
        return JsonResponse(data)
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'login.html')
