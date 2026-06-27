def solve(lcp: list[list[int]]) -> str:
    n = len(lcp)
    s = [0] * n
    char_code = 0
    
    # Assign characters greedily
    for i in range(n):
        if s[i] == 0:
            if char_code >= 26:
                return ""
            char_code += 1
            for j in range(i, n):
                if lcp[i][j] > 0:
                    s[j] = char_code
        
    # Verify the LCP matrix constraints
    # 1. Check diagonal and symmetry
    for i in range(n):
        if lcp[i][i] != n - i:
            return ""
        for j in range(i + 1, n):
            if lcp[i][j] != lcp[j][i]:
                return ""
                
    # 2. Check LCP values against the generated string
    res = [0] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]:
                val = 1 + (res[i + 1][j + 1] if (i + 1 < n and j + 1 < n) else 0)
                if lcp[i][j] != val:
                    return ""
            else:
                if lcp[i][j] != 0:
                    return ""
        # We need a DP table to verify efficiently
        if i == n - 1:
            res = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]:
                res[i][j] = 1 + res[i + 1][j + 1]
            else:
                res[i][j] = 0
            if res[i][j] != lcp[i][j]:
                return ""
                
    return "".join(chr(ord('a') + x - 1) for x in s)
