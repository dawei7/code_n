from heapq import nlargest


class Leaderboard:
    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] = self.scores.get(playerId, 0) + score

    def top(self, K: int) -> int:
        return sum(nlargest(K, self.scores.values()))

    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
