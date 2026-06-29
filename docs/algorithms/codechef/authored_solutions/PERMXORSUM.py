import sys


def best_sum(n: int) -> int:
    if n <= 1:
        return 0
    mask = (1 << n.bit_length()) - 1
    start = max(1, mask - n)
    end = min(n, mask - 1)
    paired = max(0, end - start + 1)
    return paired * mask + best_sum(start - 1)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        out.append(str(best_sum(n)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
