import heapq
import sys

def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, a, b, x, y, z = data[idx:idx + 6]
        idx += 6
        supporters = data[idx:idx + n]
        idx += n
        days_before_hooli = ceil_div(z - b, y) - 1
        need = z - (a + days_before_hooli * x)
        if need <= 0:
            out.append('0')
            continue
        heap = [-value for value in supporters if value > 0]
        heapq.heapify(heap)
        used = 0
        while need > 0 and heap:
            value = -heapq.heappop(heap)
            need -= value
            used += 1
            value //= 2
            if value:
                heapq.heappush(heap, -value)
        out.append(str(used) if need <= 0 else 'RIP')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
