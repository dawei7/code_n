def check(arr, d, n, c):
    cows = c - 1
    prev = arr[0]
    for i in range(1, n):
        if arr[i] - prev >= d:
            cows -= 1
            prev = arr[i]
        if cows == 0:
            break
    return cows <= 0

def solve():
    n, c = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    first, last = (0, int(1000000000.0) + 1)
    while last - first > 1:
        mid = (first + last) // 2
        if check(arr, mid, n, c):
            first = mid
        else:
            last = mid
    print(first)


if __name__ == "__main__":
    solve()
