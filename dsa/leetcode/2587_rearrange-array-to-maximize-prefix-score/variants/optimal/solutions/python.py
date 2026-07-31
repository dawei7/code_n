def solve(nums: list[int]) -> int:
    nums.sort(reverse=True)
    prefix_sum = 0
    score = 0

    for value in nums:
        prefix_sum += value
        if prefix_sum <= 0:
            break
        score += 1

    return score
