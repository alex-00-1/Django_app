from django import forms
from courses_app.models import CoursesModel


class CourseForm(forms.ModelForm):
    class Meta:
        model = CoursesModel
        fields = ['title', 'description','member', 'tag']
        widgets = {
            'member': forms.CheckboxSelectMultiple()
        }

        labels = {
            'title': 'Назва курсу',
            'description': 'Опис курсу',
        }

        help_texts = {
            'title': 'Ввеідть назву Вашого завдання'
        }

        error_messages = {
            'title': {
                'required': "Обов'язковий для введення",
            },
        }
        