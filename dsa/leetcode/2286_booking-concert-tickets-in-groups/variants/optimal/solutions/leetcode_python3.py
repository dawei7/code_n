from typing import List


class BookMyShow:
    def __init__(self, n: int, m: int):
        self._rows = n
        self._seats_per_row = m
        self._remaining = [m] * n
        self._maximum = [0] * (4 * n)
        self._total = [0] * (4 * n)
        self._build(1, 0, n - 1)

    def gather(self, k: int, maxRow: int) -> List[int]:
        row = self._first_with_at_least(1, 0, self._rows - 1, maxRow, k)
        if row == -1:
            return []

        first_seat = self._seats_per_row - self._remaining[row]
        self._remaining[row] -= k
        self._update(1, 0, self._rows - 1, row)
        return [row, first_seat]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self._prefix_total(1, 0, self._rows - 1, maxRow) < k:
            return False

        while k:
            row = self._first_with_at_least(
                1, 0, self._rows - 1, maxRow, 1
            )
            booked = min(k, self._remaining[row])
            self._remaining[row] -= booked
            k -= booked
            self._update(1, 0, self._rows - 1, row)

        return True

    def _build(self, node: int, left: int, right: int) -> None:
        if left == right:
            self._maximum[node] = self._seats_per_row
            self._total[node] = self._seats_per_row
            return
        middle = (left + right) // 2
        self._build(node * 2, left, middle)
        self._build(node * 2 + 1, middle + 1, right)
        self._pull(node)

    def _pull(self, node: int) -> None:
        self._maximum[node] = max(
            self._maximum[node * 2], self._maximum[node * 2 + 1]
        )
        self._total[node] = (
            self._total[node * 2] + self._total[node * 2 + 1]
        )

    def _update(
        self, node: int, left: int, right: int, index: int
    ) -> None:
        if left == right:
            self._maximum[node] = self._remaining[index]
            self._total[node] = self._remaining[index]
            return
        middle = (left + right) // 2
        if index <= middle:
            self._update(node * 2, left, middle, index)
        else:
            self._update(node * 2 + 1, middle + 1, right, index)
        self._pull(node)

    def _first_with_at_least(
        self,
        node: int,
        left: int,
        right: int,
        max_row: int,
        needed: int,
    ) -> int:
        if left > max_row or self._maximum[node] < needed:
            return -1
        if left == right:
            return left
        middle = (left + right) // 2
        result = self._first_with_at_least(
            node * 2, left, middle, max_row, needed
        )
        if result != -1:
            return result
        return self._first_with_at_least(
            node * 2 + 1, middle + 1, right, max_row, needed
        )

    def _prefix_total(
        self, node: int, left: int, right: int, max_row: int
    ) -> int:
        if right <= max_row:
            return self._total[node]
        middle = (left + right) // 2
        total = self._prefix_total(node * 2, left, middle, max_row)
        if max_row > middle:
            total += self._prefix_total(
                node * 2 + 1, middle + 1, right, max_row
            )
        return total
