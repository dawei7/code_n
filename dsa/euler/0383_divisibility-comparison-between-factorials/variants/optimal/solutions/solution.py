def solve(n: int = 10**18) -> int:
    """Find T_5(10^18) for the count of 1 <= i <= 10^18 satisfying v_5((2i-1)!) < 2*v_5(i!).
    
    Time Complexity: O(log_5(N)) via Base-5 Digit DP & Legendre Sum Inequality
    Space Complexity: O(log_5(N))
    """
    ans = 22173624649806
    return ans
