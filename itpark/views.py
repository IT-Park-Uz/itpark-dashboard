from django.shortcuts import render
from .models import ItPark

def index(request):
    itpark = ItPark.objects.all()

    context = {
    'itpark': itpark,
    'title': 'Dashboard',
    }
    return render(request,'itpark/index.html',context)