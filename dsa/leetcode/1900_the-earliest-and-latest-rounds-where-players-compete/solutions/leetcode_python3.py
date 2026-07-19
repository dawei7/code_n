from functools import lru_cache
from typing import List


class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
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

                next_positions = set()
                for before_first, before_second in positions:
                    for winner in winners:
                        next_positions.add(
                            (
                                before_first + (winner < first),
                                before_second + (winner < second),
                            )
                        )
                positions = next_positions

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
                next_first = before_first + 1
                next_second = before_second + 1
                child_earliest, child_latest = search(
                    next_count, next_first, next_second
                )
                earliest = min(earliest, child_earliest + 1)
                latest = max(latest, child_latest + 1)
            return earliest, latest

        return list(search(n, firstPlayer, secondPlayer))
