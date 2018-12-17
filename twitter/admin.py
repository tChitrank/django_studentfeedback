from django.contrib import admin
from twitter.models import Twitter

class TwitterAdmin(admin.ModelAdmin):
	list_display = ('text','created_on','total_likes')
	list_filter = ['created_on']
	search_fields = ['text']
	
admin.site.register(Twitter, TwitterAdmin)

