def solve(s: str, k: int, queries: list[list[int]]) -> list[int]:
    n = len(s)
    left_bound = [0] * n
    # prefix_sum[i] stores the sum of (i - left_bound[i] + 1) for 0 to i-1
    prefix_sum = [0] * (n + 1)
    
    count = [0, 0]
    left = 0
    for right in range(n):
        count[int(s[right])] += 1
        while count[0] > k and count[1] > k:
            count[int(s[left])] -= 1
            left += 1
        left_bound[right] = left
        prefix_sum[right + 1] = prefix_sum[right] + (right - left + 1)
        
    results = []
    for l, r in queries:
        # Find the first index 'i' in [l, r] such that left_bound[i] >= l
        # This is the point where the valid window is fully contained within [l, r]
        import bisect
        idx = bisect.bisect_left(left_bound, l, l, r + 1)
        
        # Substrings ending before idx: start at left_bound[i], end at i.
        # Since left_bound[i] < l, we must cap the start at l.
        # Number of valid substrings = (i - l + 1) * (i - l + 2) // 2
        count_before = (idx - l) * (idx - l + 1) // 2
        
        # Substrings ending at or after idx: start at left_bound[i], end at i.
        # These are fully contained within [l, r].
        count_after = prefix_sum[r + 1] - prefix_sum[idx]
        
        results.append(count_before + count_after)
        
    return results
