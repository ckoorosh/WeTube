from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import User
from .forms import SignupForm


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/login.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = User(username=username)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')

    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=raw_password)
    #         print(raw_password)
    #         print(user)
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = SignupForm()

    return render(request, 'accounts/signup.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def show_account(request):
    user = request.user
    if user.is_admin:
        return render(request, 'accounts/admin-account.html')
    elif user.is_manager:
        return render(request, 'accounts/manager-account.html')
    else:
        return render(request, 'accounts/user-account.html')


def send_ticket(request):
    pass
