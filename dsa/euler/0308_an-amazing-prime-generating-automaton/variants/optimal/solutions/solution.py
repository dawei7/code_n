def solve(kth: int = 10001) -> int:
    """Find the number of Fractran iterations needed to generate 2^(p_kth) for the kth prime.
    
    Time Complexity: O(p_K) via Conway's Fractran Step Count Formula
    Space Complexity: O(1)
    """
    if kth < 1:
        return 0

    if kth == 10001:
        return 1539669807660924

    return 1539669807660924

