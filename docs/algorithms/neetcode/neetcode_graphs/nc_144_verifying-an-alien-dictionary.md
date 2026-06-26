## Problem Description & Examples
### Goal
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

Given a list of `words` written in the alien language, and the `order` of the alphabet, return `True` if and only if the given `words` are sorted lexicographically in this alien language.

### Function Contract
**Inputs**

- `words`: List[str]
- `order`: str - alien alphabet permutation

**Return value**

bool - True if words are sorted

### Examples
**Example 1**

- Input: `words = ["hello", "leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"`
- Output: `True`

**Example 2**

- Input: `words = ['xr', 'ojiqf'], order = 'oaxsgfhkwuecvdrltjzpqibnym'`
- Output: `False`

**Example 3**

- Input: `words = ['ao', 'rzsnt'], order = 'xylkwbfztnjrqahvgmuopdicse'`
- Output: `False`

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
