def solve(word: str, forbidden: list[str]) -> int:
    forbidden_set = set(forbidden)
    max_len = 0
    left = 0
    n = len(word)
    
    # The problem constraints state forbidden strings have length at most 10.
    # We only need to check substrings ending at 'right' with length up to 10.
    for right in range(n):
        # Check all possible forbidden substrings ending at 'right'
        # A forbidden string can have a max length of 10.
        for length in range(1, 11):
            if right - length + 1 < left:
                break
            
            sub = word[right - length + 1 : right + 1]
            if sub in forbidden_set:
                # If found, move left pointer to just after the start of this forbidden string
                left = right - length + 2
                break
        
        max_len = max(max_len, right - left + 1)
        
    return max_len
