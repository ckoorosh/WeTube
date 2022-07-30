import requests


class RequestForwarder:
    """
    This class is responsible for forwarding a django request to a specified
    URL, and return an exact copy of the response to the client.
    """

    def __init__(self, server_url):
        self.server_url = server_url

    def forward(self, request):
        data = request.body
        headers = request.META

        response = requests.request(request.method,
                                    self.server_url,
                                    data=data,
                                    headers=headers)

        return response.text