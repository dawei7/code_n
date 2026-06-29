import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx:idx + n]
        idx += n
        even_values = sum(1 for value in values if value % 2 == 0)
        odd_values = n - even_values
        odd_positions = (n + 1) // 2
        even_positions = n // 2
        out.append(str(min(even_values, odd_positions) + min(odd_values, even_positions)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
