# Sum of Unique Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1748 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [sum-of-unique-elements](https://leetcode.com/problems/sum-of-unique-elements/) |

## Problem Description & Examples
### Goal
Sum the values that appear exactly once in the array.

### Function Contract
**Inputs**

- `nums`: a list of integers.

**Return value**

Return the sum of all unique-occurring values.

### Examples
**Example 1**

- Input: `nums = [1,2,3,2]`
- Output: `4`

**Example 2**

- Input: `nums = [1,1,1,1,1]`
- Output: `0`

**Example 3**

- Input: `nums = [1,2,3,4,5]`
- Output: `15`

---

## Underlying Base Algorithm(s)
Count frequencies with a hash map or fixed-size count array. Sum only the values whose final frequency is one.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` or `O(1)` for a bounded value range
