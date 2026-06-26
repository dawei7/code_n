# Maximum XOR After Operations 

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2317 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation |
| Official Link | [maximum-xor-after-operations](https://leetcode.com/problems/maximum-xor-after-operations/) |

## Problem Description & Examples
### Goal
An operation may replace one array value `x` with `x AND (x XOR y)` for any nonnegative `y`, and may be repeated. Maximize the bitwise XOR of all final values.

### Function Contract
**Inputs**

- `nums`: a list of nonnegative integers.

**Return value**

The maximum achievable XOR.

### Examples
**Example 1**

- Input: `nums = [3, 2, 4, 6]`
- Output: `7`

**Example 2**

- Input: `nums = [1, 2, 3, 9, 2]`
- Output: `11`

**Example 3**

- Input: `nums = [8]`
- Output: `8`

---

## Underlying Base Algorithm(s)
The operation can clear any chosen set bit of a value but cannot create a bit absent from it. For each bit present in at least one input value, retain that bit in exactly one final value and clear it from the others, making it appear in the XOR. Therefore the maximum equals the bitwise OR of all inputs.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`
