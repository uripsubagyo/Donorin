
from django.urls import path

from .views import register_user_admin, register_user_view

app_name = 'signup'


urlpatterns  = [
        path('', register_user_view, name='register_user_view'),
        # path('admin/KmA0zNHu6GmFao1pkIt3cLspQzf7rm9b', register_user_admin, name='register_user_admin'),

]