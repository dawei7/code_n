def solve(nums: list[int]) -> int:
    answer = None
    for index, value in enumerate(nums):
        if value != index:
            answer = value if answer is None else answer & value
    return 0 if answer is None else answer
