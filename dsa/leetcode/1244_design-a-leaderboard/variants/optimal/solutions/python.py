"""Optimal app-local adapter and reference class for LeetCode 1244."""

from heapq import nlargest


class Leaderboard:
    def __init__(self) -> None:
        self.scores: dict[int, int] = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        return sum(nlargest(K, self.scores.values()))

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]


def solve(operations: list[list]) -> list:
    leaderboard = Leaderboard()
    output = []
    for method, arguments in operations:
        if method == "addScore":
            output.append(leaderboard.addScore(*arguments))
        elif method == "top":
            output.append(leaderboard.top(*arguments))
        elif method == "reset":
            output.append(leaderboard.reset(*arguments))
        else:
            raise ValueError(f"unknown operation: {method}")
    return output
