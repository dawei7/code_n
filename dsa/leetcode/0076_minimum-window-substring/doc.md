# Minimum Window Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 76 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-window-substring/) |

## Problem Description
### Goal
You are given a source string `s` and a nonempty pattern string `t`. Find a contiguous window of `s` containing every character required by `t`, with at least the same multiplicity; repeated pattern characters therefore require repeated occurrences inside the window.

Return the minimum window substring covering all characters of `t`. The provided inputs guarantee that the answer is unique. When `s` lacks enough of any required character, return the empty string. Characters not present in `t` may occur inside a valid window.

### Function Contract
**Inputs**

- `s`: the source string
- `t`: the nonempty multiset pattern string

**Return value**

The unique minimum covering substring, or `""` when no cover exists.

### Examples
**Example 1**

- Input: `s = "ADOBECODEBANC", t = "ABC"`
- Output: `"BANC"`

**Example 2**

- Input: `s = "a", t = "a"`
- Output: `"a"`

**Example 3**

- Input: `s = "a", t = "aa"`
- Output: `""`
