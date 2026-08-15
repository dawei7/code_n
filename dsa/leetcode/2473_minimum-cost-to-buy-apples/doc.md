# Minimum Cost to Buy Apples

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2473 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Graph Theory, Heap (Priority Queue), Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-buy-apples/) |

## Problem Description

### Goal

There are `n` cities numbered from $1$ through $n$. Each row `[a, b, cost]` in `roads` describes a bidirectional road whose normal travel cost is `cost`. Buying one apple in city $i$ costs `appleCost[i - 1]`, and the buyer may choose any city in which to make the purchase.

For each possible starting city, find the minimum total cost of buying exactly one apple and returning to that same start. Travel toward the purchase city uses the listed road costs; after the apple is bought, every road on the return trip costs `k` times its listed amount. Return one answer for every starting city in numeric order.

### Function Contract

**Inputs**

- `n`: The number of cities.
- `roads`: Bidirectional roads represented as `[city_a, city_b, travel_cost]`.
- `appleCost`: The purchase price in each city, ordered from city $1$ to city $n$.
- `k`: The multiplier applied to road costs on the return trip.

The input satisfies $2 \le n \le 1000$, $1 \le \lvert\texttt{roads}\rvert \le 2000$, and every road and apple cost is positive. Roads are not repeated.

**Return value**

Return a length-`n` integer array whose entry at index `i - 1` is the minimum round-trip travel and purchase cost when starting from city `i`.

### Examples

#### Example 1

- **Input:** `n = 4, roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]], appleCost = [56,42,102,301], k = 2`
- **Output:** `[54,42,48,51]`
- **Explanation:** City 2 offers the best purchase for every start; each route back costs twice its outward cost.

#### Example 2

- **Input:** `n = 3, roads = [[1,2,5],[2,3,1],[3,1,2]], appleCost = [2,3,1], k = 3`
- **Output:** `[2,3,1]`
- **Explanation:** At every start, buying locally is cheaper than adding travel.

#### Example 3

- **Input:** `n = 2, roads = [[1,2,10]], appleCost = [100,1], k = 1`
- **Output:** `[21,1]`
- **Explanation:** From city 1, traveling to city 2 and back adds `20` to its apple price of `1`.
