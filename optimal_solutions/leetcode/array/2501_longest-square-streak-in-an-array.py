from typing import List

def solve(nums: List[int]) -> int:
    num_set = set(nums)
    max_streak = 0
    
    # We only care about numbers that could be the start of a streak.
    # A number 'x' is the start of a streak if 'sqrt(x)' is not in the set.
    # However, simply iterating through all numbers and checking is efficient enough
    # because the sequence grows quadratically and hits the limit (10^5) very quickly.
    
    for num in nums:
        current_streak = 0
        curr = num
        
        # Check if this number is the start of a potential streak
        # to avoid redundant calculations.
        root = int(curr**0.5)
        if root * root == curr and root in num_set:
            continue
            
        # Build the streak
        temp = curr
        while temp in num_set:
            current_streak += 1
            temp = temp * temp
            # The maximum value is 10^5, so temp will exceed this quickly
            if temp > 100000:
                break
        
        if current_streak >= 2:
            max_streak = max(max_streak, current_streak)
            
    return max_streak if max_streak >= 2 else -1
