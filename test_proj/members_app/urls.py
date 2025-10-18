from django.urls import path
from members_app.views import create_member


urlpatterns = [
    path('new/', create_member, name="create_member"),
]
