# Smallest String With Swaps

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1202 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-string-with-swaps/) |

## Problem Description

### Goal

You are given a lowercase string `s` and a list `pairs`, where each entry `[a,b]` names two 0-indexed positions. One allowed operation swaps the characters currently stored at the two indices of any listed pair.

Each allowed pair may be used any number of times and in any order. Return the lexicographically smallest string reachable from `s` after any sequence of these swaps, including the choice to perform no swap.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1\le n\le10^5$.
- `pairs`: A list of $p$ index pairs, where $0\le p\le10^5$ and every endpoint lies between `0` and `n - 1`.

**Return value**

- The lexicographically smallest string obtainable by repeatedly swapping characters at listed pairs of indices.

### Examples

**Example 1**

- Input: `s = "dcab"`, `pairs = [[0,3],[1,2]]`
- Output: `"bacd"`

The two disconnected pairs can be optimized independently.

**Example 2**

- Input: `s = "dcab"`, `pairs = [[0,3],[1,2],[0,2]]`
- Output: `"abcd"`

The extra pair connects all four indices, allowing the characters to be fully reordered.

**Example 3**

- Input: `s = "cba"`, `pairs = [[0,1],[1,2]]`
- Output: `"abc"`
