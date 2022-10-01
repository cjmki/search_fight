from src.figters.Bing import Bing
from src.figters.Google import Google
from src.services.FightSimulator import SearchBattleGround
from unittest import mock


def mock_google_make_search(self, q):
    return 15000


def mock_bing_make_search(self, q):
    return 20000


def test_battle_ground():

    with mock.patch.object(
        Google, "make_search", new=mock_google_make_search
    ), mock.patch.object(Bing, "make_search", new=mock_bing_make_search):
        _mock_fighters = []
        _mock_fighters.append(Google())
        _mock_fighters.append(Bing())

        _queries = ["jeff bezos", "aaron swartz"]

        battleGround = SearchBattleGround(_queries, _mock_fighters)
        fight_state = battleGround.fight()

        _expected_fight_state = {
            "jeff bezos": [
                {"name": "Google", "score": 15000},
                {"name": "Bing", "score": 20000},
            ],
            "aaron swartz": [
                {"name": "Google", "score": 15000},
                {"name": "Bing", "score": 20000},
            ],
        }

        assert fight_state == _expected_fight_state
