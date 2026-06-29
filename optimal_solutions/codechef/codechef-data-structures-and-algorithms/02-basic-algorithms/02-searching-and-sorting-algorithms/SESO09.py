def solve():
    n, k = map(int, input().split())
    pairs = []
    for _ in range(n):
        first, second = map(int, input().split())
        pairs.append((first, second))
    for first, second in pairs:
        if (first + second) % k == 0:
            print(f'({first}, {second})')


if __name__ == "__main__":
    solve()
