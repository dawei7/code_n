def solve(words: list[str], groups: list[int]) -> list[str]:
    n = len(words)
    dp = [1] * n
    parent = [-1] * n
    
    def is_valid(s1, s2):
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    for i in range(n):
        for j in range(i):
            if groups[i] != groups[j] and is_valid(words[i], words[j]):
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
    
    max_len = 0
    curr = -1
    for i in range(n):
        if dp[i] > max_len:
            max_len = dp[i]
            curr = i
            
    result = []
    while curr != -1:
        result.append(words[curr])
        curr = parent[curr]
        
    return result[::-1]
