# Number of Pairs of Interchangeable Rectangles

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2001 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Official Link | [number-of-pairs-of-interchangeable-rectangles](https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/) |

## Problem Description & Examples
### Goal
Two rectangles are interchangeable when they have the same width-to-height ratio. Count interchangeable pairs.

### Function Contract
**Inputs**

- `rectangles`: pairs `[width, height]`.

**Return value**

Return the number of pairs with equal ratios.

### Examples
**Example 1**

- Input: `rectangles = [[4,8],[3,6],[10,20],[15,30]]`
- Output: `6`

**Example 2**

- Input: `rectangles = [[4,5],[7,8]]`
- Output: `0`

**Example 3**

- Input: `rectangles = [[1,2],[2,4],[3,6],[4,7]]`
- Output: `3`

---

## Underlying Base Algorithm(s)
Normalize each ratio by dividing width and height by their gcd, then count how many previous rectangles have the same normalized pair. Add that count to the answer before incrementing it.

---

## Complexity Analysis
- **Time Complexity**: `O(n log M)` for gcd computations.
- **Space Complexity**: `O(n)`
