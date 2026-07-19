from typing import List

def solve(pref: List[int]) -> List[int]:
    """
    Reconstructs the original array from its prefix XOR array.
    
    Logic:
    pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
    pref[i-1] = arr[0] ^ arr[1] ^ ... ^ arr[i-1]
    Therefore, pref[i] ^ pref[i-1] = arr[i]
    """
    n = len(pref)
    if n == 0:
        return []
    
    res = [0] * n
    res[0] = pref[0]
    
    for i in range(1, n):
        res[i] = pref[i] ^ pref[i-1]
        
    return res
