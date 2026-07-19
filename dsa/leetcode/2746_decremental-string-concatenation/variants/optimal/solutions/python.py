from typing import List

def solve(words: List[str]) -> int:
    if not words:
        return 0
    
    # dp[first][last] stores the minimum length of a string starting with 'first' and ending with 'last'
    # We map 'a'-'z' to 0-25
    INF = float('inf')
    dp = [[INF] * 26 for _ in range(26)]
    
    first_char = ord(words[0][0]) - 97
    last_char = ord(words[0][-1]) - 97
    dp[first_char][last_char] = len(words[0])
    
    for i in range(1, len(words)):
        word = words[i]
        L = len(word)
        f = ord(word[0]) - 97
        l = ord(word[-1]) - 97
        
        next_dp = [[INF] * 26 for _ in range(26)]
        
        for first in range(26):
            for last in range(26):
                val = dp[first][last]
                if val == INF:
                    continue
                
                # Option 1: Append word to the end
                # New string starts with 'first' and ends with 'l'
                cost1 = val + L - (1 if last == f else 0)
                if cost1 < next_dp[first][l]:
                    next_dp[first][l] = cost1
                
                # Option 2: Prepend word to the beginning
                # New string starts with 'f' and ends with 'last'
                cost2 = val + L - (1 if l == first else 0)
                if cost2 < next_dp[f][last]:
                    next_dp[f][last] = cost2
                    
        dp = next_dp
        
    ans = INF
    for first in range(26):
        for last in range(26):
            if dp[first][last] < ans:
                ans = dp[first][last]
                
    return ans
