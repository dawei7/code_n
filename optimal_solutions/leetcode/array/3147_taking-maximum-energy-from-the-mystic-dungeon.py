from typing import List

def solve(energy: List[int], k: int) -> int:
    """
    Calculates the maximum energy by iterating backwards.
    We use the property that the energy at index i is the sum of 
    energy[i] and the total energy collected from index i + k.
    """
    n = len(energy)
    # We create a DP array where dp[i] is the max energy starting from i
    # We can perform this in-place to save space.
    # Iterate backwards from the end of the array.
    for i in range(n - 1, -1, -1):
        if i + k < n:
            energy[i] += energy[i + k]
            
    # The answer is the maximum value in the modified energy array.
    # Note: We only consider starting positions that allow for a full path
    # to the end, but since we can start anywhere, any index is a valid start.
    return max(energy)
