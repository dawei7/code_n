def solve(nums: list[int], k: int) -> int:
    n = len(nums)

    def bounded_pair_count(left: int, right: int) -> int:
        left = min(left, k - 1)
        full_until = min(left, k - 1 - right)
        count = 0
        if full_until >= 0:
            count = (full_until + 1) * (right + 1)
        start = max(0, full_until + 1)
        if start <= left:
            terms = left - start + 1
            count += terms * ((k - start) + (k - left)) // 2
        return count

    def contribution(maximum: bool) -> int:
        previous = [-1] * n
        following = [n] * n
        stack: list[int] = []
        for i, value in enumerate(nums):
            while stack and (nums[stack[-1]] <= value if maximum else nums[stack[-1]] >= value):
                stack.pop()
            if stack:
                previous[i] = stack[-1]
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and (nums[stack[-1]] < nums[i] if maximum else nums[stack[-1]] > nums[i]):
                stack.pop()
            if stack:
                following[i] = stack[-1]
            stack.append(i)

        total = 0
        for i, value in enumerate(nums):
            total += value * bounded_pair_count(
                i - previous[i] - 1,
                following[i] - i - 1,
            )
        return total

    return contribution(True) + contribution(False)
