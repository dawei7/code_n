import sys


def count_special_triplets(n: int) -> int:
    total = 0
    for c in range(1, n + 1):
        for b in range(c + c, n + 1, c):
            total += (n - c) // b + 1
    return total


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    out = []
    for i in range(1, t + 1):
        out.append(str(count_special_triplets(data[i])))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
