# Number of Valid Words for Each Puzzle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1178 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/) |

## Problem Description

### Goal

You are given a list of lowercase `words` and a list of seven-letter `puzzles`. A word is valid for a puzzle only when it satisfies both rules: the word contains the puzzle's first letter, and every letter occurring in the word also occurs somewhere in the puzzle. Repeated occurrences of a letter do not require separate puzzle entries.

For each puzzle independently, count how many entries in `words` are valid for it. Return the counts in the same order as `puzzles`; repeated word entries, if present, contribute separately.

### Function Contract

**Inputs**

- `words`: Between $1$ and $10^5$ lowercase English strings, each with length from $4$ through $50$.
- `puzzles`: Between $1$ and $10^4$ lowercase English strings. Every puzzle has exactly seven distinct letters, and its character at index `0` is the required letter.
- Define

$$
W=\sum_{w\in\texttt{words}} \lvert w\rvert.
$$

- Let $p=\lvert\texttt{puzzles}\rvert$ and let $u$ be the number of distinct word-letter masks containing at most seven letters.

**Return value**

- A length-$p$ integer array where entry $i$ is the number of words whose letters are all contained in `puzzles[i]` and that contain `puzzles[i][0]`.

### Examples

**Example 1**

- Input: `words = ["aaaa","asas","able","ability","actt","actor","access"]`, `puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]`
- Output: `[1,1,3,2,4,0]`

For `"actresz"`, the valid words are `"aaaa"`, `"actt"`, `"actor"`, and `"access"`.

**Example 2**

- Input: `words = ["apple","pleas","please"]`, `puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]`
- Output: `[0,1,3,2,0]`

**Example 3**

- Input: `words = ["aaaa","bbbb","abab"]`, `puzzles = ["abcdefg","bcdefgh"]`
- Output: `[2,1]`
