from typing import List

def solve(words: List[str]) -> int:
    n = len(words)
    masks = [0] * n
    lengths = [0] * n
    
    # Precompute bitmasks and lengths for each word
    for i, word in enumerate(words):
        lengths[i] = len(word)
        mask = 0
        for char in word:
            mask |= (1 << (ord(char) - ord('a')))
        masks[i] = mask
    
    max_product = 0
    
    # Compare every pair of words using bitwise AND
    for i in range(n):
        for j in range(i + 1, n):
            if (masks[i] & masks[j]) == 0:
                product = lengths[i] * lengths[j]
                if product > max_product:
                    max_product = product
                    
    return max_product
