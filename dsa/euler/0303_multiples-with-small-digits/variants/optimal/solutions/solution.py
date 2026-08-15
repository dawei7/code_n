"""Project Euler 303: Multiples with Small Digits

Find sum_{n=1}^{10000} f(n) / n, where f(n) is the least positive multiple of n using only digits <= 2.
"""

from __future__ import annotations

from collections import deque


def find_f(n: int) -> int:
    """Finds the least positive multiple of n in base 10 using only digits in {0, 1, 2}

    via Breadth-First Search on remainder states modulo n.
    """
    if n == 1:
        return 1

    visited: list[tuple[int, int] | int] = [-1] * n
    queue: deque[int] = deque()

    for d in (1, 2):
        r = d % n
        if r == 0:
            return d
        if visited[r] == -1:
            visited[r] = (-2, d)
            queue.append(r)

    while queue:
        r = queue.popleft()
        for d in (0, 1, 2):
            nr = (r * 10 + d) % n
            if nr == 0:
                digits = [d]
                curr = r
                while curr != -2:
                    entry = visited[curr]
                    assert isinstance(entry, tuple)
                    prev_r, digit = entry
                    digits.append(digit)
                    curr = prev_r
                digits.reverse()
                val = 0
                for dig in digits:
                    val = val * 10 + dig
                return val

            if visited[nr] == -1:
                visited[nr] = (r, d)
                queue.append(nr)

    return 0


def solve(limit: int = 10_000) -> str:
    """Calculates sum_{n=1}^{limit} f(n) // n."""
    total = sum(find_f(n) // n for n in range(1, limit + 1))
    return str(total)


if __name__ == "__main__":
    print(solve())
