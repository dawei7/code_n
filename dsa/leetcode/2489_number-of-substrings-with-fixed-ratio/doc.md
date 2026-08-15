# Number of Substrings With Fixed Ratio

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2489 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Math, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/) |

## Problem Description

### Goal

Given a binary string `s` and two coprime positive integers `num1` and `num2`, count its nonempty substrings in which the number of `0` characters and the number of `1` characters have the exact ratio `num1 : num2`.

A substring must occupy one contiguous interval of `s`. The counts may be any common positive multiple of `num1` and `num2`; for example, a ratio of $2:4$ also satisfies a requested ratio of $1:2$. Return the total number of qualifying intervals, including overlapping intervals when their endpoints differ.

### Function Contract

**Inputs**

- `s`: A nonempty string containing only `0` and `1`.
- `num1`: The required relative count of zeros.
- `num2`: The required relative count of ones.

Let $n = \lvert\texttt{s}\rvert$. The constraints satisfy $1 \le n \le 10^5$, $1 \le \texttt{num1},\texttt{num2} \le n$, and $\gcd(\texttt{num1},\texttt{num2})=1$.

**Return value**

Return the number of nonempty contiguous substrings whose zero count divided by their one count is exactly `num1 / num2`.

### Examples

#### Example 1

- **Input:** `s = "0110011", num1 = 1, num2 = 2`
- **Output:** `4`
- **Explanation:** Three length-three intervals contain one zero and two ones, and one length-six interval contains two zeros and four ones.

#### Example 2

- **Input:** `s = "10101", num1 = 3, num2 = 1`
- **Output:** `0`
- **Explanation:** No contiguous interval contains zeros and ones in the requested proportion.
