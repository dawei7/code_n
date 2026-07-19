from collections import defaultdict

def solve(nums: list[int]) -> int:
    n = len(nums)
    total_subarrays = n * (n + 1) // 2
    target = (total_subarrays + 1) // 2

    def count_subarrays_with_at_most_k_distinct(k: int) -> int:
        """Counts how many subarrays have at most k distinct elements."""
        count = 0
        left = 0
        freq = defaultdict(int)
        distinct = 0
        
        for right in range(n):
            if freq[nums[right]] == 0:
                distinct += 1
            freq[nums[right]] += 1
            
            while distinct > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct -= 1
                left += 1
            
            # All subarrays ending at 'right' starting from 'left' to 'right'
            # have at most k distinct elements.
            count += (right - left + 1)
        return count

    # Binary search for the smallest k such that count_subarrays(k) >= target
    low = 1
    high = len(set(nums))
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        if count_subarrays_with_at_most_k_distinct(mid) >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans
