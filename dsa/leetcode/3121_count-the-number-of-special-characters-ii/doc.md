# Count the Number of Special Characters II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3121 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-special-characters-ii/) |

## Problem Description

### Goal

You are given a string `word` containing only lowercase and uppercase English letters. A letter is special only if both of its cases occur in the string and every lowercase occurrence of that letter appears before its first uppercase occurrence.

Return the number of distinct special letters. The ordering condition applies separately to each letter: uppercase repetitions after the transition are allowed, but an uppercase occurrence before any lowercase occurrence or a lowercase occurrence after the first uppercase makes that letter ineligible.

### Function Contract

**Inputs**

- `word`: A string of lowercase and uppercase English letters.

Its length $n$ satisfies $1 \le n \le 2\cdot 10^5$.

**Return value**

Return the number of distinct letters that occur in both cases and have all lowercase occurrences before their first uppercase occurrence.

### Examples

**Example 1**

- Input: `word = "aaAbcBC"`
- Output: `3`
- Explanation: For `a`, `b`, and `c`, every lowercase occurrence precedes the first uppercase occurrence.

**Example 2**

- Input: `word = "abc"`
- Output: `0`
- Explanation: No letter has an uppercase occurrence.

**Example 3**

- Input: `word = "AbBCab"`
- Output: `0`
- Explanation: `a` begins with uppercase, and `b` has a lowercase occurrence after its first uppercase occurrence.
