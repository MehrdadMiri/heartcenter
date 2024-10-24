from django.urls import path
from . import views

app_name = 'supplements'

urlpatterns = [
    path('', views.supplement_list, name='supplement_list'),
    path('<int:pk>/', views.supplement_detail, name='supplement_detail'),
]