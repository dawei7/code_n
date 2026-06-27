def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    
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
            
            def count_valid(s_range, e_range):
                # This is a geometric counting problem:
                # s in [l_bound, i], e in [i, r_bound], e - s + 1 <= k
                # Let x = i - s, y = e - i. 0 <= x <= i - l_bound, 0 <= y <= r_bound - i
                # x + y + 1 <= k  => x + y <= k - 1
                max_x = i - l_bound
                max_y = r_bound - i
                
                # Count pairs (x, y) with 0 <= x <= max_x, 0 <= y <= max_y, x + y <= k - 1
                # This is a standard trapezoidal/triangular sum
                count = 0
                limit = k - 1
                
                # Sum over x from 0 to min(max_x, limit)
                for x in range(min(max_x, limit) + 1):
                    count += min(max_y, limit - x) + 1
                return count

            total += nums[i] * count_valid(l_bound, r_bound)
        return total

    return get_contributions(True) + get_contributions(False)
