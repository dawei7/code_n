def solve(nums: list[int]) -> int:
    def check(diff):
        n = len(nums)
        # Identify segments of -1s
        # A segment is bounded by fixed values: [left_val, -1, ..., -1, right_val]
        # If -1s are at the start or end, they are effectively bounded by one value.
        
        min_val, max_val = 1, 10**9
        
        # Collect segments
        segments = []
        i = 0
        while i < n:
            if nums[i] == -1:
                start = i
                while i < n and nums[i] == -1:
                    i += 1
                end = i - 1
                left = nums[start - 1] if start > 0 else None
                right = nums[end + 1] if end < n - 1 else None
                segments.append((left, right, end - start + 1))
            else:
                i += 1
        
        # Check fixed adjacent differences first
        for i in range(n - 1):
            if nums[i] != -1 and nums[i+1] != -1:
                if abs(nums[i] - nums[i+1]) > diff:
                    return False
        
        # Check if segments can be filled
        for left, right, length in segments:
            if left is not None and right is not None:
                if abs(left - right) > diff * (length + 1):
                    return False
            elif left is not None or right is not None:
                # Only one side bounded, always possible
                pass
            else:
                # All -1s, always possible
                pass
        return True

    low = 0
    high = 10**9
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
