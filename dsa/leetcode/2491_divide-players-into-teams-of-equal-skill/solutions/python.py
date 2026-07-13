from typing import List

def solve(skill: List[int]) -> int:
    n = len(skill)
    skill.sort()
    
    # The target sum for every pair must be the sum of the smallest and largest
    target_sum = skill[0] + skill[-1]
    total_chemistry = 0
    
    left = 0
    right = n - 1
    
    while left < right:
        current_sum = skill[left] + skill[right]
        
        # If any pair does not match the target sum, partition is impossible
        if current_sum != target_sum:
            return -1
        
        # Add the product of the current pair to the total chemistry
        total_chemistry += (skill[left] * skill[right])
        
        left += 1
        right -= 1
        
    return total_chemistry
