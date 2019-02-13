from django.contrib import admin
from .models import Blog

my_model = [Blog]
admin.site.register(my_model)

# Register your models here.
