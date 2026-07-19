from typing import List

def solve(arr1: List[int], arr2: List[int]) -> int:
    """
    Finds the length of the longest common prefix between any two numbers
    from arr1 and arr2 using a hash set for prefix storage.
    """
    prefix_set = set()
    
    # Store all possible prefixes of numbers in arr1
    for num in arr1:
        s = str(num)
        current_prefix = ""
        for char in s:
            current_prefix += char
            prefix_set.add(current_prefix)
            
    max_len = 0
    
    # Check prefixes of numbers in arr2 against the set
    for num in arr2:
        s = str(num)
        current_prefix = ""
        for char in s:
            current_prefix += char
            if current_prefix in prefix_set:
                max_len = max(max_len, len(current_prefix))
            else:
                # If the current prefix isn't in the set, longer ones won't be either
                break
                
    return max_len
