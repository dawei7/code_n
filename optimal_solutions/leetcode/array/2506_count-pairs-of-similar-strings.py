from collections import Counter

def solve(words: list[str]) -> int:
    """
    Counts pairs of similar strings by mapping each string to a bitmask
    representing the set of unique characters present in the string.
    """
    # Map each word to a bitmask where the i-th bit is 1 if the i-th 
    # letter of the alphabet is present.
    masks = []
    for word in words:
        mask = 0
        for char in word:
            mask |= (1 << (ord(char) - ord('a')))
        masks.append(mask)
    
    # Count occurrences of each mask
    counts = Counter(masks)
    
    # For a mask that appears 'n' times, the number of pairs is n * (n - 1) / 2
    total_pairs = 0
    for count in counts.values():
        if count > 1:
            total_pairs += (count * (count - 1)) // 2
            
    return total_pairs
