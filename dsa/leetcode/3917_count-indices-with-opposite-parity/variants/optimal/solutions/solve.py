def solve(nums: list[int]) -> list[int]:
    answer = [0] * len(nums)
    even_to_right = 0
    odd_to_right = 0

    for index in range(len(nums) - 1, -1, -1):
        if nums[index] % 2:
            answer[index] = even_to_right
            odd_to_right += 1
        else:
            answer[index] = odd_to_right
            even_to_right += 1

    return answer
