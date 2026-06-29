import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        if n < 3:
            out.append("-1")
        elif n % 2 == 1:
            x = (n - 1) // 2
            out.append(f"1 1 {x}")
        elif n & (n - 1) == 0:
            out.append("-1")
        else:
            lowbit = n & -n
            out.append(f"1 {lowbit} {(n - lowbit) // 2}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
