import heapq
import sys

def solve() -> None:
    lines = sys.stdin.buffer.read().splitlines()
    q = int(lines[0])
    top = []
    rest = []
    total = 0
    out = []

    def rebalance() -> None:
        target = total // 3
        while len(top) < target and rest:
            heapq.heappush(top, -heapq.heappop(rest))
        while len(top) > target:
            heapq.heappush(rest, -heapq.heappop(top))
        if rest and top and (-rest[0] > top[0]):
            small_top = heapq.heappop(top)
            large_rest = -heapq.heappop(rest)
            heapq.heappush(top, large_rest)
            heapq.heappush(rest, -small_top)
    for line in lines[1:]:
        parts = line.split()
        if parts[0] == b'1':
            x = int(parts[1])
            total += 1
            if top and x > top[0]:
                heapq.heappush(rest, -heapq.heapreplace(top, x))
            else:
                heapq.heappush(rest, -x)
            rebalance()
        elif top:
            out.append(str(top[0]))
        else:
            out.append('No reviews yet')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
