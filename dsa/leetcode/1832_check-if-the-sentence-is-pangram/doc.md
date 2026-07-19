# Check if the Sentence Is Pangram

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/check-if-the-sentence-is-pangram/) |
| Frontend ID | 1832 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A pangram contains every letter of the English alphabet at least once. Given a string `sentence` consisting only of lowercase English letters, determine whether all 26 letters from `a` through `z` occur in it.

Repeated occurrences do not change the requirement: a letter is either present or absent. Return `true` when none of the 26 letters is missing and `false` otherwise.

### Function Contract

**Inputs**

- `sentence`: a string of $n$ lowercase English letters, where $1 \le n \le 1000$.

**Return value**

- Return `true` if every lowercase English letter appears at least once.
- Return `false` if at least one letter is absent.

### Examples

**Example 1**

- Input: `sentence = "thequickbrownfoxjumpsoverthelazydog"`
- Output: `true`

Every letter occurs at least once, although several letters repeat.

**Example 2**

- Input: `sentence = "leetcode"`
- Output: `false`

Only a subset of the alphabet occurs.

**Example 3**

- Input: `sentence = "abcdefghijklmnopqrstuvwxyz"`
- Output: `true`

Each of the 26 letters appears exactly once.
