class BookMyShow:
    def __init__(self, n: int, m: int):
        size = 1
        while size < n:
            size *= 2
        self._n = n
        self._m = m
        self._size = size
        self._remaining = [m] * n
        self._maximum = [0] * (2 * size)
        self._total = [0] * (2 * size)
        for row in range(n):
            self._maximum[size + row] = m
            self._total[size + row] = m
        for node in range(size - 1, 0, -1):
            self._pull(node)

    def gather(self, k: int, maxRow: int) -> list[int]:
        row = self._first(1, 0, self._size - 1, maxRow, k)
        if row == -1 or row >= self._n:
            return []
        first_seat = self._m - self._remaining[row]
        self._remaining[row] -= k
        self._set(row)
        return [row, first_seat]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self._prefix_sum(maxRow + 1) < k:
            return False
        while k:
            row = self._first(1, 0, self._size - 1, maxRow, 1)
            booked = min(k, self._remaining[row])
            self._remaining[row] -= booked
            k -= booked
            self._set(row)
        return True

    def _pull(self, node: int) -> None:
        self._maximum[node] = max(
            self._maximum[node * 2], self._maximum[node * 2 + 1]
        )
        self._total[node] = self._total[node * 2] + self._total[node * 2 + 1]

    def _set(self, row: int) -> None:
        node = self._size + row
        self._maximum[node] = self._remaining[row]
        self._total[node] = self._remaining[row]
        node //= 2
        while node:
            self._pull(node)
            node //= 2

    def _first(
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
        result = self._first(node * 2, left, middle, max_row, needed)
        if result != -1:
            return result
        return self._first(
            node * 2 + 1, middle + 1, right, max_row, needed
        )

    def _prefix_sum(self, end: int) -> int:
        left = self._size
        right = self._size + end
        total = 0
        while left < right:
            if left % 2:
                total += self._total[left]
                left += 1
            if right % 2:
                right -= 1
                total += self._total[right]
            left //= 2
            right //= 2
        return total


def solve(
    operations: list[str],
    arguments: list[list[int]],
) -> list[list[int] | bool | None]:
    instance = None
    output: list[list[int] | bool | None] = []
    for operation, values in zip(operations, arguments):
        if operation == "BookMyShow":
            instance = BookMyShow(*values)
            output.append(None)
        elif operation == "gather":
            output.append(instance.gather(*values))
        else:
            output.append(instance.scatter(*values))
    return output
