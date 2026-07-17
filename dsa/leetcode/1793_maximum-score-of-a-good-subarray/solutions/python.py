def solve(nums: list[int], k: int) -> int:
    left = right = k
    minimum = nums[k]
    best = minimum

    while left > 0 or right + 1 < len(nums):
        if left == 0:
            right += 1
        elif right + 1 == len(nums):
            left -= 1
        elif nums[left - 1] < nums[right + 1]:
            right += 1
        else:
            left -= 1

        minimum = min(minimum, nums[left], nums[right])
        best = max(best, minimum * (right - left + 1))

    return best
