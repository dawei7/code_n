def solve(s: str, distance: list[int]) -> bool:
    # Store the first occurrence index of each character
    first_occurrence = {}
    
    for current_index, char in enumerate(s):
        char_code = ord(char) - ord('a')
        
        if char in first_occurrence:
            # Calculate distance: number of characters between the two occurrences
            # Distance = (current_index - first_index - 1)
            prev_index = first_occurrence[char]
            actual_distance = current_index - prev_index - 1
            
            if actual_distance != distance[char_code]:
                return False
        else:
            # Record the first time we see the character
            first_occurrence[char] = current_index
            
    return True
