# Sell Diminishing-Valued Colored Balls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1648 |
| Difficulty | Medium |
| Topics | Array, Math, Binary Search, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [sell-diminishing-valued-colored-balls](https://leetcode.com/problems/sell-diminishing-valued-colored-balls/) |

## Problem Description & Examples
### Goal
Sell exactly `orders` balls from color inventories where each sold ball is worth
the current inventory count of its color. Maximize total profit.

### Function Contract
**Inputs**

- `inventory`: counts of balls by color.
- `orders`: number of balls to sell.

**Return value**

The maximum profit modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `inventory = [2, 5], orders = 4`
- Output: `14`

**Example 2**

- Input: `inventory = [3, 5], orders = 6`
- Output: `19`

**Example 3**

- Input: `inventory = [2, 8, 4, 10, 6], orders = 20`
- Output: `110`

---

## Underlying Base Algorithm(s)
Sort inventories descending and sell value levels in batches. If the highest
`count` colors can all be lowered to the next inventory level within the
remaining orders, add the arithmetic-series profit for that whole band.
Otherwise sell only the needed number of top levels, splitting into full rounds
and a remainder.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`.
- **Space Complexity**: `O(1)` extra space if sorting in place.
