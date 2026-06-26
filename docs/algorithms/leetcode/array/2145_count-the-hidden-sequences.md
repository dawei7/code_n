# Count the Hidden Sequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2145 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [count-the-hidden-sequences](https://leetcode.com/problems/count-the-hidden-sequences/) |

## Problem Description & Examples
### Goal
Count integer sequences whose consecutive differences equal the supplied array and whose every value lies in the inclusive interval from `lower` to `upper`.

### Function Contract
**Inputs**

- `differences`: the required change between each neighboring pair.
- `lower`: the minimum permitted sequence value.
- `upper`: the maximum permitted sequence value.

**Return value**

The number of valid hidden sequences.

### Examples
**Example 1**

- Input: `differences = [1, -3, 4]`, `lower = 1`, `upper = 6`
- Output: `2`

**Example 2**

- Input: `differences = [3, -4, 5, 1, -2]`, `lower = -4`, `upper = 5`
- Output: `4`

**Example 3**

- Input: `differences = [4, -7, 2]`, `lower = 3`, `upper = 6`
- Output: `0`

---

## Underlying Base Algorithm(s)
Set the unknown first value to zero temporarily and compute all prefix offsets induced by `differences`. If their minimum and maximum are `lo` and `hi`, a true starting value `x` must satisfy both `lower - lo <= x` and `x <= upper - hi`. Count the integers in that intersection.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
