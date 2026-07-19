# Repeated String Match

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 686 |
| Difficulty | Medium |
| Topics | String, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/repeated-string-match/) |

## Problem Description
### Goal
Given strings `a` and `b`, repeat `a` by concatenating copies of it end to end. One repetition is `a`, two repetitions are $a + a$, and so on.

Return the minimum number of repetitions needed for `b` to occur as a contiguous substring of the repeated string. A match may cross one or more boundaries between copies of `a`. If no number of repetitions can ever contain `b`, return `-1`.

### Function Contract
**Inputs**

- `a`: a nonempty source string to repeat
- `b`: a nonempty target string to locate

**Return value**

- The minimum positive repeat count making `b` a substring, or `-1` if impossible

### Examples
**Example 1**

- Input: `a = "abcd", b = "cdabcdab"`
- Output: `3`

**Example 2**

- Input: `a = "a", b = "aa"`
- Output: `2`

**Example 3**

- Input: `a = "abc", b = "wxyz"`
- Output: `-1`
