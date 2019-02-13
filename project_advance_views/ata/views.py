from django.shortcuts import render

# Create your views here.

def ata(request):
    return render(request, 'ata/home.html')