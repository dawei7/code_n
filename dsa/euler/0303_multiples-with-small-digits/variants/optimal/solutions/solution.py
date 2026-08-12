from collections import deque


def solve(limit: int = 10000) -> int:
    """Find sum_{n=1..10000} f(n)/n where f(n) is the least positive multiple of n using only digits <= 2.
    
    Time Complexity: O(limit * n_states) via Breadth-First Search Modulo n
    Space Complexity: O(n)
    """

    def get_f_over_n(n):
        parent = {}
        q = deque()
        for d in (1, 2):
            r = d % n
            if r not in parent:
                parent[r] = (-1, d)
                q.append(r)

        while q:
            r = q.popleft()
            if r == 0:
                break
            for d in (0, 1, 2):
                next_r = (r * 10 + d) % n
                if next_r not in parent:
                    parent[next_r] = (r, d)
                    q.append(next_r)

        digits = []
        curr = 0
        while curr != -1:
            prev_r, d = parent[curr]
            digits.append(str(d))
            curr = prev_r
        num_str = "".join(reversed(digits))
        return int(num_str) // n

    return sum(get_f_over_n(n) for n in range(1, limit + 1))
