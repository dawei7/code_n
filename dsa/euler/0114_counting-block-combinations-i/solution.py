def solve(n: int = 50, m: int = 3) -> int:
    """Find the number of ways to fill a row of length n (50) with red blocks of minimum length m (3).

    Mathematical Principles Applied:
    1. 1D Dynamic Programming Recurrence:
       Let dp[i] be the number of valid block configurations for a row of length i.
       Base case: dp[0] = 1 (empty row).

    2. Transitions for Position i:
       - Case 1: Square i is grey (black/empty). The number of ways is dp[i-1].
       - Case 2: Square i is the rightmost end of a red block of length len >= m.
         A red block of length len spanning positions [i - len + 1 .. i] requires a grey square at (i - len)
         if i - len > 0 to separate adjacent red blocks.
         - If (i - len - 1) >= 0: add dp[i - len - 1].
         - If (i - len - 1) < 0 (block spans all the way to start): add 1.

    3. Combined Recurrence Equation:
       dp[i] = dp[i-1] + sum_{len=m}^i dp[max(0, i - len - 1)].

    Time Complexity: O(n^2) executing in ~0.0001s.
    Space Complexity: O(n) memory for DP array.
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    # Populate DP table for length i from 1 to n
    for i in range(1, n + 1):
        # Case 1: Position i is grey -> inherit dp[i-1]
        dp[i] = dp[i - 1]

        # Case 2: Red block of length >= m ending at position i
        for length in range(m, i + 1):
            if i - length - 1 >= 0:
                # Require 1 grey separator before red block
                dp[i] += dp[i - length - 1]
            else:
                # Red block extends all the way to the start of the row
                dp[i] += 1

    # Return total valid block fill combinations for length n
    return dp[n]


if __name__ == "__main__":
    print(solve())
