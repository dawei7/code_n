# Word Ladder

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 127 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-ladder/) |

## Problem Description
### Goal
Given `begin_word`, `end_word`, and a `word_list` of unique words with the same length, create a transformation in which each step changes exactly one character. The starting word need not come from the list, but every word reached afterward—including the destination—must be one of the allowed entries.

Return the number of words in the shortest valid sequence, counting both `begin_word` and `end_word`. Thus, the answer measures sequence length rather than the number of character changes. Intermediate words may be chosen in any order supported by one-letter transitions. Return `0` when the destination is absent from the usable dictionary or no chain can reach it.

### Function Contract
**Inputs**

- `begin_word`: the first word
- `end_word`: the required final word
- `word_list`: allowed transformed words of the same length

**Return value**

The shortest sequence length including both endpoints, or `0` when no sequence exists.

### Examples
**Example 1**

- Input: `begin_word = "hit", end_word = "cog", word_list = ["hot","dot","dog","lot","log","cog"]`
- Output: `5`

**Example 2**

- Input: the same dictionary without `"cog"`
- Output: `0`

**Example 3**

- Input: `begin_word = "a", end_word = "c", word_list = ["a","b","c"]`
- Output: `2`
