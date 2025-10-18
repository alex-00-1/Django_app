from django import forms
from members_app.models import MembersModel


class MemberForm(forms.ModelForm):
    class Meta:
        model = MembersModel
        fields = ['firstname', 'lastname','age', 'email', 'sex',]
