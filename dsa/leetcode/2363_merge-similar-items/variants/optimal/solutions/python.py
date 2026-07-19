from collections import defaultdict

def solve(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    """
    Merges two lists of [value, weight] pairs, summing weights of identical values,
    and returns the result sorted by value in ascending order.
    """
    weights = defaultdict(int)
    
    # Accumulate weights from the first list
    for val, weight in items1:
        weights[val] += weight
        
    # Accumulate weights from the second list
    for val, weight in items2:
        weights[val] += weight
        
    # Sort by value (the dictionary keys) and format as [value, weight]
    return sorted([[val, weight] for val, weight in weights.items()])
