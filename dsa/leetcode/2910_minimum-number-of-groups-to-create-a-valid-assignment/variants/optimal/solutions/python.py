from collections import Counter
import math

def solve(nums: list[int]) -> int:
    counts = Counter(nums)
    freqs = list(counts.values())
    min_f = min(freqs)
    
    def get_groups(f, k):
        # We want to represent f = a*k + b*(k+1)
        # This is equivalent to f = (a+b)*k + b
        # where 0 <= b <= a+b
        # Let n = a+b (total groups). Then f = n*k + b, where 0 <= b <= n
        # This implies n*k <= f <= n*(k+1)
        # n >= f / (k+1) and n <= f / k
        # So we need to find if there exists an integer n in [ceil(f/(k+1)), floor(f/k)]
        
        n_min = math.ceil(f / (k + 1))
        n_max = f // k
        
        if n_min <= n_max:
            return n_min
        return float('inf')

    # Try possible group sizes k starting from min_f down to 1
    for k in range(min_f, 0, -1):
        total_groups = 0
        possible = True
        for f in freqs:
            groups = get_groups(f, k)
            if groups == float('inf'):
                possible = False
                break
            total_groups += groups
        
        if possible:
            return total_groups
            
    return -1
