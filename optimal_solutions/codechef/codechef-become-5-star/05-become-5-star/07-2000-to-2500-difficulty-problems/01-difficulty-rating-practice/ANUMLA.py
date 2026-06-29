from collections import Counter
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        sums = sorted(data[idx:idx + (1 << n)])
        idx += 1 << n
        counts = Counter(sums)
        counts[0] -= 1
        made = [0]
        ans = []
        for value in sums:
            if counts[value] <= 0:
                continue
            ans.append(value)
            new_sums = [x + value for x in made]
            for x in new_sums:
                counts[x] -= 1
            made += new_sums
            if len(ans) == n:
                break
        out.append(' '.join(map(str, ans)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
