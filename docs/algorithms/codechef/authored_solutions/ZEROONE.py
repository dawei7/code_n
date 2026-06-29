import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        c = data[idx:idx + n]
        idx += n
        zeros = sorted(c[0::2], reverse=True)
        ones = sorted(c[1::2])
        result = []
        zi = oi = 0
        zero_prefix = 0
        score = 0
        for pos in range(n):
            if pos % 2 == 0:
                value = zeros[zi]
                zi += 1
                zero_prefix += value
            else:
                value = ones[oi]
                oi += 1
                score += zero_prefix * value
            result.append(value)
        out.append(" ".join(map(str, result)))
        out.append(str(score))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
