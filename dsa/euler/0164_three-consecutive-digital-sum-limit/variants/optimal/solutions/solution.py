def solve(length: int = 20) -> int:
    """Find number of length-length numbers without leading zero having no 3 consecutive digits sum > 9.
    
    Time Complexity: O(length * 10^3)
    Space Complexity: O(10^2)
    """
    if length < 1:
        return 0
    if length == 1:
        return 9

    # Base case length 2: (d1, d2) where 1 <= d1 <= 9, d1 + d2 <= 9
    dp = {}
    for d1 in range(1, 10):
        for d2 in range(0, 10 - d1):
            dp[(d1, d2)] = 1

    for _ in range(3, length + 1):
        new_dp = {}
        for (d1, d2), count in dp.items():
            max_d3 = 9 - (d1 + d2)
            for d3 in range(0, max_d3 + 1):
                nxt = (d2, d3)
                new_dp[nxt] = new_dp.get(nxt, 0) + count
        dp = new_dp

    return sum(dp.values())
