import markdown2
from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from django.utils.safestring import mark_safe
from .models import Medication

def medication_list(request):
    current_lang = get_language()
    current_lang = current_lang.split('-')[0]
    medications = Medication.objects.filter(lang=current_lang)
    return render(request, 'medications/medication_list.html', {'medications': medications})

def medication_detail(request, pk):
    current_lang = get_language()
    current_lang = current_lang.split('-')[0]
    medication = get_object_or_404(Medication, pk=pk, lang=current_lang)
    medication.text = mark_safe(markdown2.markdown(medication.text))
    if 'HX-Request' in request.headers:
        template_name = 'medications/partials/medication_detail_partial.html'
    else:
        template_name = 'medications/medication_detail.html'
    
    return render(request, template_name, {'medication': medication})