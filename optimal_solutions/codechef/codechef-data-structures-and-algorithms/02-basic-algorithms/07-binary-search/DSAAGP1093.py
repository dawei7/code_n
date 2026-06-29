


def solve():
    def binary_search(arr, n, k):
        left, right = 0, n - 1
        while left <= right:
            middle = (left + right) // 2
            if arr[middle] == k:
                return middle
            elif arr[middle] > k:
                right = middle - 1
            else:
                left = middle + 1
        return -1  # k not found

    if __name__ == "__main__":
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(binary_search(arr, n, k))


if __name__ == "__main__":
    solve()
