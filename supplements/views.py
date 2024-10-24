from django.shortcuts import render, get_object_or_404
from .models import Supplement

def supplement_list(request):
    supplements = Supplement.objects.all()
    return render(request, 'supplements/supplement_list.html', {'supplements': supplements})

def supplement_detail(request, pk):
    supplement = get_object_or_404(Supplement, pk=pk)
    return render(request, 'supplements/supplement_detail.html', {'supplement': supplement})