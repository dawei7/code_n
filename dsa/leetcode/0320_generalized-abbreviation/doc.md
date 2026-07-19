# Generalized Abbreviation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 320 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/generalized-abbreviation/) |

## Problem Description
### Goal
Given a word, form generalized abbreviations by choosing any character positions to abbreviate. Each maximal consecutive run of abbreviated characters is replaced by its decimal length, while every unabbreviated character remains visible in its original order.

Return every distinct abbreviation exactly once, in any order. Adjacent abbreviated positions must be represented by one combined count rather than separate neighboring numbers, and choosing no positions returns the original word. Choosing all positions returns its length for a nonempty word. The generated text must account for every source character exactly once, either literally or inside one run count.

### Function Contract
**Inputs**

- `word`: the source string

**Return value**

A list containing every distinct generalized abbreviation of `word` exactly once, in any order.

### Examples
**Example 1**

- Input: `word = "word"`
- Output: `["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]`

**Example 2**

- Input: `word = "a"`
- Output: `["1","a"]`

**Example 3**

- Input: `word = "ab"`
- Output: `["2","1b","a1","ab"]`
