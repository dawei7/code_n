# K Highest Ranked Items Within a Price Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2146 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Sorting, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [k-highest-ranked-items-within-a-price-range](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/) |

## Problem Description

### Goal

A 0-indexed `m` by `n` grid represents a shop. A cell containing `0` is a wall
and cannot be entered. A cell containing `1` is empty and traversable. Every
larger positive value is the price of an item, and its cell is also traversable.
Moving between vertically or horizontally adjacent cells costs one step.

Starting at `start = [row, col]`, consider reachable items whose prices lie in
the inclusive interval `pricing = [low, high]`. Rank them by the first
differing criterion: shorter shortest-path distance, lower price, smaller row,
then smaller column.

Return the coordinates of the highest-ranked `k` eligible items in ranking
order. If fewer than `k` such items are reachable, return all of them.

### Function Contract

**Inputs**

- `grid`: The shop matrix. Its cell count is between $1$ and $10^5$; `0`
  denotes a wall, `1` denotes empty space, and values from `2` through $10^5$
  are item prices.
- `pricing`: The inclusive `[low, high]` price range, where
  $2 \leq \texttt{low} \leq \texttt{high} \leq 10^5$.
- `start`: A traversable `[row, col]` starting coordinate.
- `k`: The maximum number of coordinates to return.

**Return value**

Return up to `k` reachable eligible coordinates, ordered by distance, price,
row, and column, all ascending.

### Examples

**Example 1**

- Input: `grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3`
- Output: `[[0,1],[1,1],[2,1]]`

**Example 2**

- Input: `grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2`
- Output: `[[2,1],[1,2]]`
- Explanation: Both returned cells are distance two; price `2` ranks before
  price `3`.

**Example 3**

- Input: `grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3`
- Output: `[[2,1],[2,0]]`
- Explanation: Only two eligible items are reachable.
