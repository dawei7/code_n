# First Letter to Appear Twice

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2351 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/first-letter-to-appear-twice/) |

## Problem Description

### Goal

Given a string `s` made only of lowercase English letters, identify the first
letter whose second occurrence is encountered while reading the string from
left to right. In other words, compare repeated letters by the positions of
their second appearances, not by where their first appearances occur.

Return that letter as a one-character string. The input is guaranteed to
contain at least one repeated letter, so a valid answer always exists. A
letter may occur more than twice, but only its second appearance matters when
determining which repeated letter comes first.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters with
  $2 \le \lvert\texttt{s}\rvert \le 100$.

At least one letter occurs more than once.

**Return value**

The letter whose second occurrence has the smallest index.

### Examples

**Example 1**

- Input: `s = "abccbaacz"`
- Output: `"c"`
- Explanation: The second `c` appears at index 3, before the second
  appearances of `b` and `a`.

**Example 2**

- Input: `s = "abcdd"`
- Output: `"d"`
- Explanation: `d` is the only repeated letter.

**Example 3**

- Input: `s = "bacab"`
- Output: `"a"`
- Explanation: Although `b` appears first, the second `a` occurs before the
  second `b`.
