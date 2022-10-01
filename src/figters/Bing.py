from services.HttpClient import HttpClient
from .Fighter import Fighter
import json
import util.constants as constants


class Bing(Fighter):
    def __init__(self):
        self._api_key = constants.BING_API_KEY
        self._api_host = constants.BING_API_HOST
        self._api_endpoint = constants.BING_API_ENDPOINT
        super().__init__("Bing")

    def make_search(self, q):
        # TODO: good if we can send in a param fields (like in mongo queries) so we would return only the necessary fields - total hits
        params = {
            "q": q,
            "textDecorations": True,
            "textFormat": "HTML",
        }
        headers = {"Ocp-Apim-Subscription-Key": self._api_key}

        url = HttpClient.gen_request_url(self._api_endpoint, params)

        with HttpClient(self._api_host) as connection:
            connection.request("GET", url=url, headers=headers)
            response = connection.getresponse()
            self.validate_api_response(response)
            return self.deserialize_res(response.read())

    def deserialize_res(self, res):
        res = json.loads(res)
        return int(res["webPages"]["totalEstimatedMatches"])
