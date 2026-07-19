from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Calculates the score of all prefixes of an array.
    The score of a prefix is the sum of (nums[i] + max(nums[0...i])) for all i.
    """
    n = len(nums)
    scores = [0] * n
    
    current_max = 0
    running_score = 0
    
    for i in range(n):
        # Update the maximum value encountered so far
        if nums[i] > current_max:
            current_max = nums[i]
        
        # The converted value is nums[i] + current_max
        # The prefix score is the cumulative sum of these converted values
        running_score += (nums[i] + current_max)
        scores[i] = running_score
        
    return scores
