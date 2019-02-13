from django.shortcuts import render, redirect
from .models import Mentee

# Create your views here.

def mentee(request):
    mentee = Mentee.objects.all()
    return render(request, 'mentee/mentee.html',{'mentees':mentee})