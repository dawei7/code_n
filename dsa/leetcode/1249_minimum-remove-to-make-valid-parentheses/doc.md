# Minimum Remove to Make Valid Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1249 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) |

## Problem Description

### Goal

You are given a string `s` containing lowercase English letters together with the parentheses `"("` and `")"`. Remove the minimum number of parentheses needed to make the resulting parentheses valid, and return any valid string obtainable with that minimum number of removals. Letters cannot be removed.

A parentheses string is valid if it is empty, contains only lowercase letters, is the concatenation of two valid strings, or has the form `"(" + A + ")"` for a valid string `A`. The returned string therefore needs balanced, correctly ordered parentheses while retaining every original letter in order.

### Function Contract

**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 10^5$, containing lowercase English letters and parentheses.

**Return value**

- Return any valid string formed by removing the minimum possible number of parentheses from `s`.

### Examples

**Example 1**

- Input: `s = "lee(t(c)o)de)"`
- Output: `"lee(t(c)o)de"`

**Example 2**

- Input: `s = "a)b(c)d"`
- Output: `"ab(c)d"`

**Example 3**

- Input: `s = "))(("`
- Output: `""`
