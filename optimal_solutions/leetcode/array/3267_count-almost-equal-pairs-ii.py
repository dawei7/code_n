from collections import defaultdict

def solve(nums: list[int]) -> int:
    # Normalize all numbers to the same length (max 7 digits)
    max_len = len(str(max(nums)))
    
    def get_variations(n_str):
        s = list(n_str.zfill(max_len))
        res = {tuple(s)}
        
        # 1 swap
        n = len(s)
        for i in range(n):
            for j in range(i + 1, n):
                s[i], s[j] = s[j], s[i]
                res.add(tuple(s))
                # 2 swaps: perform another swap on the result of the first
                for k in range(n):
                    for l in range(k + 1, n):
                        s[k], s[l] = s[l], s[k]
                        res.add(tuple(s))
                        s[k], s[l] = s[l], s[k] # backtrack
                s[i], s[j] = s[j], s[i] # backtrack
        return res

    count = 0
    freq = defaultdict(int)
    
    for x in nums:
        s_x = str(x).zfill(max_len)
        variations = get_variations(s_x)
        
        # For each variation, check how many times we've seen it before
        for var in variations:
            count += freq[var]
            
        # Add the original number to the frequency map
        freq[tuple(s_x)] += 1
        
    return count
