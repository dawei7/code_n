def solve(nums: list[int]) -> int:
    nums.sort()
    n = len(nums)
    median = nums[n // 2]
    
    def is_palindrome(n: int) -> bool:
        s = str(n)
        return s == s[::-1]
    
    def get_candidates(val: int) -> list[int]:
        s = str(val)
        length = len(s)
        candidates = set()
        
        # Add edge cases: 10^(n-1) - 1 and 10^n + 1
        candidates.add(10**(length - 1) - 1)
        candidates.add(10**length + 1)
        
        # Generate palindromes by modifying the prefix
        prefix = int(s[:(length + 1) // 2])
        for i in [-1, 0, 1]:
            p = str(prefix + i)
            if length % 2 == 0:
                res = p + p[::-1]
            else:
                res = p + p[:-1][::-1]
            candidates.add(int(res))
        
        return [c for c in candidates if c > 0]

    candidates = get_candidates(median)
    
    min_cost = float('inf')
    for cand in candidates:
        current_cost = sum(abs(x - cand) for x in nums)
        if current_cost < min_cost:
            min_cost = current_cost
            
    return int(min_cost)
