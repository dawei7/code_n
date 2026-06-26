# Height Checker

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1051 |
| Difficulty | Easy |
| Topics | Array, Sorting, Counting Sort |
| Official Link | [height-checker](https://leetcode.com/problems/height-checker/) |

## Problem Description & Examples
### Goal
Students are currently listed by height. Count how many positions differ from the nondecreasing height order.

### Function Contract
**Inputs**

- `heights`: List[int]

**Return value**

int - number of mismatched positions

### Examples
**Example 1**

- Input: `heights = [1, 1, 4, 2, 1, 3]`
- Output: `3`

**Example 2**

- Input: `heights = [5, 1, 2, 3, 4]`
- Output: `5`

**Example 3**

- Input: `heights = [1, 2, 3, 4, 5]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Sorting comparison.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
