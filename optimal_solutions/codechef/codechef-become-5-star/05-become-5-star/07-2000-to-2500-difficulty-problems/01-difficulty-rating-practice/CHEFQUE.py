import sys
MASK = (1 << 32) - 1

def solve() -> None:
    q, s, a, b = map(int, sys.stdin.buffer.read().split())
    values: set[int] = set()
    total = 0
    for _ in range(q):
        value = s >> 1
        if s & 1:
            if value not in values:
                values.add(value)
                total += value
        elif value in values:
            values.remove(value)
            total -= value
        s = a * s + b & MASK
    print(total)


if __name__ == "__main__":
    solve()
