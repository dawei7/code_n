def first_occurrence(arr, n, target):
    left = -1
    right = n
    while right - left > 1:
        middle = (left + right) // 2
        if arr[middle] >= target:
            right = middle
        else:
            left = middle
    return right

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    print(n - first_occurrence(arr, n, 1))


if __name__ == "__main__":
    solve()
