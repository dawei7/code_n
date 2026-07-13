def solve(nums: list[int], k: int) -> int:
    n = len(nums)

    def bounded_pair_count(max_left: int, max_right: int, limit: int) -> int:
        x_max = min(max_left, limit)
        full_until = min(x_max, limit - max_right)
        count = 0
        if full_until >= 0:
            count += (full_until + 1) * (max_right + 1)
            start = full_until + 1
        else:
            start = 0
        if start <= x_max:
            terms = x_max - start + 1
            first = limit - start + 1
            last = limit - x_max + 1
            count += terms * (first + last) // 2
        return count

    def get_contributions(is_max: bool) -> int:
        # Find boundaries where nums[i] is the max/min
        left = [-1] * n
        right = [n] * n
        stack = []

        for i in range(n):
            while stack and (nums[stack[-1]] <= nums[i] if is_max else nums[stack[-1]] >= nums[i]):
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and (nums[stack[-1]] < nums[i] if is_max else nums[stack[-1]] > nums[i]):
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        total = 0
        for i in range(n):
            l_bound = left[i] + 1
            r_bound = right[i] - 1

            # Subarrays containing i with length <= k
            # Start index s in [l_bound, i], end index e in [i, r_bound]
            # Length = e - s + 1 <= k
            # We need to count pairs (s, e) such that l_bound <= s <= i <= e <= r_bound and e - s + 1 <= k

            total += nums[i] * bounded_pair_count(i - l_bound, r_bound - i, k - 1)
        return total

    return get_contributions(True) + get_contributions(False)
