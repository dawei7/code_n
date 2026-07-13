def solve(nums: list[int]) -> int:
    """
    Calculates the sum of imbalance numbers of all subarrays.
    An imbalance number is the count of elements x in a subarray such that
    x + 1 is not present in the subarray, excluding the minimum element.
    """
    n = len(nums)
    total_imbalance = 0
    
    for i in range(n):
        seen = set()
        current_imbalance = 0
        for j in range(i, n):
            x = nums[j]
            
            if x not in seen:
                # If x-1 and x+1 are both present, adding x reduces imbalance by 1
                # because x+1 is no longer "missing" its predecessor.
                if (x - 1) in seen and (x + 1) in seen:
                    current_imbalance -= 1
                # If neither x-1 nor x+1 are present, adding x increases imbalance by 1
                # (unless it's the new minimum, but the logic handles this via the set).
                elif (x - 1) not in seen and (x + 1) not in seen:
                    if seen: # Only increment if not the very first element
                        current_imbalance += 1
                
                seen.add(x)
            
            total_imbalance += current_imbalance
            
    return total_imbalance
