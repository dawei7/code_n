def solve(arr, target):
    def total_with_cap(cap):
        return sum(min(value, cap) for value in arr)

    left, right = 0, max(arr)
    while left < right:
        mid = (left + right) // 2
        if total_with_cap(mid) < target:
            left = mid + 1
        else:
            right = mid

    lower = left - 1
    if abs(total_with_cap(lower) - target) <= abs(total_with_cap(left) - target):
        return lower
    return left
