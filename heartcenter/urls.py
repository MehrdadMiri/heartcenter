from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diseases/', include('diseases.urls', namespace='diseases')),
    path('medications/', include('medications.urls', namespace='medications')),
    path('supplements/', include('supplements.urls', namespace='supplements')),
    path('doctors/', include('doctors.urls', namespace='doctors')),
]