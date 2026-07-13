# K Highest Ranked Items Within a Price Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2146 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Breadth-First Search, Sorting, Heap (Priority Queue), Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [k-highest-ranked-items-within-a-price-range](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/).

### Goal
From a starting cell, find up to `k` reachable items whose prices lie in a given inclusive range. Rank eligible cells by shortest path distance, then price, row, and column, all ascending; blocked cells cannot be crossed.

### Function Contract
**Inputs**

- `grid`: a matrix where `0` is blocked, `1` is an empty traversable cell, and values above `1` are item prices.
- `pricing`: `[low, high]`, the accepted price interval.
- `start`: the starting `[row, column]`.
- `k`: the maximum number of item coordinates to return.

**Return value**

Coordinates of the first `k` reachable eligible items in ranking order, or all such items if fewer exist.

### Examples
**Example 1**

- Input: `grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]`, `pricing = [2, 5]`, `start = [0, 0]`, `k = 3`
- Output: `[[0, 1], [1, 1], [2, 1]]`

**Example 2**

- Input: `grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]`, `pricing = [2, 3]`, `start = [0, 0]`, `k = 2`
- Output: `[[0, 1], [1, 1]]`

**Example 3**

- Input: `grid = [[2]]`, `pricing = [1, 2]`, `start = [0, 0]`, `k = 1`
- Output: `[[0, 0]]`

---

## Solution
### Approach
Run breadth-first search from `start` to visit cells in nondecreasing distance. Gather eligible items one BFS layer at a time, sort that layer by `(price, row, column)`, and append it to the answer. Stop after obtaining `k` coordinates; processing by layers preserves distance as the primary rank.

### Complexity Analysis
- **Time Complexity**: `O(mn log(mn))` in the worst case due to ranking eligible cells
- **Space Complexity**: `O(mn)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
