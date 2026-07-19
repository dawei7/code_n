# Integer Replacement

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 397 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Greedy, Bit Manipulation, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/integer-replacement/) |

## Problem Description
### Goal
Starting from a positive integer `n`, repeatedly apply one legal operation. If the current value is even, replace it with half its value. If it is odd, replace it with either one less or one greater.

Return the minimum number of operations needed to reach exactly `1`. Choices at odd values affect later divisibility, so always decrementing or always incrementing is not necessarily optimal. The starting value `1` needs zero operations. Handle the largest signed input safely, since temporarily incrementing an odd value can exceed its original fixed-width range even though the mathematical process remains valid.

### Function Contract
**Inputs**

- `n`: the positive starting integer

**Return value**

- Return the minimum number of allowed operations needed to reach `1`.

### Examples
**Example 1**

- Input: `n = 8`
- Output: `3`

**Example 2**

- Input: `n = 7`
- Output: `4`

**Example 3**

- Input: `n = 4`
- Output: `2`
