def solve(arr, k):
    left = 0
    right = len(arr)

    while left < right:
        middle = (left + right) // 2
        missing = arr[middle] - middle - 1
        if missing < k:
            left = middle + 1
        else:
            right = middle

    return left + k
