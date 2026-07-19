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
        self.best: list[_WorstOfBest] = []
        self.remaining: list[tuple[int, str]] = []

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.remaining, (-score, name))
        if not self.best:
            return

        negative_score, candidate_name = self.remaining[0]
        candidate_score = -negative_score
        boundary = self.best[0]
        candidate_is_better = (
            candidate_score > boundary.score
            or (
                candidate_score == boundary.score
                and candidate_name < boundary.name
            )
        )
        if candidate_is_better:
            heapq.heappop(self.remaining)
            heapq.heappop(self.best)
            heapq.heappush(
                self.best,
                _WorstOfBest(candidate_score, candidate_name),
            )
            heapq.heappush(
                self.remaining,
                (-boundary.score, boundary.name),
            )

    def get(self) -> str:
        negative_score, name = heapq.heappop(self.remaining)
        heapq.heappush(self.best, _WorstOfBest(-negative_score, name))
        return self.best[0].name


def solve(
    operations: list[str],
    arguments: list[list[object]],
) -> list[str | None]:
    tracker: SORTracker | None = None
    output: list[str | None] = []

    for operation, args in zip(operations, arguments):
        if operation == "SORTracker":
            tracker = SORTracker()
            output.append(None)
        elif operation == "add":
            assert tracker is not None
            tracker.add(str(args[0]), int(args[1]))
            output.append(None)
        elif operation == "get":
            assert tracker is not None
            output.append(tracker.get())
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
