# Ways to Make a Fair Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1664 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [ways-to-make-a-fair-array](https://leetcode.com/problems/ways-to-make-a-fair-array/) |

## Problem Description & Examples
### Goal
Given an integer array, count how many indices can be removed so that the remaining array has the same sum at even positions and odd positions. After removal, all elements to the right shift left by one position.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return the number of removable indices that make the resulting array fair.

### Examples
**Example 1**

- Input: `nums = [2,1,6,4]`
- Output: `1`

**Example 2**

- Input: `nums = [1,1,1]`
- Output: `3`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Use prefix-style running sums. First compute the total sum at even and odd indices. Then scan each index as the removed element, maintaining sums already seen on the left. Elements on the right change parity after the removal, so the new even sum is `left_even + right_odd`, and the new odd sum is `left_odd + right_even`. Count indices where those two values match.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
