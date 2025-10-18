from django.shortcuts import render, redirect
from members_app.models import MembersModel
from members_app.forms import MemberForm

# # Create your views here.
# def member_list():
#     pass


def create_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create/')
    else:
        form = MemberForm()
    return render(request, 'create_member.html', {'form': form})