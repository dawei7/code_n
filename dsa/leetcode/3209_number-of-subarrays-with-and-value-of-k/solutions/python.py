from collections import defaultdict

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the number of subarrays with bitwise AND equal to k.
    Uses the property that there are at most O(log(max_val)) distinct 
    bitwise AND values ending at any index.
    """
    total_count = 0
    # current_ands stores {and_value: frequency} for subarrays ending at the previous index
    current_ands = defaultdict(int)
    
    for x in nums:
        next_ands = defaultdict(int)
        # A subarray of length 1
        next_ands[x] += 1
        
        # Extend existing subarrays ending at the previous index
        for val, count in current_ands.items():
            next_ands[val & x] += count
            
        # Add the count of subarrays ending at this index that result in k
        total_count += next_ands.get(k, 0)
        current_ands = next_ands
        
    return total_count
