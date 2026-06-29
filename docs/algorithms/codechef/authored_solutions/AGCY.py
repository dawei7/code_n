import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, q = data[idx:idx + 2]
        idx += 2
        c0 = [0] * (n + 3)
        c1 = [0] * (n + 3)
        for _ in range(q):
            left, right = data[idx:idx + 2]
            idx += 2
            c1[left] += 1
            c1[right + 1] -= 1
            c0[left] += 1 - left
            c0[right + 1] -= 1 - left
        cur1 = cur0 = 0
        ans = []
        for pos in range(1, n + 1):
            cur1 += c1[pos]
            cur0 += c0[pos]
            ans.append(str(cur1 * pos + cur0))
        out.append(" ".join(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
