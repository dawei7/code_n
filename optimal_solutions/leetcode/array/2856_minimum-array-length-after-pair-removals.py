from collections import Counter

def solve(nums: list[int]) -> int:
    """
    The optimal strategy is to identify the most frequent element.
    Let 'max_freq' be the frequency of the most common element and 'n' be the total length.
    If max_freq > n / 2, the minimum remaining length is (max_freq - (n - max_freq)) = 2 * max_freq - n.
    Otherwise, the minimum length is n % 2.
    """
    n = len(nums)
    if n == 0:
        return 0
    
    counts = Counter(nums)
    max_freq = max(counts.values())
    
    if max_freq > n // 2:
        return 2 * max_freq - n
    else:
        return n % 2
