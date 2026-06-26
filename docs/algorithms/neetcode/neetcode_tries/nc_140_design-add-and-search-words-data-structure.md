## Problem Description & Examples
### Goal
Design a data structure that supports adding new words and finding if a string matches any previously added string.

In this simulation, `solve(operations)` executes a series of commands:
- `["addWord", word]`: Adds `word`.
- `["search", word]`: Returns `True` if there is any string in the structure that matches `word`. `word` may contain dots `'.'` where dots can match any letter.

### Function Contract
**Inputs**

- `operations`: List[List] - commands

**Return value**

List[bool] - output results of search operations

### Examples
**Example 1**

- Input: `[["addWord", "bad"], ["search", ".ad"]]`
- Output: `[True]`

**Example 2**

- Input: `operations = [['addWord', 'pad'], ['addWord', 'mad'], ['search', 'p.d']]`
- Output: `[True]`

**Example 3**

- Input: `operations = [['addWord', 'bad'], ['addWord', 'bad'], ['addWord', 'pad']]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
- [Trie insert and search](trie_01_trie-insert-and-search.md)
- [Longest common prefix](trie_03_longest-common-prefix.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
