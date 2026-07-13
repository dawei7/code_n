def solve(nums, threshold):
    left, right = 1, max(nums)
    while left < right:
        mid = (left + right) // 2
        total = sum((value + mid - 1) // mid for value in nums)
        if total <= threshold:
            right = mid
        else:
            left = mid + 1
    return left
