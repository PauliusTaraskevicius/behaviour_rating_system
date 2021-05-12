from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import RegistrationForm
from .models import User, UserWorkOffice

@login_required
def user_details(request, pk):
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'users/user_details.html', context)

@login_required
def users_list(request):
    offices = UserWorkOffice.objects.all()
    context = {
        'offices': offices,
    }
    return render(request, 'users/users_list.html', context)

@login_required
def list_of_offices(request):
    offices = UserWorkOffice.objects.order_by("office_name")
    context = {
        'offices': offices,
    }
    return render(request, 'users/list_of_offices.html', context)

@login_required
def list_of_users_by_office(request, office_slug):
    offices = UserWorkOffice.objects.all()
    queryset = User.objects.all()
    if office_slug:
        work_office = get_object_or_404(UserWorkOffice, slug=office_slug)
        queryset = queryset.filter(work_office=work_office)

    context = {
        'offices': offices,
        'queryset': queryset,
        'work_office': work_office
    }
    return render(request, 'users/list_of_users_by_office.html', context)


def register(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.phone_number = registerForm.cleaned_data['phone_number']
            user.first_name = registerForm.cleaned_data['first_name']
            user.last_name = registerForm.cleaned_data['last_name']
            user.work_office = registerForm.cleaned_data['work_office']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = True
            user.save()
            registerForm.save_m2m()
            login(request, user)
            return redirect("/home")
    else:
        registerForm = RegistrationForm()
    return render(request, 'users/register.html', {'form': registerForm})
