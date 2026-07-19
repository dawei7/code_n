# Count Unhappy Friends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1583 |
| Difficulty | Medium |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/count-unhappy-friends/) |

## Problem Description
### Goal

There are $N$ friends numbered from $0$ through $N-1$, where $N$ is even. Each friend lists every other friend in `preferences[x]`, ordered from most preferred to least preferred. The `pairs` array assigns every friend exactly one partner.

Friend `x`, paired with `y`, is unhappy when another friend `u`, paired with `v`, satisfies both conditions: `x` prefers `u` over `y`, and `u` prefers `x` over `v`.

Count the friends for whom at least one such mutually preferable alternative exists. Count each unhappy friend once, even when several alternatives satisfy the condition.

### Function Contract
**Inputs**

- `n`: An even number of friends, where $2 \le N \le 500$.
- `preferences`: $N$ permutations of the other $N-1$ friend identifiers, ordered from most to least preferred.
- `pairs`: $N/2$ disjoint two-person pairs covering every friend exactly once.

**Return value**

Return the number of friends who are unhappy under the assigned pairing.

### Examples
**Example 1**

- Input: `n = 4, preferences = [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], pairs = [[0,1],[2,3]]`
- Output: `2`

**Example 2**

- Input: `n = 2, preferences = [[1],[0]], pairs = [[1,0]]`
- Output: `0`

**Example 3**

- Input: `n = 4, preferences = [[1,3,2],[2,3,0],[1,3,0],[0,2,1]], pairs = [[1,3],[0,2]]`
- Output: `4`
