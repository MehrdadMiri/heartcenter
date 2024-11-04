from django.urls import path
from . import views

app_name = 'medications'

urlpatterns = [
    path('', views.search, name='search'),
]