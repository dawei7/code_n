# Minimum Changes To Make Alternating Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1758 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/) |

## Problem Description

### Goal

You are given a binary string `s`. In one operation, choose any position and change its character from `"0"` to `"1"` or from `"1"` to `"0"`.

A binary string is alternating when every pair of adjacent characters differs. Determine the minimum number of operations required to transform `s` into an alternating string of the same length, and return that minimum.

### Function Contract

**Inputs**

- `s`: a string containing only `"0"` and `"1"`, with $1 \le n \le 10^4$, where $n=\lvert s\rvert$.

**Return value**

- Return the minimum number of single-character changes needed so that `s[i] != s[i + 1]` for every valid adjacent pair.

### Examples

**Example 1**

- Input: `s = "0100"`
- Output: `1`
- Explanation: Changing the final character produces `"0101"`.

**Example 2**

- Input: `s = "10"`
- Output: `0`
- Explanation: The two existing adjacent characters already differ.

**Example 3**

- Input: `s = "1111"`
- Output: `2`
- Explanation: Either `"0101"` or `"1010"` can be reached with two changes.
