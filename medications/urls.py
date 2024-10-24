from django.urls import path
from . import views

app_name = 'medications'

urlpatterns = [
    path('', views.medication_list, name='medication_list'),
    path('<int:pk>/', views.medication_detail, name='medication_detail'),
]