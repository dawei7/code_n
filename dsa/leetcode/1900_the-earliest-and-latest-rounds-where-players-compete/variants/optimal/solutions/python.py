from functools import lru_cache


def solve(n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
    @lru_cache(None)
    def search(player_count: int, first: int, second: int) -> tuple[int, int]:
        if first + second == player_count + 1:
            return 1, 1

        positions = {(0, 0)}
        for left in range(1, player_count // 2 + 1):
            right = player_count + 1 - left
            if first in (left, right):
                winners = (first,)
            elif second in (left, right):
                winners = (second,)
            else:
                winners = (left, right)

            positions = {
                (before_first + (winner < first), before_second + (winner < second))
                for before_first, before_second in positions
                for winner in winners
            }

        if player_count % 2:
            middle = player_count // 2 + 1
            positions = {
                (
                    before_first + (middle < first),
                    before_second + (middle < second),
                )
                for before_first, before_second in positions
            }

        earliest = player_count
        latest = 0
        next_count = (player_count + 1) // 2
        for before_first, before_second in positions:
            child = search(next_count, before_first + 1, before_second + 1)
            earliest = min(earliest, child[0] + 1)
            latest = max(latest, child[1] + 1)
        return earliest, latest

    return list(search(n, firstPlayer, secondPlayer))
