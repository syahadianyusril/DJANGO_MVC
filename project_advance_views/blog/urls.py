from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('form/', views.form, name='form')
]