import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = sorted(data[idx:idx + 2 * n])
        idx += 2 * n
        out.append(str(arr[n + n // 2]))
        perm = []
        for i in range(n):
            perm.append(arr[i])
            perm.append(arr[n + i])
        out.append(" ".join(map(str, perm)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
