# Minimum Cost to Connect Two Groups of Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1595 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Bit Manipulation, Matrix, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/) |

## Problem Description
### Goal
There are two groups of points. The first contains $m$ points and the second contains $n$ points, with $m \ge n$. Matrix `cost` has $m$ rows and $n$ columns, and `cost[i][j]` is the price of adding a connection between point $i$ in the first group and point $j$ in the second group.

Choose any set of connections such that every point in both groups is incident to at least one chosen connection. A point may be connected to several points in the opposite group; there is no one-to-one restriction. Return the minimum possible sum of the selected connection costs.

### Function Contract
**Inputs**

- `cost`: an $m \times n$ integer matrix where $1 \le n \le m \le 12$ and $0 \le \texttt{cost[i][j]} \le 100$.

**Return value**

Return the minimum total cost of connections that cover every point in both groups.

### Examples
**Example 1**

- Input: `cost = [[15, 96], [36, 2]]`
- Output: `17`

**Example 2**

- Input: `cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]`
- Output: `4`
- Explanation: The middle point of the first group may connect to two points in the second group; multiple connections per point are allowed.

**Example 3**

- Input: `cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]`
- Output: `10`

### Required Complexity
- **Time:** $O(mn2^n)$
- **Space:** $O(m2^n)$

<details>
<summary>Approach</summary>

#### General

**Give every first-group point one mandatory edge.** Because all costs are non-negative, an optimal solution never needs two edges from a first-group point merely to satisfy that point itself. Process the first group in order and choose one second-group endpoint for each point. A bitmask records which second-group points these mandatory choices have covered. Different choice histories with the same row index and mask have identical remaining obligations, so only their cheapest cost matters.

**Repair uncovered second-group points at the end.** After all $m$ rows have chosen an edge, some second-group bits may still be absent. For each uncovered point $j$, add its cheapest incident edge, `min(cost[i][j])`. These repairs are independent: they may attach to any already processed first-group point, and adding them cannot make another uncovered point covered. Precompute each column minimum so the terminal cost is quick to evaluate.

This construction represents an optimum. From any feasible connection set, select one incident edge for every first-group point as its mandatory edge; the remaining selected edges include coverage for every still-uncovered second-group point and cost at least that point's column minimum. Conversely, every DP choice plus the terminal repairs covers both groups. Minimizing over all mandatory choices and using the cheapest possible repairs therefore yields exactly the global minimum.

#### Complexity detail

There are at most $(m+1)2^n$ states `(i, mask)`. Each nonterminal state tries $n$ endpoints, giving $O(mn2^n)$ time. The memoized states use $O(m2^n)$ space, while the recursion depth is $O(m)$ and the column-minimum array uses $O(n)$ additional space.

#### Alternatives and edge cases

- **Enumerate one endpoint assignment per first-group point:** This tries $n^m$ assignments before repairing uncovered columns, repeating many equivalent `(i, mask)` states.
- **Minimum-cost matching:** Requiring one-to-one pairs is too restrictive because a point may need multiple incident edges and $m$ can exceed $n$.
- **Full edge-subset enumeration:** Testing all $2^{mn}$ subsets is correct but ignores the small second-group dimension that makes bitmask DP practical.
- Zero-cost edges are valid and can make the total answer `0`.
- When $n=1$, every first-group point must connect to the single second-group point, so every row's only cost is included.
- A second-group point omitted by all mandatory choices still needs its cheapest extra edge, even if that attaches to a first-group point that already has another connection.

</details>
