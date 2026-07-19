import heapq


class _WorstOfBest:
    def __init__(self, score: int, name: str):
        self.score = score
        self.name = name

    def __lt__(self, other: "_WorstOfBest") -> bool:
        if self.score != other.score:
            return self.score < other.score
        return self.name > other.name


class SORTracker:
    def __init__(self):
        self.best = []
        self.remaining = []

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.remaining, (-score, name))
        if self.best:
            best_remaining_score, best_remaining_name = self.remaining[0]
            worst_best = self.best[0]
            candidate_score = -best_remaining_score
            candidate_is_better = (
                candidate_score > worst_best.score
                or (
                    candidate_score == worst_best.score
                    and best_remaining_name < worst_best.name
                )
            )
            if candidate_is_better:
                heapq.heappop(self.remaining)
                heapq.heappop(self.best)
                heapq.heappush(
                    self.best,
                    _WorstOfBest(candidate_score, best_remaining_name),
                )
                heapq.heappush(
                    self.remaining,
                    (-worst_best.score, worst_best.name),
                )

    def get(self) -> str:
        negative_score, name = heapq.heappop(self.remaining)
        heapq.heappush(self.best, _WorstOfBest(-negative_score, name))
        return self.best[0].name
