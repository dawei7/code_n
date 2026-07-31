# Sum of Number and Its Reverse

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2443 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Sum of Number and Its Reverse](https://leetcode.com/problems/sum-of-number-and-its-reverse/) |

## Problem Description

### Goal

You are given a non-negative integer `num`. Determine whether there is some non-negative integer $x$ such that adding $x$ to the integer obtained by reversing the decimal digits of $x$ produces exactly `num`.

The reversed digit sequence is interpreted as an integer, so any leading zeros disappear; for example, reversing 140 yields `041`, which has value 41. Return `true` when at least one suitable $x$ exists and `false` otherwise.

### Function Contract

**Inputs**

- `num`: A non-negative integer with $0 \le \texttt{num} \le 10^5$.

**Return value**

- `true` if some non-negative integer plus its digit reversal equals `num`; otherwise `false`.

### Examples

**Example 1**

- Input: `num = 443`
- Output: `true`
- Explanation: `172 + 271 = 443`.

**Example 2**

- Input: `num = 63`
- Output: `false`
- Explanation: No non-negative integer has the required sum with its reversal.

**Example 3**

- Input: `num = 181`
- Output: `true`
- Explanation: Reversing 140 gives integer 41, and `140 + 41 = 181`.
