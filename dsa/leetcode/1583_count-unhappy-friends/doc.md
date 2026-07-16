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

### Required Complexity

- **Time:** $O(N^2)$
- **Space:** $O(N^2)$

<details>
<summary>Approach</summary>

#### General

**Make preference comparisons constant-time**

Build `rank[x][u]`, the position of friend `u` in `x`'s preference list. A smaller position means a stronger preference. Also expand `pairs` into `partner[x]` so every assigned partner is available in constant time.

**Inspect only alternatives preferred over the current partner**

For each friend `x`, scan `preferences[x]` from the beginning and stop upon reaching `partner[x]`. Every earlier friend `u` satisfies the first unhappiness condition automatically.

For each such `u`, compare `rank[u][x]` with `rank[u][partner[u]]`. If the first is smaller, `u` reciprocally prefers `x`, so mark `x` unhappy and stop scanning alternatives for `x`.

Every possible witness for `x` occurs before its assigned partner and is examined. Friends after the partner cannot satisfy the first condition. The rank comparison is exactly the second condition, so the method finds a witness if and only if `x` is unhappy, while the early break counts `x` at most once.

#### Complexity detail

Building the rank table processes $N(N-1)$ preference entries. Across all friends, witness scans examine at most another $N(N-1)$ entries, giving $O(N^2)$ time.

The rank table uses $O(N^2)$ space, and the partner array uses $O(N)$.

#### Alternatives and edge cases

- **Use inverse-rank dictionaries:** store one mapping per friend instead of a dense table. This has the same asymptotic bounds.
- **Repeated linear rank searches:** search each preference list linearly for every candidate comparison. It is correct but can take $O(N^3)$ time.
- **Check every pair of friends:** test all $x,u$ combinations with precomputed ranks. This remains $O(N^2)$ but ignores the useful partner cutoff.
- **Two friends:** each is paired with the only possible partner, so neither can be unhappy.
- **Partner ranked first:** that friend has no preferred alternative and cannot be unhappy.
- **No reciprocal preference:** preferring another person is insufficient unless that person also prefers the friend over their own partner.
- **Several witnesses:** the friend still contributes only one to the answer.
- **Asymmetric outcome:** one friend may be unhappy without their assigned partner being unhappy.
- **All friends unhappy:** every friend is counted independently.

</details>
