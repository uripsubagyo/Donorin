from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.http.response import JsonResponse

from landing.models import News
from landing.forms import NewsForm


#@login_required(login_url='/login/')
def showLanding(request):
    dataNews = News.objects.all() #.filter(user=request.user)
    context = {
        'listDataNews' : dataNews,
    }
    return render(request, "mainPage.html", context)

#@login_required(login_url='/login/')
def addNews(request):
    form = NewsForm()
    if request.method == "POST":
        form = NewsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            dataNews = News()
            dataNews.title = form.cleaned_data['title']
            dataNews.description = form.cleaned_data['description']
            dataNews.save()
            
            return HttpResponseRedirect(reverse('landing:showLanding'))

    return render(request, 'formPage.html', {'form': form})