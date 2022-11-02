from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from dashboard.models import InformationUser
from dashboard.views import dashboard_relawan
from django.contrib import auth

def login_user(request):
    users = request.user
    if request.user.is_authenticated:
        return redirect("dashboard:information_user")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            information = InformationUser.objects.filter(user=user).count()
            if information == 0:
                return redirect('dashboard:information_user')
            else:
                return redirect('dashboard:information_user')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'signin_.html', context)

def logout(request):
    auth.logout(request)
    return redirect('signin:login_user')