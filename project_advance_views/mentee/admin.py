from django.contrib import admin
from .models import Mentee

my_model = [Mentee]
admin.site.register(my_model)

# Register your models here.
