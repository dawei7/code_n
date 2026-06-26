# Successful Pairs of Spells and Potions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2300 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Official Link | [successful-pairs-of-spells-and-potions](https://leetcode.com/problems/successful-pairs-of-spells-and-potions/) |

## Problem Description & Examples
### Goal
For each spell, count potions whose product with that spell is at least `success`.

### Function Contract
**Inputs**

- `spells`: positive spell strengths.
- `potions`: positive potion strengths.
- `success`: the minimum successful product.

**Return value**

One successful-potion count for each spell in its original order.

### Examples
**Example 1**

- Input: `spells = [5, 1, 3]`, `potions = [1, 2, 3, 4, 5]`, `success = 7`
- Output: `[4, 0, 3]`

**Example 2**

- Input: `spells = [3, 1, 2]`, `potions = [8, 5, 8]`, `success = 16`
- Output: `[2, 0, 2]`

**Example 3**

- Input: `spells = [10]`, `potions = [1, 2]`, `success = 10`
- Output: `[2]`

---

## Underlying Base Algorithm(s)
Sort potions. For spell `s`, binary-search the first potion at least `ceil(success / s)`; every potion from that position onward succeeds. Subtract the insertion index from the potion count.

---

## Complexity Analysis
- **Time Complexity**: `O(m log m + n log m)`
- **Space Complexity**: `O(1)` auxiliary space when sorting potions in place
