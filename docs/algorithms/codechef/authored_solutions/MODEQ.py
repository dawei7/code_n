import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m = data[idx], data[idx + 1]
        idx += 2
        cnt = [0] * (n + 1)
        ans = 0
        for value in range(1, n + 1):
            ans += cnt[m % value]
            start = m % value
            for residue in range(start, n + 1, value):
                cnt[residue] += 1
        out.append(str(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
