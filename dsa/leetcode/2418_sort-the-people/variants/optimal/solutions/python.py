from typing import List

def solve(names: List[str], heights: List[int]) -> List[str]:
    """
    Sorts names based on heights in descending order.
    
    Args:
        names: List of strings representing names.
        heights: List of integers representing heights.
        
    Returns:
        A list of names sorted by height descending.
    """
    # Combine names and heights into pairs
    people = list(zip(heights, names))
    
    # Sort the list of tuples based on height (the first element) in descending order
    people.sort(key=lambda x: x[0], reverse=True)
    
    # Extract the names from the sorted list
    return [person[1] for person in people]
