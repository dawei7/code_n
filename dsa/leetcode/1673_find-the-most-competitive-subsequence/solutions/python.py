def solve(nums: list[int], k: int) -> list[int]:
    stack: list[int] = []
    removals = len(nums) - k

    for value in nums:
        while removals and stack and stack[-1] > value:
            stack.pop()
            removals -= 1
        if len(stack) < k:
            stack.append(value)
        else:
            removals -= 1

    return stack
