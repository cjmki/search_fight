from src.services.HttpClient import HttpClient
import src.util.constants as constants
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            {
                "key": "random_key",
                "cx": "random_cx",
                "q": "jeff bezos",
            },
            "/customsearch/v1?key=random_key&cx=random_cx&q=jeff+bezos",
        )
    ],
)
def test_gen_request_url(test_input, expected):
    _url = HttpClient.gen_request_url(
        constants.GOOGLE_API_ENDPOINT, test_input
    )
    assert _url == expected
