# Egg Dropping Puzzle

| | |
|---|---|
| **ID** | `dp_16` |
| **Category** | dynamic |
| **Complexity (required)** | $O(K * N^2)$ Time, $O(K * N)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) |

## Problem statement

You are given `k` identical eggs and you have access to a building with `n` floors labeled from `1` to `n`.
You know that there exists a floor `f` (0 \le f \le n) such that any egg dropped at a floor higher than `f` will break, and any egg dropped at or below floor `f` will not break.
Each move, you may take an unbroken egg and drop it from any floor `x` (1 \le x \le n).
If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
Return the **minimum number of moves** that you need to determine with certainty what the value of `f` is.

**Input:** Two integers `k` (eggs) and `n` (floors).
**Output:** An integer representing the minimum number of moves in the worst-case scenario.

## When to use it

- The canonical "Minimax" Dynamic Programming problem.
- Tests your ability to handle worst-case scenarios ("with certainty") while optimizing your strategy to minimize that worst case.

## Approach

**1. Define the State:**
Let `dp[e][f]` be the minimum number of attempts needed to find the critical floor using exactly `e` eggs and a building with exactly `f` floors.

**2. Find the Base Cases:**
- If you have 1 egg (`e = 1`), you have no choice but to start at floor 1 and go up one by one. Worst case, it takes `f` drops. `dp[1][f] = f`.
- If you have 0 floors or 1 floor (`f = 0` or `f = 1`), it takes 0 or 1 drop respectively, regardless of how many eggs you have. `dp[e][0] = 0` and `dp[e][1] = 1`.

**3. Find the Transition (The recurrence relation):**
If you have `e` eggs and `f` floors, you can choose to drop your next egg from *any* floor `x` (1 \le x \le f).
When you drop an egg from floor `x`, there are exactly two physical outcomes:
- **Case A (The egg breaks):** The critical floor MUST be strictly below `x`. You now have `e - 1` eggs, and there are `x - 1` floors left to check. The attempts needed is `dp[e - 1][x - 1]`.
- **Case B (The egg survives):** The critical floor MUST be at `x` or above it. You still have `e` eggs, and there are `f - x` floors left to check. The attempts needed is `dp[e][f - x]`.

Because we need to know the answer *with certainty* (worst-case), nature will always force us into the worse of the two outcomes!
So for a specific floor `x`, the worst-case attempts is: `1 + max(dp[e - 1][x - 1], dp[e][f - x])`.
But YOU get to choose which floor `x` to drop from! You are smart, so you will pick the `x` that minimizes this worst-case scenario!
`dp[e][f] = 1 + min_{1 \le x \le f}( max(dp[e - 1][x - 1], dp[e][f - x]) )`

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_16: Egg Dropping.

dp[e][m] = max floors testable with e eggs and m moves.
Find smallest m with dp[k][m] >= n.
"""


def solve(k, n):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    m = 0
    while dp[k][m] < n:
        m += 1
        for e in range(1, k + 1):
            dp[e][m] = dp[e - 1][m - 1] + dp[e][m - 1] + 1
    return m
```

</details>

## Walk-through

`k = 2` eggs, `n = 4` floors.
Base cases pre-filled:
- `dp[1][1..4] = [1, 2, 3, 4]` (1 egg takes up to f drops).
- `dp[2][0] = 0, dp[2][1] = 1`.

Calculate `e = 2`, `f = 2`:
- Drop at x=1: `1 + max(dp[1][0], dp[2][1]) = 1 + max(0, 1) = 2`.
- Drop at x=2: `1 + max(dp[1][1], dp[2][0]) = 1 + max(1, 0) = 2`.
- `dp[2][2] = min(2, 2) = 2`.

Calculate `e = 2`, `f = 3`:
- Drop x=1: `1 + max(dp[1][0], dp[2][2]) = 1 + max(0, 2) = 3`.
- Drop x=2: `1 + max(dp[1][1], dp[2][1]) = 1 + max(1, 1) = 2`. (Optimal!)
- Drop x=3: `1 + max(dp[1][2], dp[2][0]) = 1 + max(2, 0) = 3`.
- `dp[2][3] = min(3, 2, 3) = 2`.

Calculate `e = 2`, `f = 4`:
- Drop x=1: `1 + max(dp[1][0], dp[2][3]) = 1 + max(0, 2) = 3`.
- Drop x=2: `1 + max(dp[1][1], dp[2][2]) = 1 + max(1, 2) = 3`.
- Drop x=3: `1 + max(dp[1][2], dp[2][1]) = 1 + max(2, 1) = 3`.
- Drop x=4: `1 + max(dp[1][3], dp[2][0]) = 1 + max(3, 0) = 4`.
- `dp[2][4] = 3`.

Result is 3. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(K * N^2)$ | $O(K * N)$ |
| **Average** | $O(K * N^2)$ | $O(K * N)$ |
| **Worst** | $O(K * N^2)$ | $O(K * N)$ |

The table is K x N. For every cell, the x loop runs up to N times. Time is $O(K x N^2)$.
Space is exactly $O(K x N)$ for the DP matrix.

## Variants & optimizations

- **Binary Search Optimization ($O(K x N log N)$):** Notice that inside the `x` loop, `dp[e - 1][x - 1]` is strictly *increasing* as `x` grows, and `dp[e][f - x]` is strictly *decreasing* as `x` grows. The optimal x is exactly where these two functions intersect! You can use Binary Search instead of a linear scan to find x, dropping the time complexity drastically.
- **Inverted State DP ($O(K x log N)$):** The ultimate mathematical optimization. Instead of `dp[eggs][floors] = moves`, flip the definition! Let `dp[moves][eggs] = max_floors`. You can check up to `dp[m][e] = 1 + dp[m-1][e-1] + dp[m-1][e]` floors. You just increment `m` until `dp[m][K] >= N`. This requires only $O(K)$ space and essentially runs instantly!

## Real-world applications

- **Stress Testing / Quality Assurance:** Finding the maximum safe stress threshold (temperature, voltage, pressure) for a physical component where destroying the component during testing is highly expensive (limited "eggs").

## Related algorithms in cOde(n)

- **[dp_13 - Matrix Chain Multiplication](dp_13_matrix-chain-multiplication.md)** — Another problem where you must iterate a third variable `k` (or `x`) inside the DP state to find an optimal split point.
- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — The $O(\log N)$ core concept of safely eliminating half of the search space, which Egg Dropping is trying to mimic under constrained resources.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
