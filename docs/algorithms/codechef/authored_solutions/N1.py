import sys
from collections import deque


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    idx = 1
    out = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for _ in range(t):
        n = int(tokens[idx])
        idx += 1
        grid = [tokens[idx + i].decode() for i in range(n)]
        idx += n
        treasure_id = {}
        for i in range(n):
            for j, ch in enumerate(grid[i]):
                if ch == "*":
                    treasure_id[(i, j)] = len(treasure_id)
        all_mask = (1 << len(treasure_id)) - 1
        start_mask = 0
        if (0, 0) in treasure_id:
            start_mask |= 1 << treasure_id[(0, 0)]
        queue = deque([(0, 0, start_mask, 0)])
        seen = {(0, 0, start_mask)}
        answer = -1
        while queue:
            x, y, mask, dist = queue.popleft()
            if x == n - 1 and y == n - 1 and mask == all_mask:
                answer = dist
                break
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n) or grid[nx][ny] == "#":
                    continue
                new_mask = mask
                if (nx, ny) in treasure_id:
                    new_mask |= 1 << treasure_id[(nx, ny)]
                state = (nx, ny, new_mask)
                if state not in seen:
                    seen.add(state)
                    queue.append((nx, ny, new_mask, dist + 1))
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
