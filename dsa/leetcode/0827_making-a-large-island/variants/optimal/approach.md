## General
**Give every existing island a reusable identity**

Scan the grid once. Whenever an unvisited `1` appears, run an iterative depth-first search through its 4-directional neighbors. Write a new component label into a parallel matrix and count the component's cells. Store the resulting size under that label. After this pass, every land cell identifies its complete island in constant time, and no island needs to be traversed again for each possible change.

**Evaluate a water cell by merging distinct neighboring islands**

Changing a `0` at `(row, column)` creates one land cell. Its resulting island consists of that cell plus every existing island touching it above, below, left, or right. Collect the neighboring component labels in a set, then compute `1 + sum(sizes[label] for label in neighboring_labels)`. The set is essential: one bent or surrounding island may touch the same water cell from several directions but must contribute its size only once.

**Why checking local labels finds the global optimum**

Any newly connected path through the changed cell must enter one of its four neighbors, so the local label set includes every island that the operation can join. Conversely, every island represented by one of those labels becomes connected through the new cell. The candidate sum is therefore exactly the island created by that change. Taking the maximum over every `0`, while also retaining the largest unchanged component, covers every allowed choice because the operation is optional and affects at most one cell.

An all-water grid produces candidate size `1` for each cell. An all-land grid has no candidate changes, but the component-labeling pass records the existing size $n^2$.

## Complexity detail
There are $n^2$ cells. Component labeling visits each cell and each of its at most four neighbor edges a constant number of times. The second scan also checks at most four labels per cell, so the total time is $O(n^2)$. The label matrix, component-size table, and worst-case traversal stack use $O(n^2)$ auxiliary space.

## Alternatives and edge cases
- **Disjoint-set union:** Union adjacent land cells, store each root's size, and combine distinct roots around every `0`. It has near-linear time and $O(n^2)$ space but requires careful root deduplication.
- **Flip then flood-fill repeatedly:** Trying every `0` and recomputing all islands from scratch is correct but can take $O(n^4)$ time.
- **Recursive depth-first search:** It expresses component labeling compactly, but an island may contain $250{,}000$ cells and exceed Python's recursion limit; an explicit stack is safer.
- **All land:** Since the operation is optional and no `0` exists, return $n^2$.
- **All water:** Any one changed cell forms an island of size `1`.
- **Repeated neighboring label:** A single island touching the changed cell on multiple sides is added once, not once per side.
- **Diagonal land:** Diagonal cells remain disconnected unless a 4-directional path joins them.
- **Boundary cell:** Ignore neighbor coordinates outside the square rather than treating them as water components.
