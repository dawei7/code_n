# Convert to Base -2

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1017 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/convert-to-base-2/) |

## Problem Description

### Goal

You are given a nonnegative integer `n`. Return a binary string representing the same value in base $-2$, using only the digits `0` and `1`.

If the returned digits from right to left are $d_0,d_1,\ldots,d_{B-1}$, they must satisfy

$$
n=\sum_{i=0}^{B-1}d_i(-2)^i.
$$

The representation must not contain leading zeroes unless `n == 0`, whose representation is exactly `"0"`.

### Function Contract

**Inputs**

- `n`: an integer satisfying $0\le n\le10^9$.

Let $B$ denote the number of digits in the returned base-$-2$ string.

**Return value**

- The unique base-$-2$ representation of `n` using digits `0` and `1` without unnecessary leading zeroes.

### Examples

**Example 1**

- Input: `n = 2`
- Output: `"110"`
- Explanation: $(-2)^2+(-2)^1=2$.

**Example 2**

- Input: `n = 3`
- Output: `"111"`
- Explanation: $(-2)^2+(-2)^1+(-2)^0=3$.

**Example 3**

- Input: `n = 4`
- Output: `"100"`
- Explanation: $(-2)^2=4$.
