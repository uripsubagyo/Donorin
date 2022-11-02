
from django.urls import path

from .views import information_user, dashboard_admin, dashboard_relawan, information_admin, direct_url

app_name = 'dashboard'


urlpatterns  = [
        path('', direct_url, name='direct_url'),
        path('information/', information_user, name='information_user'),
        path('admin/', dashboard_admin, name = 'dashboard_admin'),
        path('relawan/', dashboard_relawan, name = 'dashboard_relawan'),
        path('information_admin/"]!lRx=xzp~s', information_admin, name = 'information_admin')]
