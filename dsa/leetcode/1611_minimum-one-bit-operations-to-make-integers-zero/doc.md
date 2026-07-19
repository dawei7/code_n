# Minimum One Bit Operations to Make Integers Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1611 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Bit Manipulation, Recursion, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/) |

## Problem Description
### Goal
Transform the non-negative integer `n` into zero by changing one bit per operation. The rightmost bit, at index 0, may always be flipped.

For any index $i>0$, bit $i$ may be flipped only when bit $i-1$ is 1 and every lower bit from $i-2$ through 0 is 0. Apply either legal operation as often as needed and return the minimum number of operations required to reach zero.

### Function Contract
**Inputs**

- `n`: an integer satisfying $0 \le n \le 10^9$.

**Return value**

Return the minimum number of legal single-bit changes that transform `n` into 0.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `2`
- Explanation: Binary `11` can flip its second bit to become `01`, then flip the rightmost bit to reach `00`.

**Example 2**

- Input: `n = 6`
- Output: `4`
- Explanation: One shortest sequence is `110 -> 010 -> 011 -> 001 -> 000`.

**Example 3**

- Input: `n = 0`
- Output: `0`
