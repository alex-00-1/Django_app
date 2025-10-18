from django import forms
from courses_app.models import CoursesModel


class CourseForm(forms.ModelForm):
    class Meta:
        model = CoursesModel
        fields = ['title', 'description','member', 'tag']
        widgets = {
            'member': forms.CheckboxSelectMultiple()
        }
