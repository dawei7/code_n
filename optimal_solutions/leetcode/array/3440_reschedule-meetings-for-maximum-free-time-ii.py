def solve(eventTime: int, startTime: list[int], endTime: list[int]) -> int:
    n = len(startTime)
    meetings = sorted(zip(startTime, endTime))
    
    # Calculate gaps between meetings
    # gaps[i] is the gap between meeting i-1 and meeting i
    # gaps[0] is before the first meeting, gaps[n] is after the last
    gaps = [0] * (n + 1)
    gaps[0] = meetings[0][0]
    for i in range(1, n):
        gaps[i] = meetings[i][0] - meetings[i-1][1]
    gaps[n] = eventTime - meetings[n-1][1]
    
    # Precompute prefix and suffix max gaps
    pref_max = [0] * (n + 1)
    suff_max = [0] * (n + 1)
    for i in range(n + 1):
        pref_max[i] = gaps[i]
        if i > 0:
            pref_max[i] = max(pref_max[i], pref_max[i-1])
            
    for i in range(n, -1, -1):
        suff_max[i] = gaps[i]
        if i < n:
            suff_max[i] = max(suff_max[i], suff_max[i+1])
            
    # To efficiently check if a gap exists elsewhere, 
    # we need to know the second largest gap.
    # We use a sorted list of all gaps to query this.
    import bisect
    sorted_gaps = sorted(gaps)
    
    def get_max_gap_excluding(val):
        # Find index of val and return the max of the remaining
        idx = bisect.bisect_left(sorted_gaps, val)
        # Remove one instance of val
        temp = sorted_gaps[:idx] + sorted_gaps[idx+1:]
        return temp[-1] if temp else 0

    ans = 0
    for i in range(n):
        duration = meetings[i][1] - meetings[i][0]
        
        # Can we move meeting i into a gap?
        # The gap created by removing meeting i is gaps[i] + gaps[i+1] + duration
        # We check if we can fit this meeting into any other gap
        
        # Max gap available excluding the current surrounding gaps
        # We need the largest gap in the array that is not gaps[i] or gaps[i+1]
        # Actually, we just need the largest gap available in the whole set
        # excluding the ones we are merging.
        
        # Optimization: check if the largest gap (excluding current) >= duration
        # We use the precomputed sorted_gaps
        best_other = 0
        # If we remove gaps[i] and gaps[i+1], the largest remaining is:
        # We can use a frequency map or just check the two largest
        # For simplicity, check the max of (pref_max[i-1], suff_max[i+2])
        if i > 0:
            best_other = max(best_other, pref_max[i-1])
        if i + 2 <= n:
            best_other = max(best_other, suff_max[i+2])
            
        if best_other >= duration:
            ans = max(ans, gaps[i] + gaps[i+1] + duration)
        else:
            ans = max(ans, gaps[i] + gaps[i+1])
            
    return ans
