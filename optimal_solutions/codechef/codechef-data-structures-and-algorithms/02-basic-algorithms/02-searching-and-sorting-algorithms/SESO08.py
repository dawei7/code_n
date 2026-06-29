


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    min_diff = float('inf')
    result = float('inf')

    for num in arr:
        diff = abs(num - k)
        if diff < min_diff or (diff == min_diff and num < result):
            min_diff = diff
            result = num

    print(result)


if __name__ == "__main__":
    solve()
