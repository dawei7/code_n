from collections import defaultdict
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        count = defaultdict(int)
        pos_sum = defaultdict(int)
        count[0] = 1
        prefix = 0
        answer = 0
        for pos, value in enumerate(arr, 1):
            prefix ^= value
            answer += count[prefix] * (pos - 1) - pos_sum[prefix]
            count[prefix] += 1
            pos_sum[prefix] += pos
        out.append(str(answer))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
