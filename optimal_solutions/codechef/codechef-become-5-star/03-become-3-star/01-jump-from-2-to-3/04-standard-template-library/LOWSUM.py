import heapq
import sys

def kth_sums(a: list[int], b: list[int], queries: list[int]) -> list[int]:
    a.sort()
    b.sort()
    need = max(queries)
    limit = min(len(a), need)
    heap = [(a[i] + b[0], i, 0) for i in range(limit)]
    heapq.heapify(heap)
    values = [0] * (need + 1)
    for rank in range(1, need + 1):
        value, i, j = heapq.heappop(heap)
        values[rank] = value
        if j + 1 < len(b):
            heapq.heappush(heap, (a[i] + b[j + 1], i, j + 1))
    return [values[q] for q in queries]

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        k, q = (data[idx], data[idx + 1])
        idx += 2
        a = data[idx:idx + k]
        idx += k
        b = data[idx:idx + k]
        idx += k
        queries = data[idx:idx + q]
        idx += q
        out.extend(map(str, kth_sums(a, b, queries)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
