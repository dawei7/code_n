import math
import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        if n == 2:
            out.append("NO")
            continue

        out.append("YES")
        if n == 1:
            out.append("1")
            continue

        blocks = math.isqrt(n - 1) + 1
        sizes = [1] * blocks
        remaining = n - blocks
        for i in range(blocks):
            add = min(remaining, blocks - 1)
            sizes[i] += add
            remaining -= add
            if remaining == 0:
                break

        perm = []
        cur = 1
        for size in sizes:
            perm.extend(range(cur + size - 1, cur - 1, -1))
            cur += size
        out.append(" ".join(map(str, perm)))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
