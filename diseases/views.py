# diseases/views.py

import markdown2
from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from django.utils.safestring import mark_safe
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
    disease.text = mark_safe(markdown2.markdown(disease.text))

    if 'HX-Request' in request.headers:
        template_name = 'diseases/partials/disease_detail_partial.html'
    else:
        template_name = 'diseases/disease_detail.html'
    
    return render(request, template_name, {'disease': disease})