import sys

def minimum_energy(n: int, height: int, gaps: list[tuple[int, int]]) -> int:
    diff = [0] * (n + 1)
    for low, high in gaps:
        diff[low] += 1
        diff[high + 1] -= 1
    covered = [0] * n
    current = 0
    for row in range(n):
        current += diff[row]
        covered[row] = current
    window = sum(covered[:height])
    best = window
    for row in range(height, n):
        window += covered[row] - covered[row - height]
        if window > best:
            best = window
    return n * height - best

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, height = (data[idx], data[idx + 1])
        idx += 2
        gaps = [(data[idx + 2 * i], data[idx + 2 * i + 1]) for i in range(n)]
        idx += 2 * n
        out.append(str(minimum_energy(n, height, gaps)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
