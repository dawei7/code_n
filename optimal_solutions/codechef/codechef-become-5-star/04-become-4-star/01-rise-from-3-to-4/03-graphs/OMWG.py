import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    test_count = data[0]
    index = 1
    out = []
    for _ in range(test_count):
        n, m = (data[index], data[index + 1])
        index += 2
        out.append(str(n * (m - 1) + m * (n - 1)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
