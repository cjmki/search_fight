# Abstract class of all fighter classes (each search engine)
class Fighter(object):
    def __init__(self, name) -> None:
        self._name = name
        self.high_score = 0
        self.winning_query = ""

    def set_high_score(self, high_score):
        self.high_score = high_score

    def get_high_score(self):
        return self.high_score

    def set_winnig_query(self, query):
        self.winning_query = query

    def get_winning_query(self):
        return self.winning_query

    def calibrate_score(self, score, query):
        if score > self.high_score:
            self.high_score = score
            self.winning_query = query

    def get_name(self) -> str:
        return self._name

    def make_search(self, q):
        pass

    def deserialize_res(self):
        pass

    """
    considering a scenario if theres equal to or more than two players, game should continue.
    we can remove the figher in fighters arr in BattleGround object and continue the fight. Also we can
    consider removing existing stats related to that fighter from fight_state in BattleGround object
    """

    def validate_api_response(self, response):
        if response.status != 200:
            print(
                f"[*] Fighter: name - {self._name} | player disqualified | reason - {response.reason}"
            )
            print("[*] Fight Simulator: exiting game")
            exit()
