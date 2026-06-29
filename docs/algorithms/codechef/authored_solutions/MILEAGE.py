import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        _, x, y, a, b = data[idx:idx + 5]
        idx += 5
        petrol = x * b
        diesel = y * a
        if petrol < diesel:
            out.append("PETROL")
        elif petrol > diesel:
            out.append("DIESEL")
        else:
            out.append("ANY")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
