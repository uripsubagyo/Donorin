from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.http.response import JsonResponse
from adminDashboard.models import hasilScreening
from adminDashboard.forms import ScreeningForm
from dashboard.models import InformationUser

# Create your views here.

def showDash(request):
    users = InformationUser.objects.filter(user =request.user, is_admin_user = True).count()

    if users != 0:
        return render(request, "adminDashPage.html")
    else:
        return redirect('dashboard:dashboard_relawan')

def addScreening(request):
    form = ScreeningForm()
    if request.method == "POST":
        form = ScreeningForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            dataAdmin = hasilScreening()
            dataAdmin.namaDonor = form.cleaned_data['namaDonor']
            dataAdmin.tekananDarah = form.cleaned_data['tekananDarah']
            dataAdmin.suhuTubuh = form.cleaned_data['suhuTubuh']
            dataAdmin.kadarHemo = form.cleaned_data['kadarHemo']
            dataAdmin.beratBadan = form.cleaned_data['beratBadan']
            dataAdmin.save()

            return HttpResponseRedirect(reverse('adminDashboard:showDash'))
        
    return render(request, 'formScreening.html', {'form': form})
