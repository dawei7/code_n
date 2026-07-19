def solve(s: str) -> str:
    from collections import Counter
    
    # Count the frequency of each character
    counts = Counter(s)
    max_freq = max(counts.values())
    
    # Identify characters that appear with the maximum frequency
    # We need to keep track of their last occurrence index to maintain relative order
    last_indices = {}
    for i, char in enumerate(s):
        last_indices[char] = i
        
    # Filter characters that have the max frequency
    result_chars = []
    for char, count in counts.items():
        if count == max_freq:
            result_chars.append((last_indices[char], char))
            
    # Sort by the index of their last occurrence to get the correct order
    result_chars.sort()
    
    return "".join(char for index, char in result_chars)
