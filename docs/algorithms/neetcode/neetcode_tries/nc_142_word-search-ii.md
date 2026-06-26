## Problem Description & Examples
### Goal
Given an `m x n` board of characters and a list of strings `words`, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

### Function Contract
**Inputs**

- `board`: List[List[str]]
- `words`: List[str]

**Return value**

List[str] - list of found words

### Examples
**Example 1**

- Input: `board = [["o", "a"], ["e", "t"]], words = ["oat", "eat"]`
- Output: `["eat", "oat"]`

**Example 2**

- Input: `board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], words = ['oath', 'pea', 'eat', 'rain']`
- Output: `['eat', 'oath']`

**Example 3**

- Input: `custom_case_3`
- Output: `derive by applying the strategy above`

---

## Underlying Base Algorithm(s)
- [Trie insert and search](trie_01_trie-insert-and-search.md)
- [Longest common prefix](trie_03_longest-common-prefix.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
