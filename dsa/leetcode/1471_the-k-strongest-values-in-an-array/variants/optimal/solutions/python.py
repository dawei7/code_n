def solve(arr, k):
    ordered = sorted(arr)
    median = ordered[(len(ordered) - 1) // 2]
    strongest = []
    left = 0
    right = len(ordered) - 1

    while len(strongest) < k:
        left_distance = abs(ordered[left] - median)
        right_distance = abs(ordered[right] - median)

        if right_distance >= left_distance:
            strongest.append(ordered[right])
            right -= 1
        else:
            strongest.append(ordered[left])
            left += 1

    return strongest
