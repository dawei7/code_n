# Maximum XOR for Each Query

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1829 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Prefix Sum |
| Official Link | [maximum-xor-for-each-query](https://leetcode.com/problems/maximum-xor-for-each-query/) |

## Problem Description & Examples
### Goal
For each query, choose a number `k` less than `2^maximumBit` that maximizes the XOR of `k` with the XOR of the current array. After answering, remove the last array element and continue.

### Function Contract
**Inputs**

- `nums`: the starting array.
- `maximumBit`: the bit width limiting each answer.

**Return value**

Return the best `k` for every removal step.

### Examples
**Example 1**

- Input: `nums = [0,1,1,3], maximumBit = 2`
- Output: `[0,3,2,3]`

**Example 2**

- Input: `nums = [2,3,4,7], maximumBit = 3`
- Output: `[5,2,6,5]`

**Example 3**

- Input: `nums = [0,1,2,2,5,7], maximumBit = 3`
- Output: `[4,3,6,4,6,7]`

---

## Underlying Base Algorithm(s)
Compute the XOR of all current elements. The value less than `2^maximumBit` that maximizes XOR is the bitwise complement of that XOR within the `maximumBit` mask. Append `mask XOR current_xor`, then remove the last element by XORing it out.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)` besides the output array
