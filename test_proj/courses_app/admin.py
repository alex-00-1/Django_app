from django.contrib import admin
from courses_app.models import CoursesModel

# Register your models here.
# admin.site.register(CoursesModel)
@admin.register(CoursesModel)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag',]
