import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, y = data[idx], data[idx + 1]
        idx += 2
        total = x + y
        n = math.isqrt(total)
        if n * n != total:
            out.append("NO")
            continue

        if n == 1:
            if x == 1:
                out.append("YES\n1")
            else:
                out.append("NO")
            continue

        even_level = 1
        odd_level = n - 1
        while odd_level >= 1 and even_level * odd_level * 2 != y:
            even_level += 1
            odd_level -= 1

        if odd_level < 1:
            out.append("NO")
            continue

        lines = ["YES", str(n)]
        for i in range(1, odd_level + 1):
            lines.append(f"1 {i + 1}")
        for i in range(1, even_level):
            lines.append(f"2 {odd_level + i + 1}")
        out.append("\n".join(lines))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
