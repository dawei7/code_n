def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        x = int(data[i])
        binary_str = format(x, '032b')
        reversed_str = binary_str[::-1]
        results.append(str(int(reversed_str, 2)))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
