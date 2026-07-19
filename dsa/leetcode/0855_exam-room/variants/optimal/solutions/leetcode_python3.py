import heapq


class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.heap = []
        self.active = set()
        self.start_to_end = {}
        self.end_to_start = {}
        self._add_interval(-1, n)

    def _candidate(self, left: int, right: int):
        if left == -1:
            return 0, right
        if right == self.n:
            return self.n - 1, self.n - 1 - left
        seat = (left + right) // 2
        return seat, seat - left

    def _add_interval(self, left: int, right: int) -> None:
        self.active.add((left, right))
        self.start_to_end[left] = right
        self.end_to_start[right] = left
        if right - left > 1:
            seat, distance = self._candidate(left, right)
            heapq.heappush(self.heap, (-distance, seat, left, right))

    def _remove_interval(self, left: int, right: int) -> None:
        self.active.discard((left, right))
        if self.start_to_end.get(left) == right:
            del self.start_to_end[left]
        if self.end_to_start.get(right) == left:
            del self.end_to_start[right]

    def seat(self) -> int:
        while self.heap:
            _, seat, left, right = heapq.heappop(self.heap)
            if (left, right) in self.active:
                break

        self._remove_interval(left, right)
        self._add_interval(left, seat)
        self._add_interval(seat, right)
        return seat

    def leave(self, p: int) -> None:
        left = self.end_to_start[p]
        right = self.start_to_end[p]
        self._remove_interval(left, p)
        self._remove_interval(p, right)
        self._add_interval(left, right)
