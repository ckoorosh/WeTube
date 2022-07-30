from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from proxy_app.request_forwarder import RequestForwarder

forwarder = RequestForwarder(scheme='http',
                             domain='127.0.0.1',
                             port=8000)


def proxy_view(request):
    content, status_code = forwarder.forward(request)
    return HttpResponse(content, status=status_code)
