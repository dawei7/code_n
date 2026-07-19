def solve(nums: list[int], diff: int) -> int:
    """
    Calculates the number of arithmetic triplets in a strictly increasing array.
    Uses a set for O(1) average time complexity lookups.
    """
    num_set = set(nums)
    count = 0
    
    for x in nums:
        # Check if the preceding and succeeding elements of the triplet exist
        if (x - diff) in num_set and (x + diff) in num_set:
            count += 1
            
    return count
