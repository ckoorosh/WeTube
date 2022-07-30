from django.http import HttpResponse

VALID_IP_ADDRESSES = [
    '127.0.0.1',
]


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def is_proxy(request):
    ip = get_client_ip(request)
    return ip in VALID_IP_ADDRESSES


def proxy_required(view):
    def f(*args, **kwargs):
        request = args[0]
        ip = get_client_ip(request)
        if ip in VALID_IP_ADDRESSES:
            return view(*args, **kwargs)
        return HttpResponse(status=403)

    return f


def is_from_proxy(request):
    ip = get_client_ip(request)
    if ip in VALID_IP_ADDRESSES:
        return True
    return False
