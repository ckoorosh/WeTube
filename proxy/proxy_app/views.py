from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from proxy_app.request_forwarder import RequestForwarder

forwarder = RequestForwarder(scheme='http',
                             domain='127.0.0.1',
                             port=8000)


def proxy_view(request):
    response = forwarder.forward(request)
    if response.status_code == 302:
        # Here we need to redirect to the value of 'Location' header
        return HttpResponseRedirect(response.headers.get('Location'))
    return HttpResponse(response.content, status=response.status_code)
