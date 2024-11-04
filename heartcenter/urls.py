from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # path('', views.home, name='home'),
    # path('diseases/', include('diseases.urls', namespace='diseases')),
    # path('medications/', include('medications.urls', namespace='medications')),
    # path('supplements/', include('supplements.urls', namespace='supplements')),
    # path('doctors/', include('doctors.urls', namespace='doctors')),
]

urlpatterns += i18n_patterns(
    path('', views.home, name='home'),  # Your home view
    path('diseases/', include('diseases.urls', namespace='diseases')),
    path('medications/', include('medications.urls', namespace='medications')),
    path('supplements/', include('supplements.urls', namespace='supplements')),
    path('doctors/', include('doctors.urls', namespace='doctors')),
    path('search/', include('search.urls', namespace='search')),
)