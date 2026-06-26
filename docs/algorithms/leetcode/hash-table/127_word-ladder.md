# Word Ladder

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_163` |
| Frontend ID | 127 |
| Difficulty | Hard |
| Topics | Hash Table, String, Breadth-First Search |
| Official Link | [word-ladder](https://leetcode.com/problems/word-ladder/) |

## Problem Description & Examples
### Goal
A transformation sequence from word `begin_word` to word `end_word` using a dictionary `word_list` is a sequence of words `begin_word -> s1 -> s2 -> ... -> sk` such that:
- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `word_list`. Note that `begin_word` does not need to be in `word_list`.
- `sk == end_word`

Given two words, `begin_word` and `end_word`, and a dictionary `word_list`, return the number of words in the shortest transformation sequence from `begin_word` to `end_word`, or `0` if no such sequence exists.

### Function Contract
**Inputs**

- `begin_word`: str
- `end_word`: str
- `word_list`: List[str]

**Return value**

int - length of shortest transformation chain

### Examples
**Example 1**

- Input: `begin_word = "hit", end_word = "cog", word_list = ["hot", "dot", "dog", "lot", "log", "cog"]`
- Output: `5`

**Example 2**

- Input: `begin_word = 'hit', end_word = 'cog', word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']`
- Output: `5`

**Example 3**

- Input: `custom_case_3`
- Output: `derive by applying the strategy above`

---

## Underlying Base Algorithm(s)
- [Breadth-first search](graph_02_bfs.md)
- [Depth-first search](graph_03_dfs.md)
- [Topological sort](graph_07_topological-sort.md)
- [Union-find](graph_09_union-find.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
