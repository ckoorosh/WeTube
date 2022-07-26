from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import User
from videos.models import Ticket


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
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html')
        else:
            user = User(username=username)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

    return render(request, 'accounts/signup.html')


@login_required(redirect_field_name='login')
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(redirect_field_name='login')
def show_account(request):
    user = request.user
    if user.is_admin:
        return render(request, 'accounts/admin-account.html')
    elif user.is_manager:
        return render(request, 'accounts/manager-account.html')
    else:
        videos = user.video_set.all()
        tickets = user.ticket_set.all()
        context = {
            'videos': videos,
            'tickets': tickets
        }
        return render(request, 'accounts/user-account.html', context=context)


@login_required(redirect_field_name='login')
def send_ticket(request):
    if request.method == "POST":
        title = request.POST.get('title', None)
        body = request.POST.get('body', None)
        if title:
            ticket = Ticket(title=title, body=body, user=request.user)
            ticket.save()

    return redirect(request.META['HTTP_REFERER'])
