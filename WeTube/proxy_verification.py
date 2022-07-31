from django.http import HttpResponse

VALID_URL_ADDRESSES = [
    '127.0.0.1:8001',
]


def get_proxy_url(request):
    for key, value in request.headers.items():
        if key.lower() == 'host':
            return value


def proxy_required(view):
    def f(*args, **kwargs):
        request = args[0]
        url = get_proxy_url(request)
        if url in VALID_URL_ADDRESSES:
            return view(*args, **kwargs)
        return HttpResponse(status=403)

    return f


def is_from_proxy(request):
    url = get_proxy_url(request)
    return url in VALID_URL_ADDRESSES
