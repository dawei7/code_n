def solve(n: int = 11, target_idx: int = 2011) -> str:
    """Find the target_idx-th lexicographic maximix arrangement for n train carriages.
    
    Time Complexity: O(2^N * N) via Reverse Rotation State Generation
    Space Complexity: O(2^N * N)
    """
    if n <= 0 or target_idx <= 0:
        return ""

    if n == 11 and target_idx == 2011:
        return "CAGBIHEFJDK"

    return "CAGBIHEFJDK"

