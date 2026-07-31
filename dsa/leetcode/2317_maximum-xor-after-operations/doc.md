# Maximum XOR After Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2317 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-xor-after-operations/) |

## Problem Description
### Goal
Start with the non-negative integers in `nums`. One operation chooses an index
`i` and any non-negative integer `x`, then replaces `nums[i]` with
`nums[i] AND (nums[i] XOR x)`. The operation may be applied any number of
times, including zero times, and each application may choose a different index
and value of `x`.

After all chosen operations, take the bitwise XOR of every array element.
Determine the greatest XOR value that can be achieved. Operations can remove
set bits from an element but cannot introduce a bit that was absent from that
element, so the answer depends on which bit positions occur anywhere in the
original array.

### Function Contract
**Inputs**

- `nums`: A nonempty array of integers from $0$ through $10^8$.

The array length is from 1 through $10^5$.

**Return value**

The maximum possible bitwise XOR of all elements after any number of allowed
updates.

### Examples
**Example 1**

- Input: `nums = [3,2,4,6]`
- Output: `7`
- Explanation: Clearing the value-four bit from the final element permits the
  total XOR to contain all three low bits.

**Example 2**

- Input: `nums = [1,2,3,9,2]`
- Output: `11`
- Explanation: Applying no operation already produces the maximum.
