import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx:idx + 2]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        if 2 * k <= n:
            out.append(" ".join(map(str, sorted(arr))))
            continue

        movable = list(range(0, n - k)) + list(range(k, n))
        values = sorted(arr[i] for i in movable)
        ans = arr[:]
        for pos, value in zip(movable, values):
            ans[pos] = value
        out.append(" ".join(map(str, ans)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
