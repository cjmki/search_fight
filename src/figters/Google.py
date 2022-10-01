from services.HttpClient import HttpClient
from .Fighter import Fighter
import json
import util.constants as constants


class Google(Fighter):
    def __init__(self) -> None:
        self._api_key = constants.GOOGLE_API_KEY
        self._api_host = constants.GOOGLE_API_HOST
        self._api_endpoint = constants.GOOGLE_API_ENDPOINT
        self._api_cx = constants.GOOGLE_API_CX
        super().__init__("Google")

    def make_search(self, q):
        # TODO: good if we can send in a param fields (like in mongo queries) so we would return only the necessary fields - total hits
        params = {
            "key": self._api_key,
            "cx": self._api_cx,
            "q": q,
        }

        url = HttpClient.gen_request_url(self._api_endpoint, params)

        with HttpClient(self._api_host) as connection:
            connection.request("GET", url=url)
            response = connection.getresponse()
            self.validate_api_response(response)
            return self.deserialize_res(response.read())

    def deserialize_res(self, res):
        res = json.loads(res)
        return int(res["queries"]["request"][0]["totalResults"])
