# Maximum 69 Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1323 |
| Difficulty | Easy |
| Topics | Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-69-number/) |

## Problem Description
### Goal
Given a positive integer `num` whose decimal representation contains only the digits `6` and `9`, produce the largest possible integer after changing at most one digit.

The optional change reverses one selected digit: a `6` becomes `9`, or a `9` becomes `6`. It is also valid to leave the number unchanged, so a change should be made only when it increases the result.

### Function Contract
**Inputs**

- `num`: an integer with $1\le\texttt{num}\le10^4$ whose $d$ decimal digits are all `6` or `9`; consequently $1\le d\le4$.

**Return value**

The maximum integer obtainable by applying the permitted digit reversal zero or one time.

### Examples
**Example 1**

- Input: `num = 9669`
- Output: `9969`
- Explanation: Changing the leftmost `6` produces the greatest increase.

**Example 2**

- Input: `num = 9996`
- Output: `9999`
- Explanation: The final digit is the only `6`, so changing it is optimal.

**Example 3**

- Input: `num = 9999`
- Output: `9999`
- Explanation: Every permitted change would decrease the number, so no digit is changed.
