from django.shortcuts import render
from django.db.models import Q
from diseases.models import Disease
from medications.models import Medication
from supplements.models import Supplement
from doctors.models import Doctor

def search(request):
    query = request.GET.get('q')
    diseases = Disease.objects.filter(name__icontains=query) if query else []
    medications = Medication.objects.filter(name__icontains=query) if query else []
    supplements = Supplement.objects.filter(name__icontains=query) if query else []
    doctors = Doctor.objects.filter(name__icontains=query) if query else []

    context = {
        'query': query,
        'diseases': diseases,
        'medications': medications,
        'supplements': supplements,
        'doctors': doctors,
    }
    return render(request, 'search/search_results.html', context)