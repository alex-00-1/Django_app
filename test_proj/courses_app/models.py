from django.db import models
from members_app.models import MembersModel

# Create your models here.
class CoursesModel(models.Model):
    title = models.CharField(max_length=55, unique=True)
    description = models.TextField(max_length=155)
    tag = models.CharField(max_length=10, unique=True)
    member = models.ManyToManyField(MembersModel, related_name="courses")
    

    def __str__(self):
        return self.title
