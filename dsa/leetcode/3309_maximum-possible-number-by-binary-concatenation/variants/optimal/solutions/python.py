from itertools import permutations

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum possible number by concatenating the binary 
    representations of the three integers in nums in any order.
    """
    max_val = 0
    
    # Generate all permutations of the input list
    for p in permutations(nums):
        # Convert each number to binary string, removing the '0b' prefix
        binary_str = "".join(bin(x)[2:] for x in p)
        
        # Convert the concatenated binary string back to an integer
        current_val = int(binary_str, 2)
        
        # Update the maximum value found so far
        if current_val > max_val:
            max_val = current_val
            
    return max_val
