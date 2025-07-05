from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required
from .forms import SimpleUserEditForm
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/accounts/')  # arahkan ke halaman utama setelah login
        else:
            messages.error(request, 'Username atau password salah.')

    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})


@login_required(login_url='/accounts/login/')
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = SimpleUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')
    else:
        form = SimpleUserEditForm(instance=user)

    return render(request, 'accounts/edit_user.html', {'form': form, 'user': user})

@login_required(login_url='/accounts/login/')
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('/accounts/')

    return render(request, 'accounts/delete_user.html', {'user': user})