from django.forms import ModelForm
from .models import student, ratings
from django import forms
 
choices = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)

class feedbackform(ModelForm):
	class Meta:
		model = ratings
		fields = "__all__"
		widgets =	{
			'Punctuality1': forms.RadioSelect(choices=choices,),
			'Subject_knowledge1': forms.RadioSelect(choices=choices,),
			'Behaviour1': forms.RadioSelect(choices=choices,),
			'Method_of_teaching1': forms.RadioSelect(choices=choices,),
			'Audibility1': forms.RadioSelect(choices=choices,),
			'Syllabus_coverage1': forms.RadioSelect(choices=choices,),
			'Punctuality2': forms.RadioSelect(choices=choices,),
			'Subject_knowledge2': forms.RadioSelect(choices=choices,),
			'Behaviour2': forms.RadioSelect(choices=choices,),
			'Method_of_teaching2': forms.RadioSelect(choices=choices,),
			'Audibility2': forms.RadioSelect(choices=choices,),
			'Syllabus_coverage2': forms.RadioSelect(choices=choices,),
			'Punctuality3': forms.RadioSelect(choices=choices,),
			'Subject_knowledge3': forms.RadioSelect(choices=choices,),
			'Behaviour3': forms.RadioSelect(choices=choices,),
			'Method_of_teaching3': forms.RadioSelect(choices=choices,),
			'Audibility3': forms.RadioSelect(choices=choices,),
			'Syllabus_coverage3': forms.RadioSelect(choices=choices,),
			'Punctuality4': forms.RadioSelect(choices=choices,),
			'Subject_knowledge4': forms.RadioSelect(choices=choices,),
			'Behaviour4': forms.RadioSelect(choices=choices,),
			'Method_of_teaching4': forms.RadioSelect(choices=choices,),
			'Audibility4': forms.RadioSelect(choices=choices,),
			'Syllabus_coverage4': forms.RadioSelect(choices=choices,),
			'Punctuality5': forms.RadioSelect(choices=choices,),
			'Subject_knowledge5': forms.RadioSelect(choices=choices,),
			'Behaviour5': forms.RadioSelect(choices=choices,),
			'Method_of_teaching5': forms.RadioSelect(choices=choices,),
			'Audibility5': forms.RadioSelect(choices=choices,),
			'Syllabus_coverage5': forms.RadioSelect(choices=choices,),
			'Punctuality6': forms.RadioSelect(choices=choices,),
			'Subject_knowledge6': forms.RadioSelect(choices=choices,),
			'Behaviour6': forms.RadioSelect(choices=choices,),
			'Method_of_teaching6': forms.RadioSelect(choices=choices,),
			'Audibility6': forms.RadioSelect(choices=choices,),
			'Syllabus_coverage6': forms.RadioSelect(choices=choices,)
			}


class info(ModelForm):
	class Meta:
		model = student
		fields = "__all__"