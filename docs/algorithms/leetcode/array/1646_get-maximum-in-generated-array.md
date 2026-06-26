# Get Maximum in Generated Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1646 |
| Difficulty | Easy |
| Topics | Array, Simulation |
| Official Link | [get-maximum-in-generated-array](https://leetcode.com/problems/get-maximum-in-generated-array/) |

## Problem Description & Examples
### Goal
Generate the array defined by the recurrence up to index `n` and return its
maximum value.

### Function Contract
**Inputs**

- `n`: the final index to generate.

**Return value**

The largest value in the generated array.

### Examples
**Example 1**

- Input: `n = 7`
- Output: `3`

**Example 2**

- Input: `n = 2`
- Output: `1`

**Example 3**

- Input: `n = 3`
- Output: `2`

---

## Underlying Base Algorithm(s)
Build the array directly. Set `nums[0] = 0` and `nums[1] = 1` when present.
For each index `i`, fill `2 * i` from `nums[i]` and `2 * i + 1` from
`nums[i] + nums[i + 1]` when those indices are within bounds. Track the maximum
as values are written.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`.
- **Space Complexity**: `O(n)`.
