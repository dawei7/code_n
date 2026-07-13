# Word Ladder II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 126 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-ladder-ii/) |

## Problem Description
### Goal
Given two words of equal length and a `wordList` containing unique allowed words, transform `beginWord` into `endWord` by changing exactly one character at a time. Every word produced after the starting word, including the destination, must occur in `wordList`, and each intermediate form must have the same length.

Return all transformation sequences that use the minimum possible number of words, with both endpoints included in every sequence. Longer valid sequences must be omitted, while distinct shortest routes through different intermediate words must all be retained. Outer sequence order is irrelevant. If the destination is unavailable or cannot be reached through valid one-letter changes, return an empty list.

### Function Contract
**Inputs**

- `beginWord`: the first word in every sequence
- `endWord`: the required final word
- `wordList`: allowed transformed words, all with the same length

**Return value**

All shortest valid word sequences. Outer sequence order does not matter; word order inside each sequence does.

### Examples
**Example 1**

- Input: `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`
- Output: `[["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]`

**Example 2**

- Input: the same words without `"cog"`
- Output: `[]`

**Example 3**

- Input: `beginWord = "a", endWord = "c", wordList = ["a","b","c"]`
- Output: `[["a","c"]]`

### Required Complexity

- **Time:** $O(NLA + PL)$
- **Space:** $O(NL + PL)$

<details>
<summary>Approach</summary>

#### General

**BFS determines the shortest-distance subgraph before paths are built**

Treat words as graph vertices and one-character transformations as edges. Breadth-first search processes an entire distance layer at a time. For each word, replace every one of its `L` positions with each alphabet character and keep candidates found in the unvisited dictionary.

If `endWord` is absent from the dictionary, no valid sequence exists because every transformed word after the start must belong to it.

**Delay dictionary removal until the complete level is processed**

When neighbor `v` is reached from current word `u`, record `u` in `parents[v]`. Add `v` to the next frontier, but do not remove any next-frontier word from the unvisited set until all current-level words have been expanded.

This delay lets two distance-$d$ parents both record shortest edges into the same distance-$(d+1)$ child. Immediate removal would let whichever parent is processed first erase valid alternate shortest sequences. A set for the next frontier prevents redundant expansion while the parent collection preserves all converging edges.

**Finish the discovery level containing the end, then stop**

Once any edge reaches `endWord`, continue processing the rest of that same current layer so every shortest parent of `endWord` and its peers can be recorded. Do not expand a deeper layer: every later path would contain more transformations than the already known ending distance.

**Backtracking shares prefixes instead of storing full paths during BFS**

Start from `endWord` and recursively choose each recorded parent until `beginWord` is reached. The constructed chain runs backward, so reverse or prepend it when saving a result. Parent edges always decrease BFS distance by one, making this graph acyclic toward the start.

**The parent DAG contains exactly shortest-layer transitions**

Breadth-first search assigns each discovered level the minimum transformation distance from the start. Delaying removal until the level ends lets every distance-$d$ word record itself as a parent of the same distance-$(d+1)$ child, preserving converging shortest alternatives.

Removing the level afterward prevents any longer path from adding parents to an already reached word. Parent edges therefore always decrease distance by one toward the start. Backtracking this acyclic graph enumerates all and only paths whose length equals the minimum ending level.

#### Complexity detail

For `N` words of length `L` and alphabet size `A`, neighbor generation costs $O(NLA)$ before the ending level. Writing `P` returned paths costs $O(PL)$. The word sets, parent graph, and output use $O(NL + PL)$ space.

#### Alternatives and edge cases

- **Store complete paths in the BFS queue:** duplicates prefixes heavily and consumes much more memory.
- **Remove neighbors immediately:** loses alternate parents discovered later in the same level.
- **Depth-first search first:** can explore exponentially many longer sequences before proving the shortest length.
- Multiple paths may share long prefixes or suffixes; the parent DAG stores those segments once until output enumeration.
- Changing a character to itself should be skipped or harmlessly rejected as already visited; it is not a transformation edge.

</details>
