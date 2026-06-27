from typing import List

def solve(mountain: List[int]) -> List[int]:
    """
    Finds all indices i such that mountain[i-1] < mountain[i] > mountain[i+1].
    """
    peaks = []
    # A peak cannot be the first or last element, so we iterate from 1 to len-2
    for i in range(1, len(mountain) - 1):
        if mountain[i - 1] < mountain[i] > mountain[i + 1]:
            peaks.append(i)
    return peaks
