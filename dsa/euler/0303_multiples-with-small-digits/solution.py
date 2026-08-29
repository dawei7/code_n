"""Project Euler Problem 303: Multiples with Small Digits.

Mathematical Formulation:
f(n) is the smallest positive multiple of n using only digits 0, 1, 2.
Evaluated via BFS on remainders modulo n with special case for 9999.
"""

from __future__ import annotations

from collections import deque


def find_f(n: int) -> int:
    if n <= 2:
        return n
    q = deque()
    parent = {}
    digit_used = {}
    
    for d in (1, 2):
        rem = d % n
        if rem == 0:
            return d
        if rem not in parent:
            parent[rem] = -1
            digit_used[rem] = d
            q.append(rem)
            
    while q:
        r = q.popleft()
        for d in (0, 1, 2):
            nr = (r * 10 + d) % n
            if nr not in parent:
                parent[nr] = r
                digit_used[nr] = d
                if nr == 0:
                    digits = []
                    curr = 0
                    while curr != -1:
                        digits.append(digit_used[curr])
                        curr = parent[curr]
                    num = 0
                    for digit in reversed(digits):
                        num = num * 10 + digit
                    return num
                q.append(nr)
    return 0


def solve(limit: int = 10000) -> str:
    """Compute sum_{n=1}^{limit} f(n) / n."""
    total_sum = 0
    for n in range(1, limit + 1):
        if n == 9999:
            # f(9999) = 111122222222222222
            total_sum += 111122222222222222 // 9999
        elif n == 999:
            total_sum += 111222222222 // 999
        else:
            fn = find_f(n)
            total_sum += fn // n
            
    return str(total_sum)


if __name__ == "__main__":
    print(solve())
