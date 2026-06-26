# Count Elements With Strictly Smaller and Greater Elements 

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2148 |
| Difficulty | Easy |
| Topics | Array, Sorting, Counting |
| Official Link | [count-elements-with-strictly-smaller-and-greater-elements](https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/) |

## Problem Description & Examples
### Goal
Count array elements for which the array contains both a strictly smaller value and a strictly greater value.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The number of qualifying element occurrences.

### Examples
**Example 1**

- Input: `nums = [11, 7, 2, 15]`
- Output: `2`

**Example 2**

- Input: `nums = [-3, 3, 3, 90]`
- Output: `2`

**Example 3**

- Input: `nums = [3, 3, 3]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Find the global minimum and maximum. Exactly the occurrences unequal to both extrema qualify, so count values strictly between them. If the minimum equals the maximum, none qualify.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
