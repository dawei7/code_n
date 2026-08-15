# Find the Number of Distinct Colors Among the Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3160 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/) |

## Problem Description

### Goal

There are `limit + 1` balls with distinct labels from `0` through `limit`. Every ball begins without a color. Process the two-dimensional array `queries` in order; a query `[x, y]` assigns color `y` to ball `x`. If that ball was already colored, the new assignment replaces its previous color.

After each query, count how many distinct colors are currently used by at least one ball. An uncolored ball contributes nothing to this count, and being uncolored is not itself treated as a color. Return the sequence of counts, one value after every query.

### Function Contract

**Inputs**

- `limit`: The largest ball label, with $1 \le \texttt{limit} \le 10^9$. Valid labels range from `0` through `limit`.
- `queries`: A list of $n$ pairs `[x, y]`, where $1 \le n \le 10^5$, $0 \le x \le \texttt{limit}$, and $1 \le y \le 10^9$.

**Return value**

Return a list of $n$ integers. Entry $i$ is the number of distinct colors present immediately after applying `queries[i]`.

### Examples

#### Example 1

- **Input:** `limit = 4, queries = [[1, 4], [2, 5], [1, 3], [3, 4]]`
- **Output:** `[1, 2, 2, 3]`
- **Explanation:** Recoloring ball `1` removes color `4` temporarily, then ball `3` introduces it again.

#### Example 2

- **Input:** `limit = 4, queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]`
- **Output:** `[1, 2, 2, 3, 4]`
- **Explanation:** Balls `1` and `2` share color `2`, so the third assignment does not add a distinct color.
