"""Two-pass circular monotonic stack for LeetCode 503."""


def solve(nums: list[int]) -> list[int]:
    size = len(nums)
    answer = [-1] * size
    stack: list[int] = []

    for scan_index in range(2 * size):
        index = scan_index % size
        while stack and nums[stack[-1]] < nums[index]:
            answer[stack.pop()] = nums[index]
        if scan_index < size:
            stack.append(index)
    return answer
