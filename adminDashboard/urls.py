from django.urls import path
from adminDashboard.views import showDash, addScreening

app_name = 'adminDashboard'

urlpatterns = [
    path('adminDashPage/', showDash, name='showDash'),
    path('formScreening/', addScreening, name='addScreening'),
]