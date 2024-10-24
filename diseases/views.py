from django.shortcuts import render, get_object_or_404
from .models import Disease

def disease_list(request):
    diseases = Disease.objects.all()
    return render(request, 'diseases/disease_list.html', {'diseases': diseases})

def disease_detail(request, pk):
    disease = get_object_or_404(Disease, pk=pk)
    return render(request, 'diseases/disease_detail.html', {'disease': disease})