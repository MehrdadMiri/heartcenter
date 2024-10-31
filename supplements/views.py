import markdown2
from django.shortcuts import render, get_object_or_404
from django.utils.translation import get_language
from django.utils.safestring import mark_safe
from .models import Supplement

def supplement_list(request):
    current_lang = get_language()
    current_lang = current_lang.split('-')[0]
    print(current_lang, '####')
    supplements = Supplement.objects.filter(lang=current_lang)
    return render(request, 'supplements/supplement_list.html', {'supplements': supplements})

def supplement_detail(request, pk):
    current_lang = get_language()
    current_lang = current_lang.split('-')[0]
    supplement = get_object_or_404(Supplement, pk=pk, lang=current_lang)
    supplement.text = mark_safe(markdown2.markdown(supplement.text))
    if 'HX-Request' in request.headers:
        template_name = 'supplements/partials/supplement_detail_partial.html'
    else:
        template_name = 'supplements/supplement_detail.html'
    
    return render(request, template_name, {'supplement': supplement})