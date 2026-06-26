from typing import List

def solve(score: List[List[int]], k: int) -> List[List[int]]:
    """
    Sorts the students based on their score in the k-th subject in descending order.
    
    Args:
        score: A 2D list of integers representing student scores.
        k: The index of the subject to sort by.
        
    Returns:
        The sorted 2D list.
    """
    # Python's sort is stable and uses Timsort.
    # We sort the list of rows using the k-th element of each row as the key.
    # reverse=True ensures descending order.
    score.sort(key=lambda row: row[k], reverse=True)
    return score
