import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    INF = 10**18
    for _ in range(t):
        n, m = data[idx], data[idx + 1]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        dests = data[idx:idx + m]
        idx += m

        left_train = [INF] * n
        last = -INF
        for i, value in enumerate(arr):
            if value == 1:
                last = i
            if last > -INF:
                left_train[i] = i - last

        right_train = [INF] * n
        last = INF
        for i in range(n - 1, -1, -1):
            if arr[i] == 2:
                last = i
            if last < INF:
                right_train[i] = last - i

        ans = []
        for b in dests:
            pos = b - 1
            if pos == 0:
                ans.append("0")
            else:
                best = min(left_train[pos], right_train[pos])
                ans.append(str(best if best < INF else -1))
        out.append(" ".join(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
