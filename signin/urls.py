
from django.urls import path
from .views import login_user, logout

app_name = 'signin'


urlpatterns  = [
        path('', login_user, name='login_user'),
        path('logout', logout, name='logout')
]