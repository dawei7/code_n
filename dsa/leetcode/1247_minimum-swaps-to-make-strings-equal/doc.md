# Minimum Swaps to Make Strings Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1247 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/) |

## Problem Description

### Goal

You are given two strings `s1` and `s2` of equal length. Every character in both strings is either `"x"` or `"y"`. In one operation, choose an index `i` in `s1` and an index `j` in `s2`, then swap `s1[i]` with `s2[j]`. The two chosen indices do not need to be the same.

Return the minimum number of such swaps needed to make the two strings equal. If no sequence of cross-string swaps can make them equal, return `-1`.

### Function Contract

**Inputs**

- `s1`: a string containing only `"x"` and `"y"`.
- `s2`: a string of the same length as `s1`, also containing only `"x"` and `"y"`.
- The common length $n$ satisfies $1 \le n \le 1000$.

**Return value**

- Return the minimum number of swaps between one character of `s1` and one character of `s2` that makes the strings equal, or `-1` when this is impossible.

### Examples

**Example 1**

- Input: `s1 = "xx"`, `s2 = "yy"`
- Output: `1`
- Explanation: Swapping `s1[0]` with `s2[1]` makes both strings `"yx"`.

**Example 2**

- Input: `s1 = "xy"`, `s2 = "yx"`
- Output: `2`
- Explanation: The two mismatches have opposite orientations, so one swap cannot repair both of them.

**Example 3**

- Input: `s1 = "xx"`, `s2 = "xy"`
- Output: `-1`
- Explanation: There is an odd number of mismatched positions, so the strings cannot be made equal.
