def solve(nums: list[int]) -> list[int]:
    answer = [0] * len(nums)
    stack: list[int] = []

    for right in range(len(nums) + 1):
        current = -1 if right == len(nums) else nums[right]

        while stack and nums[stack[-1]] >= current:
            index = stack.pop()
            left = stack[-1] if stack else -1
            width = right - left - 1
            answer[width - 1] = max(
                answer[width - 1],
                nums[index],
            )

        if right < len(nums):
            stack.append(right)

    for index in range(len(nums) - 2, -1, -1):
        answer[index] = max(answer[index], answer[index + 1])

    return answer
