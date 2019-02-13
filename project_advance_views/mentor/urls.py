from django.urls import path
from . import views

urlpatterns = [
    path('mentor', views.mentor, name='mentor')
]