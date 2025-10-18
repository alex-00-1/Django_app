from django.urls import path
from courses_app.views import course_list, create_course


urlpatterns = [
    path('', course_list, name='course_list'),
    path('create/', create_course, name="create_course")
]