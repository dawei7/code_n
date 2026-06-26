# Minimum Cost to Cut a Stick

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1547 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Sorting |
| Official Link | [minimum-cost-to-cut-a-stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/) |

## Problem Description & Examples
### Goal
Cut a stick at all requested positions. Each cut costs the current length of the
piece being cut, so choose an order with minimum total cost.

### Function Contract
**Inputs**

- `n`: the original stick length.
- `cuts`: positions where the stick must be cut.

**Return value**

The minimum total cutting cost.

### Examples
**Example 1**

- Input: `n = 7, cuts = [1, 3, 4, 5]`
- Output: `16`

**Example 2**

- Input: `n = 9, cuts = [5, 6, 1, 4, 2]`
- Output: `22`

**Example 3**

- Input: `n = 5, cuts = [2, 4]`
- Output: `7`

---

## Underlying Base Algorithm(s)
Sort the cut positions and add sentinels `0` and `n`. Use interval dynamic
programming where `dp[i][j]` is the minimum cost to complete all cuts strictly
between boundary cuts `i` and `j`. Try every possible first cut inside the
interval and add the current stick length.

---

## Complexity Analysis
- **Time Complexity**: `O(c^3)`, where `c` is the number of cuts.
- **Space Complexity**: `O(c^2)`.
