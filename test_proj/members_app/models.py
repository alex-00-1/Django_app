from django.db import models



class MembersModel(models.Model):
    geneders = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('H', 'Hidden'),
    ]

    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField(unique=True, null=True)
    sex = models.CharField(choices=geneders, default="H", null=True)


    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    