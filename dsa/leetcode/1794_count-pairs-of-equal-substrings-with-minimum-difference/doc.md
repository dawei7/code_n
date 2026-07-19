# Count Pairs of Equal Substrings With Minimum Difference

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/) |
| Frontend ID | 1794 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given two 0-indexed strings `firstString` and `secondString`, both containing only lowercase English letters. Consider every index quadruple $(i,j,a,b)$ satisfying

$$
0 \le i \le j < \lvert\texttt{firstString}\rvert
\quad\text{and}\quad
0 \le a \le b < \lvert\texttt{secondString}\rvert.
$$

The quadruple is eligible when the inclusive substring `firstString[i:j + 1]` equals `secondString[a:b + 1]`. Among all eligible quadruples, find the minimum possible value of $j-a$.

Return how many eligible quadruples attain that global minimum. If the two strings have no equal nonempty substrings, return zero.

### Function Contract

**Inputs**

- `firstString`: a lowercase English string of length $n$, where $1 \le n \le 2\cdot 10^5$.
- `secondString`: a lowercase English string of length $m$, where $1 \le m \le 2\cdot 10^5$.

**Return value**

- Return the number of equal-substring quadruples whose value $j-a$ is minimum over every eligible quadruple.

### Examples

**Example 1**

- Input: `firstString = "abcd", secondString = "bccda"`
- Output: `1`

The singleton match `(i, j, a, b) = (0, 0, 4, 4)` is the unique quadruple with minimum difference.

**Example 2**

- Input: `firstString = "ab", secondString = "cd"`
- Output: `0`

The strings share no character, so no equal nonempty substrings exist.

**Example 3**

- Input: `firstString = "abc", secondString = "abc"`
- Output: `3`

The three same-position singleton matches all have difference zero; longer equal substrings have a larger value.
