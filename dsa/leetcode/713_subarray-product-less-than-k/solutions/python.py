def solve(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0

    product = 1
    left = 0
    answer = 0

    for right, value in enumerate(nums):
        product *= value
        while product >= k:
            product //= nums[left]
            left += 1
        answer += right - left + 1

    return answer
