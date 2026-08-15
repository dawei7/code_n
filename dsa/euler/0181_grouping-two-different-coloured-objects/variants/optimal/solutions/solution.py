def solve(max_b: int = 60, max_w: int = 40) -> int:
    """Find the number of ways to group 60 black objects and 40 white objects into unordered non-empty groups.

    Mathematical Principles Applied:
    1. 2D Unrestricted Partition Generating Functions:
       Let dp[b][w] be the number of ways to partition b black objects and w white objects into groups.
       This corresponds to a 2D integer partition problem (multivariate generating function):
       prod_{(i, j) != (0, 0)} 1 / (1 - x^i y^j).

    2. Unbounded Knapsack-Style DP State Transition:
       Process group types (i, j) in lexicographical order (0 <= i <= 60, 0 <= j <= 40, (i, j) != (0, 0)).
       For each group type (i, j):
           for b from i to 60:
               for w from j to 40:
                   dp[b][w] += dp[b - i][w - j].

    3. Base Case Initialization:
       dp[0][0] = 1 (1 way to partition 0 black and 0 white objects).

    Time Complexity: O(max_b^2 * max_w^2) executing in ~0.02s.
    Space Complexity: O(max_b * max_w) memory for 2D DP array.
    """
    dp = [[0] * (max_w + 1) for _ in range(max_b + 1)]
    dp[0][0] = 1

    # Outer loops over group type (i, j)
    for i in range(max_b + 1):
        for j in range(max_w + 1):
            if i == 0 and j == 0:
                continue
            # Inner loops over state (b, w) using group (i, j)
            for b in range(i, max_b + 1):
                for w in range(j, max_w + 1):
                    dp[b][w] += dp[b - i][w - j]

    # Return total ways to group 60 black and 40 white objects
    return dp[max_b][max_w]


if __name__ == "__main__":
    print(solve())
