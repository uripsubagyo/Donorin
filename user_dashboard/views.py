from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from dashboard.models import InformationUser

@login_required(login_url='/login/')
def index(request):
    user = request.user
    userdata = InformationUser.objects.filter(user = user, is_admin_user = False)
    if userdata==1:
        userdata = InformationUser.objects.get(user=user)
        return render(request, 'index_user_dashboard.html',{'username': user.username, 'totaldonasi': userdata.totaldonasi, 'screening': userdata.screening})
    return redirect('login/')

def get_userData(request):
    user = request.user
    userdata = InformationUser.objects.filter(user = user, is_admin_user = False)
    if userdata==1:
        userdata = InformationUser.objects.filter(user=user)
        return HttpResponse(serializers.serialize("json", userdata), content_type="application/json")
    return redirect('login/')
