import sys
from collections import defaultdict

def contribution(positions: list[int], value: int, n: int) -> int:
    if len(positions) < value:
        return 0
    total = 0
    for left in range(0, len(positions) - value + 1):
        right = left + value - 1
        prev_pos = positions[left - 1] if left else -1
        next_pos = positions[right + 1] if right + 1 < len(positions) else n
        total += (positions[left] - prev_pos) * (next_pos - positions[right]) * value
    return total

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        groups: dict[int, list[int]] = defaultdict(list)
        for i in range(n):
            value = data[idx + i]
            if value <= n:
                groups[value].append(i)
        idx += n
        ans = sum((contribution(pos, value, n) for value, pos in groups.items()))
        out.append(str(ans))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
