from django.db import models


# Константа, яка створюєтья напряму через СУБД. Допустимі значення -> ["Male", "Female", "Hidden"]
class MemberSex(models.Model):
    sex = models.CharField()

    def __str__(self):
        return self.sex


class MembersModel(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    age = models.IntegerField()
    email = models.EmailField(unique=True, null=True)
    sex = models.ForeignKey(MemberSex, on_delete=models.SET_NULL , null=True, default="Hidden")


    def __str__(self):
        return f'{self.firstname} {self.lastname}'
    