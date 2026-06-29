import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, q = data[idx], data[idx + 1]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        pref = [0] * (n + 2)
        suff = [0] * (n + 3)
        for i, value in enumerate(arr, start=1):
            pref[i] = math.gcd(pref[i - 1], value)
        for i in range(n, 0, -1):
            suff[i] = math.gcd(suff[i + 1], arr[i - 1])
        for _query in range(q):
            left, right = data[idx], data[idx + 1]
            idx += 2
            out.append(str(math.gcd(pref[left - 1], suff[right + 1])))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
