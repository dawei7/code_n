from heapq import heapify, heappop, heappush


def solve(classes: list[list[int]], extraStudents: int) -> float:
    heap = [
        (-(total - passed) / (total * (total + 1)), passed, total)
        for passed, total in classes
    ]
    heapify(heap)

    for _ in range(extraStudents):
        _, passed, total = heappop(heap)
        passed += 1
        total += 1
        heappush(
            heap,
            (-(total - passed) / (total * (total + 1)), passed, total),
        )

    return sum(passed / total for _, passed, total in heap) / len(classes)
