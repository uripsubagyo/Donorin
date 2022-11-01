from django.urls import path
from jadwal.views import *

app_name = 'jadwal'

urlpatterns = [
    path('', show_jadwal, name='show_jadwal'),
    path('delete/', delete, name='delete'),
    path('book/', book_jadwal, name='book_jadwal'),
]