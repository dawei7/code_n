# Minimum Number of Changes to Make Binary String Beautiful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2914 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/) |

## Problem Description

### Goal

A binary string of even length is beautiful when it can be divided into one or
more contiguous substrings such that every part has even length and consists
entirely of `0` characters or entirely of `1` characters. The partition may
use parts of different even lengths, but it must cover the whole string without
reordering or omitting characters.

You may replace any character of `s` with either binary digit. Determine the
minimum number of individual character changes needed so that some valid
beautiful partition exists. A character already holding the desired digit
does not need to be changed.

### Function Contract

**Inputs**

- `s`: A binary string of even length $n$, where $2\le n\le10^5$.

**Return value**

Return the minimum number of character changes required to make `s` beautiful.

### Examples

**Example 1**

- Input: `s = "1001"`
- Output: `2`
- Explanation: Changing the result to `"1100"` permits the partition `"11|00"`.

**Example 2**

- Input: `s = "10"`
- Output: `1`
- Explanation: One character must change so that the only length-two part is uniform.

**Example 3**

- Input: `s = "0000"`
- Output: `0`
- Explanation: The whole string is already one even-length uniform part.
