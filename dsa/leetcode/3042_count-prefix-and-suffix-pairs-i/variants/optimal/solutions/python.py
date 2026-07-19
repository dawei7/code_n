from typing import List

def solve(words: List[str]) -> int:
    """
    Counts the number of pairs (i, j) such that i < j and 
    words[i] is both a prefix and a suffix of words[j].
    """
    count = 0
    n = len(words)
    
    for i in range(n):
        for j in range(i + 1, n):
            str1 = words[i]
            str2 = words[j]
            
            # A string cannot be a prefix/suffix of a shorter string
            if len(str1) > len(str2):
                continue
                
            if str2.startswith(str1) and str2.endswith(str1):
                count += 1
                
    return count
