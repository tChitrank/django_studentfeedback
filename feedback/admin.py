from django.contrib import admin
from .models import ratings
from .models import student

admin.site.register(ratings)
admin.site.register(student)