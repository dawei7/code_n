import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, x, y = data[:3]
    a = data[3:3 + n]
    b = data[3 + n:3 + 2 * n]
    jobs = sorted(((abs(ai - bi), ai, bi) for ai, bi in zip(a, b)), reverse=True)
    total = 0
    used_a = 0
    used_b = 0
    for _, ai, bi in jobs:
        if (ai >= bi and used_a < x) or used_b == y:
            total += ai
            used_a += 1
        else:
            total += bi
            used_b += 1
    print(total)


if __name__ == "__main__":
    main()
