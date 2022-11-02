
from django.urls import path

from users.views import signup_relawan, login_relawan

app_name = 'users'


urlpatterns  = [
        path('', signup_relawan, name='signup_relawan'),
        path('login', login_relawan, name='login_relawan'),

]

