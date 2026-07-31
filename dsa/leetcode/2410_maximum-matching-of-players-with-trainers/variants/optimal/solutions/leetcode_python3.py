from typing import List


class Solution:
    def matchPlayersAndTrainers(
        self,
        players: List[int],
        trainers: List[int],
    ) -> int:
        players.sort()
        trainers.sort()

        player_index = 0
        for capacity in trainers:
            if player_index < len(players) and players[player_index] <= capacity:
                player_index += 1
        return player_index
