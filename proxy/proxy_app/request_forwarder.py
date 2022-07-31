import requests


def _refine_headers(headers, request):
    result = {}
    for key, value in headers.items():
        result[key] = value
    result['user-id'] = str(request.user.id)
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
        headers = _refine_headers(request.headers, request)
        params = request.GET
        url = f'{self.server_url}{request.path}'
        response = requests.request(request.method,
                                    url,
                                    params=_refine_params(params),
                                    data=data,
                                    )
        if len(response.history) > 0:
            last_response = response.history[-1]
            return last_response
        return response

    def send_post_request(self, data, path):
        url = f'{self.server_url}{path}'
        requests.post(url=url, data=data)
