from collections import Counter

def solve(words: list[str]) -> int:
    # Count total frequency of each character
    total_counts = Counter()
    for word in words:
        for char in word:
            total_counts[char] += 1
            
    # Calculate total number of pairs available
    num_pairs = 0
    for char in total_counts:
        num_pairs += total_counts[char] // 2
        
    # Sort words by length to prioritize filling shorter palindromes first
    words.sort(key=len)
    
    ans = 0
    leftover_chars = 0
    
    for word in words:
        length = len(word)
        pairs_needed = length // 2
        
        # If we have enough pairs to satisfy the current word's structure
        if num_pairs >= pairs_needed:
            num_pairs -= pairs_needed
            # If length is odd, we need one extra character in the middle
            if length % 2 == 1:
                leftover_chars += 1
            ans += 1
        else:
            # Cannot form this palindrome
            # All characters in this word become "leftover"
            leftover_chars += length
            
    return ans
