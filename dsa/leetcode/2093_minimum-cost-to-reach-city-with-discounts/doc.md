# Minimum Cost to Reach City With Discounts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2093 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/) |

## Problem Description

### Goal

There are $n$ cities numbered from `0` through `n - 1`. Each highway `[city1, city2, toll]` is undirected and may be traveled in either direction by paying `toll`. No pair of cities has more than one highway.

You own a limited number of single-use discounts. Applying one discount to a highway traversal changes that traversal's cost to `toll // 2`, and at most one discount may be used on a traversal. Discounts are optional. Return the minimum cost of reaching city `n - 1` from city `0`, or `-1` if no route exists.

### Function Contract

**Inputs**

- `n`: the city count, where $2 \le n \le 1000$.
- `highways`: $E$ distinct undirected edges `[city1, city2, toll]`, where $1 \le E \le 1000$.
- Each toll is between $0$ and $10^5$.
- `discounts`: the available discount count $K$, where $0 \le K \le 500$.

**Return value**

Return the minimum achievable total toll from city `0` to city `n - 1`, or `-1` when the destination is unreachable.

### Examples

**Example 1**

- Input: `n = 5`, `highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]]`, `discounts = 1`
- Output: `9`
- Explanation: Pay `4` from `0` to `1`, then discount toll `11` to `5`.

**Example 2**

- Input: `n = 4`, `highways = [[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]]`, `discounts = 20`
- Output: `8`
- Explanation: The route `0 -> 1 -> 2 -> 3` discounts its tolls to `3`, `3`, and `2`.

**Example 3**

- Input: `n = 4`, `highways = [[0,1,3],[2,3,2]]`, `discounts = 0`
- Output: `-1`
