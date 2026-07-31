def solve(nums: list[int]) -> list[int]:
    even_values = sorted(nums[::2])
    odd_values = sorted(nums[1::2], reverse=True)
    answer = nums[:]
    answer[::2] = even_values
    answer[1::2] = odd_values
    return answer
