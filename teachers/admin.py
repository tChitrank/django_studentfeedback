from django.contrib import admin
from teachers.models import Teachers

class TeachersAdmin(admin.ModelAdmin):
	list_display = ('Name','created_on','total_likes')
	list_filter = ['created_on']
	search_fields = ['text']
	
admin.site.register(Teachers, TeachersAdmin)