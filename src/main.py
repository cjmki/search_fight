import sys
from figters.Google import Google
from figters.Bing import Bing
from services.FightSimulator import SearchBattleGround
from util.argv_util import read_argv
from util.init_game import init_fighters

if __name__ == "__main__":

    _fighters = init_fighters()
    _search_queries = read_argv(sys.argv)
    battleGround = SearchBattleGround(_search_queries, _fighters)
    battleGround.fight()
    battleGround.show_scoreboard()
