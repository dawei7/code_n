from typing import List

def solve(strs: List[str]) -> int:
    """
    Calculates the maximum value of strings in an array.
    A string's value is its integer value if it is numeric, 
    otherwise it is its length.
    """
    max_val = 0
    
    for s in strs:
        # Check if the string consists only of digits
        if s.isdigit():
            current_val = int(s)
        else:
            current_val = len(s)
            
        if current_val > max_val:
            max_val = current_val
            
    return max_val
