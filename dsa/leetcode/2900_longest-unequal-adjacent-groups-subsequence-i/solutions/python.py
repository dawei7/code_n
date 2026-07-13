from typing import List

def solve(words: List[str], groups: List[int]) -> List[str]:
    """
    Constructs the longest subsequence where adjacent elements belong to different groups.
    Uses a greedy strategy to pick elements whenever the group changes.
    """
    if not words:
        return []
    
    result = [words[0]]
    last_group = groups[0]
    
    for i in range(1, len(words)):
        if groups[i] != last_group:
            result.append(words[i])
            last_group = groups[i]
            
    return result
