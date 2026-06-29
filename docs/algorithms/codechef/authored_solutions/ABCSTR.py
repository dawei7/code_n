from collections import defaultdict
import sys


def main() -> None:
    s = sys.stdin.buffer.read().strip()
    a = b = c = 0
    seen = defaultdict(int)
    seen[(0, 0)] = 1
    ans = 0
    for ch in s:
        if ch == 65:
            a += 1
        elif ch == 66:
            b += 1
        else:
            c += 1
        key = (a - b, a - c)
        ans += seen[key]
        seen[key] += 1
    print(ans)


if __name__ == "__main__":
    main()
