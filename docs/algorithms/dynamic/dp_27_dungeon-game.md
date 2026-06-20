# Dungeon Game

| | |
|---|---|
| **ID** | `dp_27` |
| **Category** | dynamic |
| **Complexity (required)** | $O(M * N)$ Time, $O(N)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) |

## Problem statement

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of `m x n` rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room.
The knight can only move **down** or **right**.
Some rooms contain demons (negative integers), which decrease the knight's health. Other rooms contain magic orbs (positive integers), which increase the knight's health.
The knight's health MUST be \ge 1 at all times. If his health drops to 0 or below, he dies immediately.
Return the knight's **minimum initial health** so that he can successfully rescue the princess.

**Input:** An `m x n` integer matrix `dungeon`.
**Output:** An integer representing the minimum starting health required.

## When to use it

- To demonstrate mastery over **Backwards DP**.
- When a pathfinding problem has a strict non-negative running constraint, forward DP fails because local maximums might not lead to global validity.

## Approach

**1. The Flaw of Forward DP:**
If we start from `(0,0)` and try to track the "minimum health required to reach `(i, j)`", we face a paradox.
If we reach a cell with 2 paths:
- Path A: Requires `10` initial health, but currently gives you `50` bonus health.
- Path B: Requires `5` initial health, but currently gives you `1` bonus health.
Which path is "better"? Path B requires less initial health right now, but Path A gives you a massive shield against future demons! We cannot make a localized greedy choice going forward!

**2. Backwards DP:**
We MUST start from the princess at `(M-1, N-1)` and work backwards to the knight at `(0,0)`!
Let `dp[i][j]` be the **minimum health needed** upon entering cell `(i, j)` to safely reach the princess.

**3. Find the Base Case:**
At the princess's cell `(M-1, N-1)`:
- If her room has a demon (e.g., `-5`), we need enough health to survive it AND have at least `1` health left. So we need `6` health.
- If her room has an orb (e.g., `+5`), we still need at least `1` health just to be alive before entering.
Therefore: `dp[M-1][N-1] = max(1, 1 - dungeon[M-1][N-1])`.

**4. Find the Transition (The recurrence relation):**
For any internal cell `(i, j)`, the knight will inevitably leave this cell and move either DOWN to `(i+1, j)` or RIGHT to `(i, j+1)`.
To minimize his starting health, he should choose the path that requires LESS health!
So the health he needs *after* leaving this cell is: `min_health_on_exit = min(dp[i+1][j], dp[i][j+1])`.
To calculate the health needed *before* entering `(i, j)`, we subtract the healing/damage of `(i, j)` from `min_health_on_exit`.
If `dungeon[i][j]` heals him so much that the required health becomes negative, we clamp it to `1` (since he can never have \le 0 health).
`dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])`

**5. Space Optimization:**
Because calculating row `i` only requires row `i+1`, we can compress the M x N matrix into a 1D array of size N+1.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_27: Dungeon Game.

Backwards DP: dp[i][j] = min HP needed when entering (i,j)
to safely reach the princess. Fill from bottom-right to
top-left. Space-optimized to O(N) using a rolling 1D array.
"""


def solve(dungeon, m, n):
    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[n - 1] = 1
    for i in range(m - 1, -1, -1):
        new_dp = [INF] * (n + 1)
        for j in range(n - 1, -1, -1):
            min_exit = min(dp[j], new_dp[j + 1])
            new_dp[j] = max(1, min_exit - dungeon[i][j])
        dp = new_dp
    return dp[0]
```

</details>

## Walk-through

`dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]`.
M=3, N=3. Initial `dp = [inf, inf, inf, inf]`.
Set dummy: `dp[2] = 1`. `dp = [inf, inf, 1, inf]`.

1. **i = 2 (Bottom row):**
   - `j=2` (Princess, `-5`): `min_exit = min(1, inf) = 1`. `dp[2] = max(1, 1 - (-5)) = 6`. (Need 6 HP to fight the -5 demon). `dp = [inf, inf, 6, inf]`.
   - `j=1` (`30`): `min_exit = min(inf, 6) = 6`. `dp[1] = max(1, 6 - 30) = 1`. (Orb heals 30, only need 1 HP).
   - `j=0` (`10`): `min_exit = min(inf, 1) = 1`. `dp[0] = max(1, 1 - 10) = 1`.
   - `dp` state: `[1, 1, 6, inf]`.

2. **i = 1 (Middle row):**
   - `j=2` (`1`): `min_exit = min(6(down), inf(right)) = 6`. `dp[2] = max(1, 6 - 1) = 5`.
   - `j=1` (`-10`): `min_exit = min(1(down), 5(right)) = 1`. `dp[1] = max(1, 1 - (-10)) = 11`.
   - `j=0` (`-5`): `min_exit = min(1(down), 11(right)) = 1`. `dp[0] = max(1, 1 - (-5)) = 6`.
   - `dp` state: `[6, 11, 5, inf]`.

3. **i = 0 (Top row):**
   - `j=2` (`3`): `min_exit = min(5, inf) = 5`. `dp[2] = max(1, 5 - 3) = 2`.
   - `j=1` (`-3`): `min_exit = min(11, 2) = 2`. `dp[1] = max(1, 2 - (-3)) = 5`.
   - `j=0` (`-2`): `min_exit = min(6, 5) = 5`. `dp[0] = max(1, 5 - (-2)) = 7`.

Result `dp[0]` is 7. ✓ (Knight needs 7 HP to start).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M * N)$ | $O(N)$ |
| **Average** | $O(M * N)$ | $O(N)$ |
| **Worst** | $O(M * N)$ | $O(N)$ |

The nested loops strictly visit every cell in the M x N matrix once. Time is $O(M \times N)$.
By using the 1D rolling array, Space is $O(N)$ (where N is the number of columns).

## Variants & optimizations

- **Binary Search on Answer:** If you struggle to wrap your head around Backwards DP, you can actually solve this using Forward DP combined with Binary Search! You binary search the starting health `H` (from 1 to Infinity). For a given `H`, you run a standard Forward DP to see if you can reach the end without dying. This approach takes $O(M x N x log(\text{MaxHealth})$) time, but is extremely intuitive to write!

## Real-world applications

- **Supply Chain Logistics:** Calculating the minimum initial fuel / capital required for a fleet of vehicles traveling across a network of cities where some cities charge tolls (demons) and others offer refueling grants (orbs), ensuring bankruptcy never occurs.

## Related algorithms in cOde(n)

- **[dp_12 - Minimum Path Sum](dp_12_min-cost-path.md)** — The foundational Forward DP algorithm that this problem forces you to invert.
- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — The alternative $O(M x N log(\text{Health})$) approach.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
