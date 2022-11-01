from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
import json
from .forms import RegistrationFormRelawan, LoginForm


# Create your views here.
def is_ajax(request):
	return request.META.get('HTTP_X_REQUESTED_WITH') == 'JSONHttpRequest'


def signup_relawan(request):
	user = request.user
	# if user.is_authenticated: 
	# 	return HttpResponse("<h3>Anda sudah masuk ke akun dengan email " + str(user.email) + "</h3>")
	context = {}
	if request.POST:
		form = RegistrationFormRelawan(request.POST)
		data = {}
		print(request.POST)
		if form.is_valid():
			form.save()
			data['success'] = True
			return HttpResponse(json.dumps(data), content_type='application/json')
		else:
			data['error'] = form.errors
			data['success'] = False
			context['registration_form'] = form
			return HttpResponse(json.dumps(data), content_type='application/json')

	else:
		form = RegistrationFormRelawan()
		context['registration_form'] = form
	return render(request, 'signup_relawan.html', context)


def login_relawan(request):
	context = {}


	if request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)
			if user:
				login(request, user)
				return redirect('')
				
	else:
		form = LoginForm()
	context['login_form'] = form

	return render(request, "signin_relawan.html", context)
