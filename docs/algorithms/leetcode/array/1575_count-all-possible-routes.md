# Count All Possible Routes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1575 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization |
| Official Link | [count-all-possible-routes](https://leetcode.com/problems/count-all-possible-routes/) |

## Problem Description & Examples
### Goal
Count routes that start at `start`, may visit cities repeatedly, and end at
`finish` without spending more than the available fuel.

### Function Contract
**Inputs**

- `locations`: city positions on a line.
- `start`: the starting city index.
- `finish`: the destination city index.
- `fuel`: the starting fuel amount.

**Return value**

The number of valid routes modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `locations = [2, 3, 6, 8, 4], start = 1, finish = 3, fuel = 5`
- Output: `4`

**Example 2**

- Input: `locations = [4, 3, 1], start = 1, finish = 0, fuel = 6`
- Output: `5`

**Example 3**

- Input: `locations = [5, 2, 1], start = 0, finish = 2, fuel = 3`
- Output: `0`

---

## Underlying Base Algorithm(s)
Use memoized dynamic programming on `(city, remaining_fuel)`. Each state counts
one route immediately if `city == finish`, then tries moving to every other city
whose distance cost fits in the remaining fuel.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2 * fuel)`.
- **Space Complexity**: `O(n * fuel)`.
