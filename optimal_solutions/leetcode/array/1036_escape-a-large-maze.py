"""Optimal solution for LeetCode 1036: Escape a Large Maze."""

from collections import deque


def solve(blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
    blocked_set = {tuple(cell) for cell in blocked}
    limit = len(blocked) * (len(blocked) - 1) // 2
    size = 1_000_000

    def can_escape(start: tuple[int, int], finish: tuple[int, int]) -> bool:
        queue: deque[tuple[int, int]] = deque([start])
        seen = {start}
        while queue and len(seen) <= limit:
            r, c = queue.popleft()
            if (r, c) == finish:
                return True
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                nxt = (nr, nc)
                if 0 <= nr < size and 0 <= nc < size and nxt not in blocked_set and nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return len(seen) > limit

    src = (source[0], source[1])
    dst = (target[0], target[1])
    return can_escape(src, dst) and can_escape(dst, src)
