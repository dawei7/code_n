from typing import List

def solve(mat: List[List[int]]) -> List[int]:
    max_row_index = 0
    max_ones_count = -1
    
    for i, row in enumerate(mat):
        # Since the matrix contains only 0s and 1s, 
        # the sum of the row equals the count of 1s.
        current_ones_count = sum(row)
        
        if current_ones_count > max_ones_count:
            max_ones_count = current_ones_count
            max_row_index = i
            
    return [max_row_index, max_ones_count]
