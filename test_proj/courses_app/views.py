from django.shortcuts import render, redirect
from courses_app.models import CoursesModel
from courses_app.forms import CourseForm


def course_list(request):
    courses = CoursesModel.objects.all()

    if request.method == 'GET':
        return render(request, 'course_list.html', {"courses": courses})
    

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})