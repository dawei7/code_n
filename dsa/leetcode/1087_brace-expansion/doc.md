# Brace Expansion

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1087 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Stack, Breadth-First Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/brace-expansion/) |

## Problem Description

### Goal

The string `s` describes words using lowercase letters and brace groups. A lowercase letter outside braces is fixed in that position. A group such as `"{a,b,c}"` contributes exactly one of its comma-separated single-letter alternatives. Braces are not nested, and the expression is valid.

Form every word obtained by independently choosing one letter from each brace group while retaining every fixed letter. Return all expanded words in lexicographic order. Each output has one character for every fixed position or brace group in the expression.

### Function Contract

**Inputs**

- `s`: a valid, non-nested brace expression of length $n$ containing lowercase fixed letters and comma-separated single-letter alternatives.

Let $L$ be the number of output positions after treating each brace group as one position, and let $R$ be the number of expanded words.

**Return value**

- A lexicographically sorted list containing all $R$ expansions, each of length $L$.

### Examples

**Example 1**

- Input: `s = "{a,b}c{d,e}f"`
- Output: `["acdf", "acef", "bcdf", "bcef"]`

**Example 2**

- Input: `s = "abcd"`
- Output: `["abcd"]`
