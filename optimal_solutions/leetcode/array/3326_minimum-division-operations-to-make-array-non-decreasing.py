def solve(nums: list[int]) -> int:
    MAX_VAL = 1000000
    min_prime = list(range(MAX_VAL + 1))
    
    # Precompute smallest prime factor using Sieve
    for i in range(2, int(MAX_VAL**0.5) + 1):
        if min_prime[i] == i:
            for j in range(i * i, MAX_VAL + 1, i):
                if min_prime[j] == j:
                    min_prime[j] = i
                    
    def get_smallest_proper_divisor(n: int) -> int:
        if n < 4:
            return n
        p = min_prime[n]
        return n // p if p != n else n

    count = 0
    n = len(nums)
    
    # Traverse backwards to ensure non-decreasing property greedily
    for i in range(n - 2, -1, -1):
        if nums[i] > nums[i + 1]:
            nums[i] = get_smallest_proper_divisor(nums[i])
            count += 1
            if nums[i] > nums[i + 1]:
                return -1
                
    return count
