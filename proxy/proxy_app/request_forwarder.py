import requests


def _refine_headers(headers, port):
    result = {}
    for key, value in headers.items():
        result[key] = value
    result['REMOTE_PORT'] = port
    return result


def _refine_params(params):
    result = {}
    for key, value in params.items():
        result[key] = value
    return result


class RequestForwarder:
    """
    This class is responsible for forwarding a django request to a specified
    URL, and return an exact copy of the response to the client.
    """

    def __init__(self, scheme, domain, port):
        self.server_url = f'{scheme}://{domain}:{port}'

        if self.server_url[-1] == '/':
            self.server_url = self.server_url[:-1]

    def forward(self, request):
        data = request.body
        headers = _refine_headers(request.headers, request.META.get('SERVER_PORT'))
        params = request.GET
        url = f'{self.server_url}{request.path}'
        response = requests.request(request.method,
                                    url,
                                    params=_refine_params(params),
                                    data=data,
                                    headers=headers)

        return response.content, response.status_code
