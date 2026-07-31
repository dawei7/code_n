def solve(nums):
    answer = 0
    prefix_sum = 0
    for value in nums:
        prefix_sum += value
        answer |= value | prefix_sum
    return answer
