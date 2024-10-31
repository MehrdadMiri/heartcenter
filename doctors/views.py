import markdown2
from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
from .models import Doctor

def doctor_list(request):
    current_lang = get_language()
    current_lang = current_lang.split('-')[0]
    doctors = Doctor.objects.filter(lang=current_lang)
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    current_lang = get_language()
    current_lang = current_lang.split('-')[0]
    doctor = get_object_or_404(Doctor, pk=pk, lang=current_lang)
    doctor.text = mark_safe(markdown2.markdown(doctor.text))
    if 'HX-Request' in request.headers:
        template_name = 'doctors/partials/doctor_detail_partial.html'
    else:
        template_name = 'doctors/doctor_detail.html'
    
    return render(request, template_name, {'doctor': doctor})
