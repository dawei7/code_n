import functools

def solve(nums: list[int]) -> int:
    n = len(nums)
    
    @functools.lru_cache(None)
    def dp(i: int, last_idx: int) -> int:
        # i is the index of the first element in the current pair
        # last_idx is the index of the element left over from the previous operation
        
        # If we have reached the end of the array
        if i >= n:
            return nums[last_idx]
        
        # If we are at the second to last element
        if i == n - 1:
            return max(nums[i], nums[last_idx])
        
        # Option 1: Pair current element with the leftover element
        res1 = max(nums[i], nums[last_idx]) + dp(i + 2, i + 1)
        
        # Option 2: Pair current element with the next element
        res2 = max(nums[i], nums[i + 1]) + dp(i + 2, last_idx)
        
        # Option 3: Pair the two remaining elements (last_idx and next)
        res3 = max(nums[last_idx], nums[i + 1]) + dp(i + 2, i)
        
        return min(res1, res2, res3)

    # Initial call: start at index 1, with index 0 as the "leftover"
    return dp(1, 0)
