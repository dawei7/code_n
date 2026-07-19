from collections import defaultdict

def solve(coordinates: list[list[int]], k: int) -> int:
    """
    Counts pairs (i, j) with i < j such that (x1 ^ x2) + (y1 ^ y2) == k.
    """
    count = 0
    freq = defaultdict(int)
    
    for x, y in coordinates:
        # We need (x ^ x2) + (y ^ y2) == k
        # Let x ^ x2 = i, then y ^ y2 = k - i
        # So x2 = x ^ i, y2 = y ^ (k - i)
        for i in range(k + 1):
            target_x = x ^ i
            target_y = y ^ (k - i)
            
            if (target_x, target_y) in freq:
                count += freq[(target_x, target_y)]
        
        freq[(x, y)] += 1
        
    return count
