from django.shortcuts import render, get_object_or_404
from .models import Medication

def medication_list(request):
    medications = Medication.objects.all()
    return render(request, 'medications/medication_list.html', {'medications': medications})

def medication_detail(request, pk):
    medication = get_object_or_404(Medication, pk=pk)
    return render(request, 'medications/medication_detail.html', {'medication': medication})