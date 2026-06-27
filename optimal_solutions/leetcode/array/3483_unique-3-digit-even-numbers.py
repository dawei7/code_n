from collections import Counter

def solve(digits: list[int]) -> list[int]:
    # Count the frequency of each available digit
    counts = Counter(digits)
    result = []
    
    # Iterate through all possible 3-digit even numbers
    # A 3-digit number ranges from 100 to 999.
    for num in range(100, 1000, 2):
        # Extract digits of the current number
        d1 = num // 100
        d2 = (num // 10) % 10
        d3 = num % 10
        
        # Check if we have enough of each digit to form this number
        temp_counts = Counter([d1, d2, d3])
        
        possible = True
        for digit, freq in temp_counts.items():
            if counts[digit] < freq:
                possible = False
                break
        
        if possible:
            result.append(num)
            
    return result
