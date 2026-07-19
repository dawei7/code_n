import heapq


class _FractionEntry:
    __slots__ = ("numerator", "denominator", "values")

    def __init__(self, numerator: int, denominator: int, values: list[int]):
        self.numerator = numerator
        self.denominator = denominator
        self.values = values

    def __lt__(self, other: "_FractionEntry") -> bool:
        return (
            self.values[self.numerator] * self.values[other.denominator]
            < self.values[other.numerator] * self.values[self.denominator]
        )


def solve(arr: list[int], k: int) -> list[int]:
    last = len(arr) - 1
    heap = [_FractionEntry(index, last, arr) for index in range(last)]
    heapq.heapify(heap)

    entry = heap[0]
    for _ in range(k):
        entry = heapq.heappop(heap)
        next_denominator = entry.denominator - 1
        if next_denominator > entry.numerator:
            heapq.heappush(
                heap,
                _FractionEntry(entry.numerator, next_denominator, arr),
            )

    return [arr[entry.numerator], arr[entry.denominator]]
