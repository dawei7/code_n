def solve(nums: list[int]) -> int:
    def contribution(as_maximum: bool) -> int:
        total = 0
        stack: list[int] = []

        for right in range(len(nums) + 1):
            while stack and (
                right == len(nums)
                or (
                    nums[stack[-1]] < nums[right]
                    if as_maximum
                    else nums[stack[-1]] > nums[right]
                )
            ):
                middle = stack.pop()
                left = stack[-1] if stack else -1
                total += nums[middle] * (middle - left) * (right - middle)
            stack.append(right)

        return total

    return contribution(True) - contribution(False)
