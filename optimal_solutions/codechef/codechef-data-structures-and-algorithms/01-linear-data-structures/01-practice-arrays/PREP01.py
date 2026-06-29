def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    output = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        row = []
        current = 1
        for k in range(n):
            row.append(str(current))
            if k < n - 1:
                current = current * (n - 1 - k) // (k + 1)
        output.append(' '.join(row))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()
