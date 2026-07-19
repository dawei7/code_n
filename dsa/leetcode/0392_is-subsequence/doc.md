# Is Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 392 |
| Difficulty | Easy |
| Topics | Two Pointers, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/is-subsequence/) |

## Problem Description
### Goal
Given strings `s` and `t`, decide whether `s` is a subsequence of `t`. You may delete any number of characters from `t`, but the characters retained to form `s` must keep their original relative order.

Return `True` when every character of `s` can be matched from left to right within `t`, not necessarily at adjacent positions. Repeated characters require separate later occurrences, and the matching indices cannot move backward. The empty string is a subsequence of every string, while a nonempty `s` cannot be a subsequence of an empty or too-short `t`.

### Function Contract
**Inputs**

- `s`: the candidate subsequence
- `t`: the source string whose relative character order must be preserved

**Return value**

- Return `True` when every character of `s` can be matched in order within `t`; otherwise return `False`.

### Examples
**Example 1**

- Input: `s = "abc", t = "ahbgdc"`
- Output: `True`

**Example 2**

- Input: `s = "axc", t = "ahbgdc"`
- Output: `False`

**Example 3**

- Input: `s = "", t = "anything"`
- Output: `True`
