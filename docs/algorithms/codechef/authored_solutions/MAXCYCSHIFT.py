import sys
from collections import defaultdict


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n

        occ = defaultdict(int)
        distinct = 0
        pref = 0
        for value in arr:
            pref ^= value
            if occ[pref] == 0:
                distinct += 1
            occ[pref] += 1

        total = pref
        ans = 0
        for value in arr:
            pref ^= value
            if occ[pref] == 0:
                distinct += 1
            occ[pref] += 1

            old = pref ^ total
            occ[old] -= 1
            if occ[old] == 0:
                distinct -= 1
            if distinct > ans:
                ans = distinct

        out.append(str(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
