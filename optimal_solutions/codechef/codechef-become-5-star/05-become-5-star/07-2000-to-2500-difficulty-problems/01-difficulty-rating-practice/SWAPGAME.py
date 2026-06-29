from collections import defaultdict, deque
import sys

class Fenwick:

    def __init__(self, n):
        self.n = n
        self.count = [0] * (n + 1)
        self.total = [0] * (n + 1)

    def add(self, idx, cnt, value):
        while idx <= self.n:
            self.count[idx] += cnt
            self.total[idx] += value
            idx += idx & -idx

    def sum(self, idx):
        cnt = total = 0
        while idx:
            cnt += self.count[idx]
            total += self.total[idx]
            idx -= idx & -idx
        return (cnt, total)

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n
        b = data[idx:idx + n]
        idx += n
        positions = defaultdict(deque)
        for pos, value in enumerate(b, 1):
            positions[value].append(pos)
        bit = Fenwick(n)
        answer = 0
        for value in a:
            pos = positions[value].popleft()
            before_count, before_sum = bit.sum(pos)
            seen_count, seen_sum = bit.sum(n)
            inv_count = seen_count - before_count
            inv_sum = seen_sum - before_sum
            answer += inv_sum - inv_count * value
            bit.add(pos, 1, value)
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
