# Generate Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 22 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-parentheses/) |

## Problem Description
### Goal
Given a positive integer `n`, construct strings containing exactly `n` opening parentheses and `n` closing parentheses. A string is well formed when parentheses close in proper nesting order: no prefix may contain more closings than openings, and the final counts must balance.

Return every distinct well-formed string of length `2n` exactly once. The collection may be listed in any order. Parentheses cannot be omitted, added, or replaced, so each result represents one complete arrangement of the supplied `n` pairs.

### Function Contract
**Inputs**

- `n`: positive `int`

**Return value**

A `List[str]` containing all valid length-`2n` parenthesis strings exactly once.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `["((()))", "(()())", "(())()", "()(())", "()()()"]`

**Example 2**

- Input: `n = 1`
- Output: `["()"]`

**Example 3**

- Input: `n = 2`
- Output: `["(())", "()()"]`
