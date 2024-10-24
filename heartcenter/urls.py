from django.contrib import admin
from django.urls import path, include
from . import views  # Import the views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Add this line for the main page
    path('diseases/', include('diseases.urls', namespace='diseases')),
    path('medications/', include('medications.urls', namespace='medications')),
    path('supplements/', include('supplements.urls', namespace='supplements')),
    path('doctors/', include('doctors.urls', namespace='doctors')),
]