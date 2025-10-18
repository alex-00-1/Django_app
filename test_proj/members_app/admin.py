from django.contrib import admin
from members_app.models import MembersModel


# admin.site.register(MembersModel)
@admin.register(MembersModel)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'age', 'sex',]