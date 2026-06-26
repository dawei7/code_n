## Problem Description & Examples
### Goal
There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in locally increasing order by the new language's rules. If there is no solution, return `""`. If there are multiple solutions, return any of them.

### Function Contract
**Inputs**

- `words`: List[str]

**Return value**

str - order of alien characters, or empty string

### Examples
**Example 1**

- Input: `words = ["wrt", "wrf"]`
- Output: `"tfwr"`

**Example 2**

- Input: `words = ['egd', 'aaf', 'gfg']`
- Output: `'edfag'`

**Example 3**

- Input: `words = ['dcb', 'afd', 'eb']`
- Output: `'dcbfae'`

---

## Underlying Base Algorithm(s)
- [Dijkstra shortest path](graph_04_dijkstra.md)
- [Kruskal minimum spanning tree](graph_08_kruskal-s-mst.md)
- [Prim minimum spanning tree](graph_10_prim-s-mst.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
