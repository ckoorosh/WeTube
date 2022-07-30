from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers

from proxy_verification import proxy_required, is_proxy
from .models import User
from videos.models import Ticket, TicketResponse


def get_user(request):
    if 'user-id' in request.headers:
        user_id = int(request.headers['user-id'])
        if user_id:
            return User.objects.get(id=user_id)

    return request.user


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if not user.is_admin:
                login(request, user)
                return redirect('home')

    return render(request, 'accounts/login.html')


@proxy_required
def admin_signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_admin and user.is_verified:
                login(request, user)
                return HttpResponse(user.id, status=200)

    return HttpResponse(status=403)


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


@proxy_required
def admin_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse(status=403)
        else:
            user = User(username=username)
            user.set_password(password)
            user.is_admin = True
            user.save()
            return HttpResponse(status=200)

    return HttpResponse(status=403)


# @login_required(redirect_field_name='login')
def logout_user(request):
    logout(request)
    return redirect('home')


# @login_required(redirect_field_name='login')
def show_account(request):
    user = get_user(request)
    if user.is_admin:
        struck_users = User.objects.filter(strike=True)
        user_tickets = Ticket.objects.filter(user__is_admin=False)
        tickets = user.ticket_set.all()

        context = {
            'struck_users': struck_users,
            'user_tickets': user_tickets,
            'tickets': tickets,
            'user': get_user(request)
        }
        return render(request, 'accounts/admin-account.html', context=context)
    elif user.is_manager:
        admin_tickets = Ticket.objects.filter(user__is_admin=True)
        unverified_admins = User.objects.filter(is_admin=True, is_verified=False)
        context = {
            'admin_tickets': admin_tickets,
            'unverified_admins': unverified_admins
        }
        return render(request, 'accounts/manager-account.html', context=context)
    else:
        videos = user.video_set.all()
        tickets = user.ticket_set.all()
        context = {
            'videos': videos,
            'tickets': tickets
        }
        return render(request, 'accounts/user-account.html', context=context)


# @login_required(redirect_field_name='login')
def send_ticket(request):
    user = get_user(request)
    if request.method == "POST":
        title = request.POST.get('title', None)
        body = request.POST.get('body', None)
        if title:
            ticket = Ticket(title=title, body=body, user=user)
            ticket.save()

    if user.is_admin:
        return show_account(request)
    else:
        return redirect('account')


# TODO: ?
def respond_ticket(request, pk):
    user = get_user(request)
    if request.method == "POST":
        if user.is_admin or user.is_manager:
            ticket = Ticket.objects.get(pk=pk)
            if ticket:
                body = request.POST.get('body', None)
                if body:
                    response = TicketResponse(user=user, body=body)
                    response.save()
                    ticket.response = response
                    ticket.save()

    if user.is_admin:
        return show_account(request)
    else:
        return redirect('account')


# TODO: ?
def change_ticket_status(request, pk):
    user = get_user(request)
    if request.method == "POST":
        if user.is_admin or user.is_manager:
            ticket = Ticket.objects.get(pk=pk)
            if ticket:
                if ticket.status != 'c':
                    status = request.POST.get("status")
                    ticket.set_status(status)

    return redirect('account')


@proxy_required
def unstrike(request, pk):
    user = get_user(request)
    if user.is_admin:
        user = User.objects.get(pk=pk)
        if user:
            user.set_strike(False)

    if user.is_admin:
        return show_account(request)
    else:
        return redirect('account')


def verify(request, pk):
    user = get_user(request)
    if user.is_manager:
        user = User.objects.get(pk=pk)
        if user and user.is_admin:
            user.verify()

    return redirect('account')
