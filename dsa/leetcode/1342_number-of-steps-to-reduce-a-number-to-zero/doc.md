# Number of Steps to Reduce a Number to Zero

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1342 |
| Difficulty | Easy |
| Topics | Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/) |

## Problem Description
### Goal
Starting from the non-negative integer `num`, repeatedly apply the operation required by its current parity. When the value is even and positive, divide it by 2. When it is odd, subtract 1.

Return the number of operations performed when the value first reaches zero. The rule is deterministic—there is no choice between the two operations—and an input already equal to zero requires no steps.

### Function Contract
**Inputs**

- `num`: an integer satisfying $0\le\texttt{num}\le10^6$.

**Return value**

The number of mandated divide-or-subtract steps needed to transform `num` into zero.

### Examples
**Example 1**

- Input: `num = 14`
- Output: `6`
- Explanation: The sequence is `14 -> 7 -> 6 -> 3 -> 2 -> 1 -> 0`.

**Example 2**

- Input: `num = 8`
- Output: `4`

**Example 3**

- Input: `num = 123`
- Output: `12`
