# Decrease Elements To Make Array Zigzag

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1144 |
| Difficulty | Medium |
| Topics | Array, Greedy |
| Official Link | [decrease-elements-to-make-array-zigzag](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/) |

## Problem Description & Examples
### Goal
Decrease array elements by one per operation until the array alternates between valleys and peaks. Return the fewest operations needed.

### Function Contract
**Inputs**

- `nums`: integer array.

**Return value**

The minimum number of decrement operations needed so that either all even indices are valleys or all odd indices are valleys.

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `2`

**Example 2**

- Input: `nums = [9,6,1,6,2]`
- Output: `4`

**Example 3**

- Input: `nums = [2,1,2]`
- Output: `0`

---

## Underlying Base Algorithm(s)
Greedy local adjustment.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
