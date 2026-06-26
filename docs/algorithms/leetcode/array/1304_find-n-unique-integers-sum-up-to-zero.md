# Find N Unique Integers Sum up to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1304 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [find-n-unique-integers-sum-up-to-zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/) |

## Problem Description & Examples
### Goal
Return any `n` distinct integers whose sum is zero.

### Function Contract
**Inputs**

- `n`: number of integers to return.

**Return value**

A list of `n` unique integers with total sum `0`.

### Examples
**Example 1**

- Input: `n = 5`
- Output: `[-2,-1,0,1,2]`

**Example 2**

- Input: `n = 3`
- Output: `[-1,0,1]`

**Example 3**

- Input: `n = 4`
- Output: `[-2,-1,1,2]`

---

## Underlying Base Algorithm(s)
Symmetric pair construction.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` for the output.
