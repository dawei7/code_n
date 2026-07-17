def solve(nums: list[int]) -> int:
    right = [sum(nums[::2]), sum(nums[1::2])]
    left = [0, 0]
    answer = 0

    for index, value in enumerate(nums):
        right[index % 2] -= value
        if left[0] + right[1] == left[1] + right[0]:
            answer += 1
        left[index % 2] += value

    return answer
