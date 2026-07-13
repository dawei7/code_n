from collections import deque


def solve(mat):
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    start = 0
    for r in range(rows):
        for c in range(cols):
            if mat[r][c]:
                start |= 1 << (r * cols + c)
    if start == 0:
        return 0

    flips = []
    for r in range(rows):
        for c in range(cols):
            mask = 0
            for dr, dc in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    mask ^= 1 << (nr * cols + nc)
            flips.append(mask)

    queue = deque([(start, 0)])
    seen = {start}
    while queue:
        mask, steps = queue.popleft()
        for flip in flips:
            nxt = mask ^ flip
            if nxt == 0:
                return steps + 1
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, steps + 1))
    return -1
