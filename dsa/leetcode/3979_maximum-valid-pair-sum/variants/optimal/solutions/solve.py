def solve(nums: list[int], k: int) -> int:
    best_left = 0
    answer = 0

    for right in range(k, len(nums)):
        best_left = max(best_left, nums[right - k])
        answer = max(answer, best_left + nums[right])

    return answer
