# Valid Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 20 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-parentheses/) |

## Problem Description
### Goal
Given a nonempty string containing only parentheses `()`, square brackets `[]`, and braces `{}`, decide whether it forms a valid bracket sequence. Every opening bracket must eventually be closed by the matching type.

Closures must also respect nesting order: the most recently opened unmatched bracket must be the next one closed. A closing bracket cannot appear without a corresponding opener, and no opener may remain unmatched after the entire string is consumed. Return a boolean indicating whether all of these conditions hold.

### Function Contract
**Inputs**

- `s`: non-empty `str` containing `()[]{}`

**Return value**

`True` when the complete bracket sequence is valid; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "()"`
- Output: `True`

**Example 2**

- Input: `s = "()[]{}"`
- Output: `True`

**Example 3**

- Input: `s = "(]"`
- Output: `False`
