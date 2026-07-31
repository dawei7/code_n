# Number of Good Binary Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2533 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-good-binary-strings/) |

## Problem Description

### Goal

You are given `minLength`, `maxLength`, `oneGroup`, and `zeroGroup`. A binary string is good when its length lies in the inclusive interval `[minLength, maxLength]`, every maximal block of consecutive `1` characters has length divisible by `oneGroup`, and every maximal block of consecutive `0` characters has length divisible by `zeroGroup`.

Count all distinct good binary strings and return the count modulo $10^9+7$. A missing block has size zero, which is considered a multiple of every positive group size; consequently, an all-zero or all-one string may be valid when its one present block meets the corresponding divisibility rule.

### Function Contract

**Inputs**

- `minLength`: The minimum permitted string length.
- `maxLength`: The maximum permitted string length.
- `oneGroup`: The divisor required for every consecutive-ones block length.
- `zeroGroup`: The divisor required for every consecutive-zeros block length.

The constraints are $1 \le \texttt{minLength} \le \texttt{maxLength} \le 10^5$ and $1 \le \texttt{oneGroup},\texttt{zeroGroup} \le \texttt{maxLength}$.

**Return value**

Return the number of good strings with permitted length, reduced modulo $10^9+7$.

### Examples

**Example 1**

- Input: `minLength = 2, maxLength = 3, oneGroup = 1, zeroGroup = 2`
- Output: `5`
- Explanation: The valid strings are `"00"`, `"11"`, `"001"`, `"100"`, and `"111"`.

**Example 2**

- Input: `minLength = 4, maxLength = 4, oneGroup = 4, zeroGroup = 3`
- Output: `1`
- Explanation: Only `"1111"` satisfies the block-size rules at length four.
