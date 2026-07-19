# Alien Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 269 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/alien-dictionary/) |

## Problem Description
### Goal
You are given words already sorted lexicographically according to an unknown alphabet. Infer precedence relationships from the first differing characters of adjacent words, while also accounting for every distinct character that appears even when no comparison constrains it.

Return any ordering of all observed characters consistent with the supplied dictionary. Several orders may be valid. Return an empty string when the constraints contain a cycle or when a longer word incorrectly appears before its exact prefix, since no alphabet can produce that order. Do not impose precedence from later differing positions after the first difference has already determined an adjacent-word comparison.

### Function Contract
**Inputs**

- `words`: dictionary words in alien lexicographic order

**Return value**

Any character ordering consistent with the dictionary, or `""` when the ordering is impossible.

### Examples
**Example 1**

- Input: `words = ["wrt","wrf","er","ett","rftt"]`
- Output: `"wertf"`

**Example 2**

- Input: `words = ["z","x","z"]`
- Output: `""`

**Example 3**

- Input: `words = ["abc","ab"]`
- Output: `""`
