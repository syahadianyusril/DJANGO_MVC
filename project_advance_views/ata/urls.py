from django.urls import path
from . import views

urlpatterns = [
    path('', views.ata, name='ata')
]