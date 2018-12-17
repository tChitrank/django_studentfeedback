from django.db import models

class Twitter(models.Model):
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	via = models.URLField(blank=True)
	
	def total_likes(self):
		return self.like_set.count()
		
	def str_(self):
		return self.text[:50]
		
class Like(models.Model):
	twitter = models.ForeignKey('Twitter',on_delete=models.PROTECT)
