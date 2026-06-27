import bisect
from typing import List

def solve(envelopes: List[List[int]]) -> int:
    if not envelopes:
        return 0
    
    # Sort by width ascending, then by height descending.
    # Descending height for same width prevents picking multiple envelopes of same width.
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    # Find the Longest Increasing Subsequence (LIS) of the heights.
    tails = []
    for _, h in envelopes:
        idx = bisect.bisect_left(tails, h)
        if idx < len(tails):
            tails[idx] = h
        else:
            tails.append(h)
            
    return len(tails)
