from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

class student(models.Model):
	roll_no=models.IntegerField( primary_key=True, default="00")
	branch =models.CharField(choices=(
			('CS', 'Computer Science'),
			('IT', 'Information Technology'),
			('EC', 'Electrical and Communication'),
			('EE', 'Electrical Engineering'),
			('ME', 'Mechanical Engineering'),
			('CE', 'Civil Engineering'),
		),
		max_length=80
	)

	section=models.CharField(max_length=10)

	def __str__(self):
		return self.branch

class ratings(models.Model):
	roll_no=models.IntegerField( primary_key=True, default="00")
	branch =models.CharField(choices=(
			('CS', 'Computer Science'),
			('IT', 'Information Technology'),
			('EC', 'Electrical and Communication'),
			('EE', 'Electrical Engineering'),
			('ME', 'Mechanical Engineering'),
			('CE', 'Civil Engineering'),
		),
		max_length=80, default='Branch'
	)

	section=models.CharField(max_length=10,default='Section')

	subject_name1=models.CharField(max_length=50, null=True)
	teacher_name1=models.CharField(max_length=50, null=True)
	Punctuality1 = models.IntegerField(blank=False , default=5)
	Subject_knowledge1 = models.IntegerField(blank=False, default=5)
	Behaviour1 = models.IntegerField(blank=False, default=5)
	Method_of_teaching1 = models.IntegerField(blank=False, default=5)
	Audibility1 = models.IntegerField(blank=False, default=5)
	Syllabus_coverage1 = models.IntegerField(blank=False, default=5)
	

	subject_name2=models.CharField(max_length=50, null=True)
	teacher_name2=models.CharField(max_length=50, null=True)
	Punctuality2 = models.IntegerField(blank=False , default=5)
	Subject_knowledge2 = models.IntegerField(blank=False, default=5)
	Behaviour2 = models.IntegerField(blank=False, default=5)
	Method_of_teaching2 = models.IntegerField(blank=False, default=5)
	Audibility2 = models.IntegerField(blank=False, default=5)
	Syllabus_coverage2 = models.IntegerField(blank=False, default=5)

	subject_name3=models.CharField(max_length=50, null=True)
	teacher_name3=models.CharField(max_length=50, null=True)
	Punctuality3 = models.IntegerField(blank=False , default=5)
	Subject_knowledge3 = models.IntegerField(blank=False, default=5)
	Behaviour3 = models.IntegerField(blank=False, default=5)
	Method_of_teaching3 = models.IntegerField(blank=False, default=5)
	Audibility3 = models.IntegerField(blank=False, default=5)
	Syllabus_coverage3 = models.IntegerField(blank=False, default=5)

	subject_name4=models.CharField(max_length=50, null=True)
	teacher_name4=models.CharField(max_length=50, null=True)
	Punctuality4 = models.IntegerField(blank=False , default=5)
	Subject_knowledge4 = models.IntegerField(blank=False, default=5)
	Behaviour4 = models.IntegerField(blank=False, default=5)
	Method_of_teaching4 = models.IntegerField(blank=False, default=5)
	Audibility4 = models.IntegerField(blank=False, default=5)
	Syllabus_coverage4 = models.IntegerField(blank=False, default=5)

	subject_name5=models.CharField(max_length=50, null=True)
	teacher_name5=models.CharField(max_length=50, null=True)
	Punctuality5 = models.IntegerField(blank=False , default=5)
	Subject_knowledge5 = models.IntegerField(blank=False, default=5)
	Behaviour5 = models.IntegerField(blank=False, default=5)
	Method_of_teaching5 = models.IntegerField(blank=False, default=5)
	Audibility5 = models.IntegerField(blank=False, default=5)
	Syllabus_coverage5 = models.IntegerField(blank=False, default=5)


	subject_name6=models.CharField(max_length=50, null=True)
	teacher_name6=models.CharField(max_length=50, null=True)
	Punctuality6 = models.IntegerField(blank=False , default=5)
	Subject_knowledge6 = models.IntegerField(blank=False, default=5)
	Behaviour6 = models.IntegerField(blank=False, default=5)
	Method_of_teaching6 = models.IntegerField(blank=False, default=5)
	Audibility6 = models.IntegerField(blank=False, default=5)
	Syllabus_coverage6 = models.IntegerField(blank=False, default=5)

	def __str__(self):
		return self.branch
