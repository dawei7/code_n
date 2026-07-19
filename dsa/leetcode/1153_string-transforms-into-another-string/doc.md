# String Transforms Into Another String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1153 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/string-transforms-into-another-string/) |

## Problem Description

### Goal

You are given two strings, `str1` and `str2`, with the same length. Determine whether zero or more conversions can transform `str1` into `str2`.

In one conversion, choose one lowercase English character currently present in `str1` and replace all of its occurrences with any other lowercase English character. Each operation is global: it changes every current occurrence of the chosen character at once, and later conversions operate on the string produced so far. Return `true` if and only if some sequence of conversions reaches `str2`; the order of conversions can affect whether the transformation succeeds.

### Function Contract

**Inputs**

- `str1`: The starting string of length $n$, containing only lowercase English letters.
- `str2`: The target string of the same length, also containing only lowercase English letters.

The shared length satisfies $1 \le n \le 10^4$.

**Return value**

- `true` when `str1` can be transformed into `str2` by the allowed global conversions; otherwise, `false`.

### Examples

**Example 1**

- Input: `str1 = "aabcc"`, `str2 = "ccdee"`
- Output: `true`

The conversion order can be `c` to `e`, then `b` to `d`, and finally `a` to `c`.

**Example 2**

- Input: `str1 = "leetcode"`, `str2 = "codeleet"`
- Output: `false`

**Example 3**

- Input: `str1 = "abcdefghijklmnopqrstuvwxyz"`, `str2 = "bcdefghijklmnopqrstuvwxyza"`
- Output: `false`
