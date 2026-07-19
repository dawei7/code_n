# Reorganize String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 767 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Sorting, Heap (Priority Queue), Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reorganize-string/) |

## Problem Description

### Goal

Given a lowercase string `s`, rearrange all of its characters so that no two adjacent characters are the same. Every occurrence from the input must appear exactly once in the output; characters may move to any positions.

Return any rearranged string satisfying the adjacency condition. If no such arrangement exists because one character occurs too frequently, return the empty string. The task does not require the lexicographically smallest or otherwise uniquely ordered valid result.

### Function Contract

**Inputs**

- `s`: a nonempty lowercase string.

**Return value**

- Any permutation of `s` with unequal adjacent characters, or `""` if such a permutation is impossible.

### Examples

**Example 1**

- Input: `s = "aab"`
- Output: `"aba"`
- Explanation: The two copies of `a` are separated by `b`.

**Example 2**

- Input: `s = "aaab"`
- Output: `""`
- Explanation: Three copies of `a` cannot fit into the two available separated positions.

**Example 3**

- Input: `s = "vvvlo"`
- Output: `"vlvov"`
- Explanation: This is one of multiple possible arrangements with no equal neighbors.
