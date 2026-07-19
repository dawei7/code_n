from typing import List

def solve(word: str, m: int) -> List[int]:
    """
    Calculates the divisibility array of a string based on a divisor m.
    Uses modular arithmetic to maintain a running remainder.
    """
    n = len(word)
    divisibility_array = [0] * n
    current_remainder = 0
    
    for i in range(n):
        # Update the remainder: (previous_remainder * 10 + current_digit) % m
        current_remainder = (current_remainder * 10 + int(word[i])) % m
        
        # If the remainder is 0, the prefix is divisible by m
        if current_remainder == 0:
            divisibility_array[i] = 1
        else:
            divisibility_array[i] = 0
            
    return divisibility_array
