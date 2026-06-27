def solve(s: str, queries: list[list[int]]) -> list[bool]:
    n = len(s)
    half = n // 2
    s1 = s[:half]
    s2 = s[half:][::-1]
    
    # Precompute prefix sums for character counts in both halves
    def get_prefix_counts(t):
        res = [[0] * 26 for _ in range(len(t) + 1)]
        for i, char in enumerate(t):
            for j in range(26):
                res[i + 1][j] = res[i][j]
            res[i + 1][ord(char) - ord('a')] += 1
        return res

    pref1 = get_prefix_counts(s1)
    pref2 = get_prefix_counts(s2)

    def get_count(pref, l, r):
        return [pref[r + 1][i] - pref[l][i] for i in range(26)]

    results = []
    for a, b, c, d in queries:
        # Map indices to the reversed second half
        c_new = n - 1 - d
        d_new = n - 1 - c
        
        # Check if the parts outside the modified ranges match
        # Range 1: [0, min(a, c_new) - 1]
        # Range 2: [max(b, d_new) + 1, half - 1]
        if (a > 0 and pref1[a] != pref2[a]) or (d_new < half - 1 and pref1[half] - pref1[d_new + 1] != pref2[half] - pref2[d_new + 1]):
            results.append(False)
            continue
            
        # Check if the modified ranges can be rearranged to match
        if a <= c_new:
            # Range [a, b] covers [c_new, d_new] or vice versa
            # Check if remaining parts match
            if b < d_new:
                results.append(False)
                continue
            count1 = get_count(pref1, a, b)
            count2 = get_count(pref2, a, b)
            # The modified range must contain the other range
            # Check if the difference is valid
            diff = [count1[i] - count2[i] for i in range(26)]
            if any(x < 0 for x in diff):
                results.append(False)
            else:
                results.append(True)
        else:
            # c_new < a
            if d_new < b:
                results.append(False)
                continue
            count1 = get_count(pref1, c_new, d_new)
            count2 = get_count(pref2, c_new, d_new)
            diff = [count2[i] - count1[i] for i in range(26)]
            if any(x < 0 for x in diff):
                results.append(False)
            else:
                results.append(True)
                
    return results
