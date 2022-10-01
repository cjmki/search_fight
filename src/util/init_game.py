from figters.Bing import Bing
from figters.Google import Google


def init_fighters():
    _fighters = []
    _fighters.append(Google())
    _fighters.append(Bing())

    return _fighters
