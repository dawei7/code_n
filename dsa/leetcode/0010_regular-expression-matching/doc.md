# Regular Expression Matching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 10 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/regular-expression-matching/) |

## Problem Description
### Goal
You are given a text string `s` and a pattern `p` using lowercase letters plus two special symbols. A dot `.` matches exactly one arbitrary character. An asterisk `*` modifies the immediately preceding letter or dot and allows that element to appear zero or more consecutive times.

Decide whether the pattern can match the entire text from beginning to end. Matching only a prefix or internal substring is not sufficient. An asterisk may eliminate its preceding element completely, so patterns can match an empty text, and several starred elements may interact; no other regular-expression operators have special meaning.

### Function Contract
**Inputs**

- `s`: `str`
- `p`: valid `str` pattern using lowercase letters, `.` and `*`

**Return value**

`True` when `p` matches the complete string; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "aa", p = "a"`
- Output: `False`

**Example 2**

- Input: `s = "aa", p = "a*"`
- Output: `True`

**Example 3**

- Input: `s = "ab", p = ".*"`
- Output: `True`
