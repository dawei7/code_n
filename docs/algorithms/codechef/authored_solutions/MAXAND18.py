import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        k = data[idx + 1]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        scores = []
        for bit in range(30):
            contribution = sum((value >> bit) & 1 for value in arr) * (1 << bit)
            scores.append((-contribution, bit))
        scores.sort()
        ans = 0
        for _, bit in scores[:k]:
            ans |= 1 << bit
        out.append(str(ans))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
