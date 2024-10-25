from django.shortcuts import render, get_object_or_404
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
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})