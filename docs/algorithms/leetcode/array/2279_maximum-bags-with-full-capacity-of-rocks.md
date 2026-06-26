# Maximum Bags With Full Capacity of Rocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2279 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [maximum-bags-with-full-capacity-of-rocks](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/) |

## Problem Description & Examples
### Goal
Distribute at most `additionalRocks` among bags without exceeding their capacities. Maximize how many bags become exactly full.

### Function Contract
**Inputs**

- `capacity`: maximum rocks for each bag.
- `rocks`: current rocks at matching indices.
- `additionalRocks`: available rocks to add.

**Return value**

The greatest number of bags that can be full.

### Examples
**Example 1**

- Input: `capacity = [2, 3, 4, 5]`, `rocks = [1, 2, 4, 4]`, `additionalRocks = 2`
- Output: `3`

**Example 2**

- Input: `capacity = [10, 2, 2]`, `rocks = [2, 2, 0]`, `additionalRocks = 100`
- Output: `3`

**Example 3**

- Input: `capacity = [5]`, `rocks = [0]`, `additionalRocks = 4`
- Output: `0`

---

## Underlying Base Algorithm(s)
Compute each bag's deficit `capacity[i] - rocks[i]` and sort deficits ascending. Fill bags from cheapest to most expensive until the next deficit exceeds the remaining additional rocks. Zero-deficit bags are counted automatically.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` for deficits, or `O(1)` extra if an input array is reused
