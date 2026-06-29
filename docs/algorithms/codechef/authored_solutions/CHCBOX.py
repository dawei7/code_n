import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        w = list(map(int, data[idx:idx + n]))
        idx += n

        half = n // 2
        mx = max(w)
        diff = [0] * (n + 1)

        for pos, value in enumerate(w):
            if value != mx:
                continue
            start = (-pos) % n
            end = (half - 1 - pos) % n
            if start <= end:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] += 1
                diff[n] -= 1
                diff[0] += 1
                diff[end + 1] -= 1

        cur = 0
        good = 0
        for k in range(n):
            cur += diff[k]
            if cur == 0:
                good += 1
        out.append(str(good))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
