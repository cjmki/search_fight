from http import client
from urllib.parse import urlencode


class HttpClient(object):
    def __init__(self, api_endpoint) -> None:
        self.connection = client.HTTPSConnection(api_endpoint)
        self.connection.connect()

    def __enter__(self) -> client.HTTPConnection:
        return self.connection

    def __exit__(self, exception_type, exception_value, traceback) -> None:
        self.connection.close()

    def gen_request_url(api_endpoint, params) -> str:
        encoded_params = urlencode(params)
        return f"{api_endpoint}?{encoded_params}"
