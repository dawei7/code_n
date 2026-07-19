def solve(words: list[str], queries: list[list[int]]) -> list[int]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    n = len(words)
    
    # prefix_sum[i] stores the count of valid strings in words[0...i-1]
    prefix_sum = [0] * (n + 1)
    
    for i in range(n):
        is_valid = 1 if (words[i][0] in vowels and words[i][-1] in vowels) else 0
        prefix_sum[i + 1] = prefix_sum[i] + is_valid
        
    results = []
    for li, ri in queries:
        # The number of valid strings in range [li, ri] is prefix_sum[ri + 1] - prefix_sum[li]
        count = prefix_sum[ri + 1] - prefix_sum[li]
        results.append(count)
        
    return results
