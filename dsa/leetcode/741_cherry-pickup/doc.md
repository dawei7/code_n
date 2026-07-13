# Cherry Pickup

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 741 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Matrix |
| Official Link | [LeetCode](https://leetcode.com/problems/cherry-pickup/) |

## Problem Description
### Goal
An $n \times n$ grid contains empty cells `0`, cherries `1`, and impassable thorns `-1`. Travel from `(0, 0)` to $(n - 1, n - 1)$ using only right or down moves through valid cells, then return using only left or up moves.

Collect a cherry when a route first visits its cell; that cell becomes empty, so the return trip cannot collect it again. Return the maximum cherries obtainable over both journeys. If no valid outward-and-return trip exists, return `0`; neither route may enter a thorn.

### Function Contract
**Inputs**

- `grid`: an $n \times n$ matrix containing `-1` for thorns, `0` for empty cells, and `1` for cherries; the two endpoints are not thorns

**Return value**

- The maximum cherries collectable by a right/down outward path and a left/up return path, or `0` when no complete trip exists

### Examples
**Example 1**

- Input: `grid = [[0,1,-1],[1,0,-1],[1,1,1]]`
- Output: `5`

**Example 2**

- Input: `grid = [[1,1,-1],[1,-1,1],[-1,1,1]]`
- Output: `0`

**Example 3**

- Input: `grid = [[1,1,1],[1,1,1],[1,1,1]]`
- Output: `8`

### Required Complexity

- **Time:** $O(n^3)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Reverse the return path conceptually**

A return path from bottom-right to top-left can be reversed into another path from top-left to bottom-right using right and down moves. The problem becomes choosing two forward paths and counting cherries in their union. This removes the need to mutate cherries between separate trips.

**Synchronize the two walkers by diagonal step**

After $k$ moves, each walker satisfies $r+c=k$. Therefore a state needs only their two row coordinates `(r1, r2)`; columns are $k-r_1$ and $k-r_2$. This reduces the apparent four-coordinate state to two coordinates per layer.

**Transition from four paired moves**

For each step, ignore positions outside the grid or on thorns. Each walker arrived by moving right, which keeps its row, or down, which increases its row. Thus the best predecessor is the maximum of `(r1,r2)`, `(r1-1,r2)`, `(r1,r2-1)`, and `(r1-1,r2-1)` in the previous layer. Unreachable predecessors remain negative infinity.

**Count shared cells only once**

Add the cherry at the first walker's cell and also the second walker's cherry only when their rows differ. On a synchronized diagonal, equal rows imply equal columns and hence the same cell. Reusing only the previous and current `n x n` layers gives the final value at `(n-1,n-1)`.

**Why the dynamic program represents every round trip**

Every legal round trip corresponds bijectively to two legal synchronized forward paths. At each step, the four predecessor choices cover all combinations of right/down moves, and thorn filtering removes exactly the illegal states. The stored score is the best union count for those positions because shared cells are counted once at the only step when both walkers occupy them. Maximizing every predecessor therefore finds the best path pair; an unreachable final state means no round trip exists.

#### Complexity detail

There are `2n-1` diagonal layers and at most $n^{2}$ row pairs per layer, each with four constant-time predecessors. Time is $O(n^3)$. Two `n x n` score layers use $O(n^2)$ space.

#### Alternatives and edge cases

- **Top-down memoization:** recurse on `(r1, c1, r2)` and derive `c2`; it has the same $O(n^3)$ state count and often reads closer to the two-walker formulation.
- **Enumerate complete path pairs:** generate every valid monotone path and compare their cherry unions; this is correct for small grids but exponential in `n`.
- **Choose the best outward path first:** greedily maximizing the first trip can remove cherries needed for a much better combined pair and is not globally correct.
- **No complete path:** return zero rather than a negative unreachable sentinel.
- **One-cell grid:** both conceptual walkers share the endpoint, so its cherry is counted once.
- **Shared endpoints and crossings:** any cell occupied by both walkers on the same step contributes at most one cherry.
- **Thorns:** a state is invalid if either walker lands on `-1`.
- **Empty cells:** they preserve reachability while adding no score.

</details>
