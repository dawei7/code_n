import heapq
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, x, y = (data[idx], data[idx + 1], data[idx + 2])
        idx += 3
        heap = data[idx:idx + n]
        idx += n
        heapq.heapify(heap)
        while y > 0:
            u = heap[0]
            v = u ^ x
            if v < u:
                break
            heapq.heapreplace(heap, v)
            y -= 1
        if y & 1:
            u = heapq.heappop(heap)
            heapq.heappush(heap, u ^ x)
        out.append(' '.join(map(str, sorted(heap))))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
