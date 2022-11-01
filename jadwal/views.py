from django.shortcuts import render, redirect
from jadwal.models import Jadwal
from jadwal.forms import JadwalForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.

# @login_required(login_url='/login/')
def show_jadwal(request):
    jadwal = Jadwal.objects.all() # harusnya ganti filter
    context = {
        'list_jadwal': jadwal
    }

    return render(request, 'jadwal.html', context)
    #return redirect('/login')

# @login_required(login_url='/login/')
def delete(request, id):
    if Jadwal.objects.get(id=id).accepted == 'Menunggu konfirmasi':
        Jadwal.objects.get(id=id).delete()
        return JsonResponse({'instance': 'Permintaan mendonor dibatalkan'}, status=200)
    elif Jadwal.objects.get(id=id).accepted == 'Dikonfirmasi - menunggu kedatangan':
        return JsonResponse({'instance': 'Anda tidak dapat menghapus jadwal yang sudah dikonfirmasi, silakan hubungi UTD terkait'}, status=200)
    return redirect('jadwal:show_jadwal')

# @login_required(login_url='/login/')
def book_jadwal(request):
    if request.method == 'POST':
        form = JadwalForm(request.POST)
        if form.is_valid():
            tanggal = form.cleaned_data['tanggal']
            lokasi = form.cleaned_data['lokasi']

            Jadwal.objects.create(user=request.user, date=tanggal, loc=lokasi, accepted='Menunggu konfirmasi')

            return HttpResponseRedirect(reverse('jadwal:show_jadwal'))
    else:
        form = JadwalForm()
    context = {'form':form}
    return render(request, 'book.html', context)