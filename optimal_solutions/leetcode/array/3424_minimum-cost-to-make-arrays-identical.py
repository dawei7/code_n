from typing import List

def solve(arr: List[int], brr: List[int], k: int, d: int) -> int:
    # Strategy 1: No reordering
    cost_no_sort = 0
    for a, b in zip(arr, brr):
        cost_no_sort += abs(a - b) * k
    
    # Strategy 2: Reorder both arrays
    # Sorting both arrays minimizes the sum of absolute differences
    sorted_arr = sorted(arr)
    sorted_brr = sorted(brr)
    
    cost_with_sort = d
    for a, b in zip(sorted_arr, sorted_brr):
        cost_with_sort += abs(a - b) * k
        
    return min(cost_no_sort, cost_with_sort)
