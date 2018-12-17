from django.db import models

class Teachers(models.Model):
	Name = models.CharField(max_length=100)
	created_on = models.DateTimeField(auto_now_add=True)
	via = models.URLField(blank=True)
	
	def total_likes(self):
		return self.like_set.count()
		
	def str_(self):
		return self.text[:50]
		
class Like(models.Model):
	teachers = models.ForeignKey('Teachers',on_delete=models.PROTECT)