from django.contrib import admin
from .models import BlogPost, Mentee

my_model = [BlogPost, Mentee]
admin.site.register(my_model)

# Register your models here.
