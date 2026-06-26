## Problem Description & Examples
### Goal
You are given a 0-indexed string `s` and a dictionary of words `dictionary`. You have to break `s` into one or more non-overlapping substrings such that each substring is present in `dictionary`. There may be some extra characters in `s` which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up `s` optimally.

### Function Contract
**Inputs**

- `s`: str
- `dictionary`: List[str]

**Return value**

int - minimum extra characters left over

### Examples
**Example 1**

- Input: `s = "leetscode", dictionary = ["leet", "code"]`
- Output: `1`

**Example 2**

- Input: `s = 'leetscode', dictionary = ['leet', 'code', 'leetcode']`
- Output: `1`

**Example 3**

- Input: `s = 'hellosworldx', dictionary = ['hello', 'world']`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Trie insert and search](trie_01_trie-insert-and-search.md)
- [Longest common prefix](trie_03_longest-common-prefix.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
