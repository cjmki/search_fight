import requests
import constants

# https://www.googleapis.com/customsearch/v1?key=INSERT_YOUR_API_KEY&cx=017576662512468239146:omuauf_lfve&q=lectures


def google_make_request():
    params = {
        "key": constants.GOOGLE_API_KEY,
        "cx": "a3307a6a039e048b0",
        "q": "charith jayawardana",
    }
    response = requests.get(constants.GOOGLE_API_HOST, params=params)
    jsonFormat = response.json()
    # for i in jsonFormat:
    #     print("key: ", i, "val: ", jsonFormat[i])
    return jsonFormat["queries"]["request"][0]["totalResults"]


def bing_make_request():
    headers = {"Ocp-Apim-Subscription-Key": constants.BING_API_KEY}
    params = {
        "q": " charith jayawardana",
        "textDecorations": True,
        "textFormat": "HTML",
    }
    response = requests.get(
        constants.BING_API_HOST, params=params, headers=headers
    )
    jsonFormat = response.json()
    return jsonFormat["webPages"]["totalEstimatedMatches"]
