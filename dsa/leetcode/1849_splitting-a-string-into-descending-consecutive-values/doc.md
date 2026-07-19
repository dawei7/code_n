# Splitting a String Into Descending Consecutive Values

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/) |
| Frontend ID | 1849 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given a string `s` containing only decimal digits. Split the entire string into at least two non-empty contiguous substrings. Interpret each substring as an integer; leading zeros are permitted and do not affect that numerical value.

The split is valid only when its values form a descending consecutive sequence: every value after the first must be exactly one less than the value immediately before it. Return whether any placement of split boundaries satisfies all of these conditions.

### Function Contract

**Inputs**

- `s`: a digit string with $1 \le \lvert\texttt{s}\rvert \le 20$.
- A substring such as `"0090"` has numerical value 90.
- Let $n=\lvert\texttt{s}\rvert$.

**Return value**

- Return `true` if all characters can be divided into at least two non-empty substrings with values $v_1,v_2,\ldots,v_k$ such that $k\ge 2$ and $v_{i+1}=v_i-1$ for every $1\le i<k$.
- Return `false` if no such complete split exists.

### Examples

**Example 1**

- Input: `s = "1234"`
- Output: `false`

No placement of boundaries produces the required descending consecutive values.

**Example 2**

- Input: `s = "050043"`
- Output: `true`

The substrings `"05"`, `"004"`, and `"3"` have values 5, 4, and 3.

**Example 3**

- Input: `s = "9080701"`
- Output: `false`
