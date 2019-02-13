from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('form/', views.form, name='form'),
    path('blog/<int:post_id>/', views.post_detail, name="post_detail")
]