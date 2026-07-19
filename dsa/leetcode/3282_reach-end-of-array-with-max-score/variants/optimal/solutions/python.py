def solve(nums: list[int]) -> int:
    """
    Calculates the maximum score to reach the end of the array.
    We iterate through the array and keep track of the maximum value seen so far.
    Every step, we add the current maximum value to our total score, 
    effectively simulating jumps from the best previous position.
    """
    total_score = 0
    current_max = 0
    
    # We iterate up to the second to last element because 
    # we must land on the last index.
    for i in range(len(nums) - 1):
        current_max = max(current_max, nums[i])
        total_score += current_max
        
    return total_score
