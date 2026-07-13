from typing import List
from collections import Counter

def solve(arr: List[str]) -> List[str]:
    # Count occurrences of every substring across all strings
    # A substring is only valid if it appears in exactly one string
    # and that string is the one we are currently checking.
    
    substring_counts = Counter()
    
    # Pre-calculate all substrings for every string
    # We use a set for each string to avoid counting the same substring 
    # multiple times within the same string.
    all_substrings_per_word = []
    for s in arr:
        n = len(s)
        subs = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                subs.add(s[i:j])
        all_substrings_per_word.append(subs)
        for sub in subs:
            substring_counts[sub] += 1
            
    result = []
    for idx, s in enumerate(arr):
        n = len(s)
        found = False
        # Check lengths from 1 to n to find the shortest
        for length in range(1, n + 1):
            candidates = []
            for i in range(n - length + 1):
                sub = s[i:i + length]
                # If this substring appears only in the current string
                if substring_counts[sub] == 1:
                    candidates.append(sub)
            
            if candidates:
                # Sort lexicographically to pick the smallest
                candidates.sort()
                result.append(candidates[0])
                found = True
                break
        
        if not found:
            result.append("")
            
    return result
