from django.urls import path

from landing.views import showLanding, addNews, deleteNews

app_name = 'landing'

urlpatterns = [
    path('', showLanding, name='showLanding'),
    path('addNews/', addNews, name='addNews'),
    path('delete/<int:id>', deleteNews, name='deleteNews'),
]