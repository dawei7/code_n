


def solve():
    n = int(input())

    pairs = []
    for _ in range(n):
        pair = tuple(map(int, input().split()))
        pairs.append(pair)

    left, right = map(int, input().split())

    # Output pairs whose sum and product are within [left, right]
    for a, b in pairs:
        if left <= a + b <= right and left <= a * b <= right:
            print(a, b)


if __name__ == "__main__":
    solve()
