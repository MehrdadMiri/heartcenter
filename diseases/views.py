from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from .models import Disease

def disease_list(request):
    current_lang = get_language()
    current_lang = current_lang.split('-')[0]    
    diseases = Disease.objects.filter(lang=current_lang)
    return render(request, 'diseases/disease_list.html', {'diseases': diseases})

def disease_detail(request, pk):
    current_lang = get_language()
    current_lang = current_lang.split('-')[0]
    disease = get_object_or_404(Disease, pk=pk, lang=current_lang)
    return render(request, 'diseases/disease_detail.html', {'disease': disease})