# Count Palindromic Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2484 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-palindromic-subsequences/) |

## Problem Description

### Goal

Given a string `s` made only of decimal digits, count its palindromic subsequences whose length is exactly five. A subsequence chooses indices in increasing order and may omit any characters between them; different choices of indices count separately even when they produce the same digit string.

A palindrome reads identically from left to right and from right to left. Because the number of valid index selections can be large, return the count modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `s`: A string containing only the digits `"0"` through `"9"`.

Let $n = \lvert\texttt{s}\rvert$. The constraints satisfy $1 \le n \le 10^4$.

**Return value**

Return the number of index tuples

$$
0 \le i_1 < i_2 < i_3 < i_4 < i_5 < n
$$

for which `s[i1] = s[i5]` and `s[i2] = s[i4]`, reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `s = "103301"`
- Output: `2`
- Explanation: Two distinct selections of indices produce the palindrome `"10301"`.

**Example 2**

- Input: `s = "0000000"`
- Output: `21`
- Explanation: Every choice of five among the seven positions forms `"00000"`, giving $\binom{7}{5} = 21$.

**Example 3**

- Input: `s = "9999900000"`
- Output: `2`
- Explanation: Exactly one selection forms `"99999"` and one forms `"00000"`.
