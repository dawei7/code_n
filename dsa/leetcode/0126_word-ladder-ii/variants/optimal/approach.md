## General
**BFS determines the shortest-distance subgraph before paths are built**

Treat words as graph vertices and one-character transformations as edges. Breadth-first search processes an entire distance layer at a time. For each `word`, the candidate enumerates its positions with `i`, replaces that character with each lowercase English letter, and keeps candidates found in `unvisited`.

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

## Complexity detail
Let $N$ be the number of dictionary words and $R$ the total number of word positions across all returned sequences. The source contract limits word length to at most five and fixes the alphabet at 26 letters, so the candidate generates only constant legal work per visited word. BFS plus output construction therefore takes $O(N + R)$ time. The word sets and bounded-degree parent DAG use $O(N)$ space, while the returned paths use $O(R)$, for $O(N + R)$ total space.

If word length $L$ and alphabet size $A$ were generalized beyond this source contract, Python substring construction and hashing would make neighbor generation $O(NAL^2)$ rather than $O(NLA)$, and the parent DAG could contain $O(NLA)$ references.

## Alternatives and edge cases
- **Store complete paths in the BFS queue:** duplicates prefixes heavily and consumes much more memory.
- **Remove neighbors immediately:** loses alternate parents discovered later in the same level.
- **Depth-first search first:** can explore exponentially many longer sequences before proving the shortest length.
- Multiple paths may share long prefixes or suffixes; the parent DAG stores those segments once until output enumeration.
- Changing a character to itself should be skipped or harmlessly rejected as already visited; it is not a transformation edge.
