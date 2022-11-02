from multiprocessing import context
from multiprocessing.util import info
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashboard.models import InformationUser
from signin import admin

# Create your views here.

@login_required(login_url='login/')
def information_user(request):
    username_user = request.user.username
    # check user sudah pernah isi atau tidak:
    information_default = InformationUser.objects.filter(user = request.user).count()
    if request.method == "POST":
        print(request)
        full_name = request.POST.get("full_name")
        blood_group = request.POST.get('blood_group')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        province = request.POST.get('province')
        city = request.POST.get('city')
        gender = request.POST.get('gender')

        information = InformationUser(user = request.user, 
                    full_name = full_name, 
                    blood_group=blood_group, 
                    phone_number = phone_number, 
                    birth_date = birth_date, 
                    province = province, 
                    city = city, 
                    gender = gender)
        information.save()

    context = {'username': username_user}

    if information_default == 0:
        return render(request, 'build_information_user.html', context)
    else:
        # direct dashboard information
        if information_default.is_admin_user() == True:
            return redirect('dashboard:dashboard_admin')
        else:
            return redirect('dashboard:dashboard_relawan')

@login_required(login_url='login/')
def direct_url(request):
    user = InformationUser.objects.filter(user = request.user).count()
    if user == 0:
        redirect
    if admin:
        return redirect('dashboard:dashboard_admin')
    else:
        return redirect()

@login_required(login_url='login/')
def dashboard_relawan(request):
    context = {}
    return render(request, 'dahsboard_relawan.html', context)


@login_required(login_url='login/')
def dashboard_admin(requuest):
    context = {}
    return render(requuest, 'dashboard_admin.html', context)


@login_required(login_url='login/')
def information_admin(request):
    username_user = request.user.username
    # check user sudah pernah isi atau tidak:
    information_default = InformationUser.objects.filter(user = request.user).count()

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        blood_group = request.POST.get('blood_group')
        phone_number = request.POST.get('phone_number')
        birth_date = request.POST.get('birth_date')
        province = request.POST.get('province')
        city = request.POST.get('city')
        gender = request.POST.get('gender')

        information = InformationUser(user = request.user, 
                    full_name = full_name, 
                    blood_group=blood_group, 
                    phone_number = phone_number, 
                    birth_date = birth_date, 
                    province = province, 
                    city = city, 
                    gender = gender,
                    is_validate = True,
                    is_admin_user = True,
                    )
        information.save()

    context = {'username': username_user}
    #direct ke dashboard

    if information_default == 0:
        #kondosi belum isi
        render(request, 'build_information.html', context)
    else:
        # direct dashboard information
        if information_default.is_admin_user() == True:
            return redirect('dashboard:dashboard_admin')
        else:
            return redirect('dashboard:dashboard_relawan')
