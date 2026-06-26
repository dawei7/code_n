## Problem Description & Examples
### Goal
A trie (pronounced as 'try') or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. Design a Trie structure.

In this simulation, `solve(operations)` executes a series of commands on a single Trie instance:
- `["insert", word]`: Inserts `word`.
- `["search", word]`: Returns `True` if `word` is in the trie.
- `["startsWith", prefix]`: Returns `True` if there is a previously inserted word that starts with `prefix`.

### Function Contract
**Inputs**

- `operations`: List[List] - trie commands

**Return value**

List[bool] - output results of search and startsWith operations

### Examples
**Example 1**

- Input: `[["insert", "apple"], ["search", "apple"]]`
- Output: `[True]`

**Example 2**

- Input: `operations = [['startsWith', 'b'], ['search', 'bat'], ['startsWith', 'ban']]`
- Output: `[False, False, False]`

**Example 3**

- Input: `operations = [['insert', 'bat'], ['insert', 'apricot'], ['insert', 'banana']]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
- [Trie insert and search](trie_01_trie-insert-and-search.md)
- [Longest common prefix](trie_03_longest-common-prefix.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
