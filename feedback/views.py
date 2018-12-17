from django.shortcuts import render,HttpResponseRedirect
from feedback.forms import feedbackform, info
from .models import student,ratings as rt

def index(request):
    #return HttpResponse("hello");
	return render(request, 'feedback/index.html')
	
def student(request):
    if request.method == "POST":
        form = info(request.POST)
        if form.is_valid():
            actual_data=form.cleaned_data
            print(actual_data)
            
            new_instance = student(roll_no = actual_data['roll_no'],
                branch = actual_data['branch'],
                section = actual_data['section'])
            new_instance.save()
        return HttpResponseRedirect('/pages/fill.html/')

    else:
        form= info()
    return render(request, 'pages/student.html', {'form': form})
	
def fill(request):
    if request.method == "POST":
        form = feedbackform(request.POST)
        if form.is_valid():
            actual_data=form.cleaned_data
            print(actual_data)
            
            new_instance = rt(roll_no = actual_data['roll_no'],
                branch = actual_data['branch'],
                section = actual_data['section'],
                subject_name1 = actual_data['subject_name1'],
                teacher_name1 = actual_data['teacher_name1'],
                Punctuality1=actual_data['Punctuality1'],
                Subject_knowledge1=actual_data['Subject_knowledge1'],
                Behaviour1=actual_data['Behaviour1'],
                Method_of_teaching1=actual_data['Method_of_teaching1'],
                Audibility1=actual_data['Audibility1'],
                Syllabus_coverage1=actual_data['Syllabus_coverage1'],
                subject_name2 = actual_data['subject_name2'],
                teacher_name2 = actual_data['teacher_name2'],
                Punctuality2=actual_data['Punctuality2'],
                Subject_knowledge2=actual_data['Subject_knowledge2'],
                Behaviour2=actual_data['Behaviour2'],
                Method_of_teaching2=actual_data['Method_of_teaching2'],
                Audibility2=actual_data['Audibility2'],
                Syllabus_coverage2=actual_data['Syllabus_coverage2'],
                subject_name3 = actual_data['subject_name3'],
                teacher_name3 = actual_data['teacher_name3'],
                Punctuality3=actual_data['Punctuality3'],
                Subject_knowledge3=actual_data['Subject_knowledge3'],
                Behaviour3=actual_data['Behaviour3'],
                Method_of_teaching3=actual_data['Method_of_teaching3'],
                Audibility3=actual_data['Audibility3'],
                Syllabus_coverage3=actual_data['Syllabus_coverage3'],
                subject_name4 = actual_data['subject_name4'],
                teacher_name4 = actual_data['teacher_name4'],
                Punctuality4=actual_data['Punctuality4'],
                Subject_knowledge4=actual_data['Subject_knowledge4'],
                Behaviour4=actual_data['Behaviour4'],
                Method_of_teaching4=actual_data['Method_of_teaching4'],
                Audibility4=actual_data['Audibility4'],
                Syllabus_coverage4=actual_data['Syllabus_coverage4'],
                subject_name5 = actual_data['subject_name5'],
                teacher_name5 = actual_data['teacher_name5'],
                Punctuality5=actual_data['Punctuality5'],
                Subject_knowledge5=actual_data['Subject_knowledge5'],
                Behaviour5=actual_data['Behaviour5'],
                Method_of_teaching5=actual_data['Method_of_teaching5'],
                Audibility5=actual_data['Audibility5'],
                Syllabus_coverage5=actual_data['Syllabus_coverage5'],
                subject_name6 = actual_data['subject_name6'],
                teacher_name6 = actual_data['teacher_name6'],
                Punctuality6=actual_data['Punctuality6'],
                Subject_knowledge6=actual_data['Subject_knowledge6'],
                Behaviour6=actual_data['Behaviour6'],
                Method_of_teaching6=actual_data['Method_of_teaching6'],
                Audibility6=actual_data['Audibility6'],
                Syllabus_coverage6=actual_data['Syllabus_coverage6'])
            new_instance.save()
        return HttpResponseRedirect('/feedback')

    else:
        form= feedbackform()
    return render(request, 'pages/fill.html', {'form': form})

	
	

