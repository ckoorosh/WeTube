from django.http import HttpResponse

VALID_IP_ADDRESSES = [
    '127.0.0.1:8001',
]


def get_proxy_url(request):
    for key, value in request.headers.items():
        if key.lower() == 'host':
            return value


def is_proxy(request):
    ip = get_proxy_url(request)
    return ip in VALID_IP_ADDRESSES


def proxy_required(view):
    def f(*args, **kwargs):
        request = args[0]
        ip = get_proxy_url(request)
        print(ip)
        if ip in VALID_IP_ADDRESSES:
            return view(*args, **kwargs)
        return HttpResponse(status=403)

    return f


def is_from_proxy(request):
    ip = get_proxy_url(request)
    if ip in VALID_IP_ADDRESSES:
        return True
    return False
