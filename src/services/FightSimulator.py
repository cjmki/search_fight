from typing import Dict, List
from figters.Fighter import Fighter


class SearchBattleGround(object):
    def __init__(
        self, fight_params: List[str], fighters: List[Fighter]
    ) -> None:
        self._fight_params = fight_params
        self.fighters = fighters
        # {query[i]: [name: "", score: "", ...], ...}
        self.fight_state = {}
        self.score_board = ""
        self.high_score = 0
        self.winning_query = ""

    def fight(self) -> Dict:
        print(
            f"[*] Fight Simulator: fight initiated | total fighters - {len(self.fighters)} | total queries - {len(self._fight_params)} | total API requests - {len(self._fight_params) * len(self.fighters)}"
        )

        # TODO: O(N^2) find a more efficient way if possible (use a batch api request ?)
        for query in self._fight_params:
            # holds the info about current query (for each fighter)
            current_stats = []
            total = 0

            for fighter in self.fighters:
                # holds the info about fighter stats (name, total hits)
                current_fight_stats = {}

                current_fight_stats["name"] = fighter.get_name()
                current_fight_stats["score"] = fighter.make_search(query)
                total += current_fight_stats["score"]

                # maintain the individual state of fighter, to determine each fighter's highest score against query
                fighter.calibrate_score(current_fight_stats["score"], query)
                current_stats.append(current_fight_stats)

            if total > self.high_score:
                self.winning_query = query
                self.high_score = total

            self.fight_state[query] = current_stats

        return self.fight_state

    def show_scoreboard(self):
        fight_score = ""
        for state in self.fight_state:
            fight_score += f"\n{state}:"
            for fighter in self.fight_state[state]:
                name = fighter["name"]
                score = fighter["score"]
                fight_score += f" {name}: {score}"
        print(fight_score)

        for fighter in self.fighters:
            print(
                f"{fighter.get_name()} winner: {fighter.get_winning_query()}"
            )

        print(f"Total winner: {self.winning_query}")
        return None
