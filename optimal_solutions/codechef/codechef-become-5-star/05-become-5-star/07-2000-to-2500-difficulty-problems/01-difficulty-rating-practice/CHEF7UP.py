import bisect
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        chef = data[idx + 1]
        idx += 2
        police = data[idx:idx + n]
        idx += n
        police.sort()
        pos = bisect.bisect_left(police, chef)
        ans = 0
        left = pos - 1
        while left >= 0 and police[left] & 1 != chef & 1:
            ans += 1
            left -= 1
        right = pos
        while right < n and police[right] & 1 != chef & 1:
            ans += 1
            right += 1
        out.append(f'{ans} {(1 if ans == n else -1)}')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
