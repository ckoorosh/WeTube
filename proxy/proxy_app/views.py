from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

# Create your views here.
import json
from .request_forwarder import RequestForwarder
from .models import User

forwarder = RequestForwarder(scheme='http',
                             domain='127.0.0.1',
                             port=8000)


def home(request):
    if request.user.is_authenticated:
        return proxy_view(request)
    else:
        return redirect('admin-login')


def admin_signin(request):
    if request.method == "POST":
        response = forwarder.forward(request)
        if response.status_code == 200:
            user_id = int(response.text)
            user, created = User.objects.get_or_create(id=user_id, username=request.POST['username'])
            if created:
                user.save()
            login(request, user)
            return redirect('home')

    return render(request, 'proxy_app/admin-login.html')


def admin_signup(request):
    if request.method == "POST":
        response = forwarder.forward(request)
        if response.status_code == 200:
            return redirect('home')

    return render(request, 'proxy_app/admin-signup.html')


def logout_user(request):
    logout(request)
    return redirect('admin-login')


def proxy_view(request):
    if request.user.is_authenticated:
        request.session['user_id'] = request.user.id
    response = forwarder.forward(request)
    if response.status_code == 302:
        # Here we need to redirect to the value of 'Location' header
        return HttpResponseRedirect(response.headers.get('Location'))
    return HttpResponse(response.content, status=response.status_code)
