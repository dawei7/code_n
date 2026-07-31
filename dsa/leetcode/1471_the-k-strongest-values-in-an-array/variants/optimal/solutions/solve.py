def solve(arr, k):
    arr.sort()
    median = arr[(len(arr) - 1) // 2]
    strongest = []
    left = 0
    right = len(arr) - 1

    while len(strongest) < k:
        left_distance = abs(arr[left] - median)
        right_distance = abs(arr[right] - median)

        if right_distance >= left_distance:
            strongest.append(arr[right])
            right -= 1
        else:
            strongest.append(arr[left])
            left += 1

    return strongest
