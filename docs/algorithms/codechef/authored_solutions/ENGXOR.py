import sys


def parity(value: int) -> int:
    return value.bit_count() & 1


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, q = data[idx], data[idx + 1]
        idx += 2
        counts = [0, 0]
        for value in data[idx:idx + n]:
            counts[parity(value)] += 1
        idx += n
        for value in data[idx:idx + q]:
            z = parity(value)
            out.append(f"{counts[z]} {counts[z ^ 1]}")
        idx += q
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
