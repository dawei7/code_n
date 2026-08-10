## General

**Model mutually connected streets as an undirected graph**

Each grid cell is a graph node. Two horizontally or vertically adjacent cells share an edge only when the current cell opens toward the neighbor and the neighbor opens back toward the current cell. A one-sided opening is not a valid connection.

The solution builds these connections with disjoint-set union, also called union-find. After every valid neighboring pair has been merged, the top-left and bottom-right cells have a valid street path exactly when they belong to the same connected component.

**Flatten two-dimensional coordinates**

For $n$ columns, cell $(i,j)$ maps to integer

$$
i\cdot n+j.
$$

Rows occupy nonoverlapping blocks of $n$ IDs, so this mapping is unique from zero through $mn-1$. The start is ID zero, and the target is `m * n - 1`.

`p = list(range(m * n))` initially makes every node its own component representative. `find(x)` follows parent pointers to a root. The assignment `p[x] = find(p[x])` applies path compression, making future finds on that path faster.

To merge connected cells, the code assigns the current root's parent to the neighbor root:

`p[find(current)] = find(neighbor)`.

The union direction does not affect connectivity correctness.

**Decode each street's two openings**

Each street type triggers exactly the two direction helpers corresponding to its shape:

- Type 1 opens left and right.
- Type 2 opens up and down.
- Type 3 opens left and down.
- Type 4 opens right and down.
- Type 5 opens left and up.
- Type 6 opens right and up.

The outer loops visit every cell, inspect its type, and call those two helpers.

**Why each helper checks the neighbor type**

Opening toward a coordinate is insufficient unless the neighbor connects back.

For `left(i, j)`, a left neighbor exists only when `j > 0`. That neighbor must open right, which is true for types 1, 4, and 6.

For `right(i, j)`, the right neighbor must open left, so its type must be 1, 3, or 5.

For `up(i, j)`, the upper neighbor must open down, so its type must be 2, 3, or 4.

For `down(i, j)`, the lower neighbor must open up, so its type must be 2, 5, or 6.

Only after both the boundary and reciprocal-opening tests pass does the helper union the two cell IDs. This exactly encodes legal street continuation.

**Repeated edge checks are harmless**

A valid connection may be discovered from both endpoints. For example, one cell's right helper can union its neighbor, and later the neighbor's left helper can attempt the same union. Unioning nodes already in one component changes no connectivity result. Avoiding duplicate checks could reduce constants, but symmetric processing makes the mapping easier to verify.

**Why union-find answers a path question**

Union-find does not store a particular route. Instead, it maintains the transitive closure of discovered edges as components. Whenever cells share a direct valid connection, they are merged. If A connects to B and B connects to C, all three eventually have the same root, representing the path A–B–C.

After all cells are processed, `find(0) == find(m * n - 1)` means there is a chain of valid reciprocal street edges from start to target. Different roots mean no such chain exists.

**Why the algorithm is correct**

Every union performed corresponds to adjacent cells whose street openings face each other, so union-find never creates connectivity not present in the grid. Conversely, for every valid adjacent street connection, the helper associated with at least one endpoint's opening checks the reciprocal neighbor type and performs the union, so no real graph edge is omitted.

Union-find places two nodes in the same component exactly when a sequence of merged edges connects them. Since merged edges are exactly the legal street connections, equality of the start and target roots is equivalent to the existence of a valid grid path. The returned Boolean is therefore correct.

## Complexity detail

Let $V=mn$ be the number of cells. Each cell performs two constant-time neighbor checks and at most two union operations. Path compression makes repeated `find` operations very close to constant amortized time, commonly written $O(\alpha(V))$ when paired with the standard union-find analysis. Total time is $O(V\alpha(V))$, treated as $O(mn)$ in the manifest because the inverse Ackermann factor is effectively constant.

The implementation does not use union by rank or size, so the strongest textbook $\alpha(V)$ guarantee is normally associated with adding that heuristic as well. Path compression and bounded grid unions still provide near-linear practical behavior; a conservative discussion can retain the tiny union-find overhead rather than claim literal constant work per find.

The parent array contains $V$ integers, and recursive `find` uses transient stack depth determined by parent chains. Overall auxiliary space is $O(mn)$, matching the manifest.

## Alternatives and edge cases

- **Breadth-first search:** Traverse from the start and enqueue only reciprocally connected neighbors. It gives direct $O(mn)$ time and space and can stop when the target is reached.
- **Depth-first search:** The same reciprocal-direction test works recursively or with an explicit stack. Recursive depth can reach all cells.
- **Direction bitmasks:** Encode the two openings of each type and verify that a neighbor has the opposite bit. This removes four specialized helper membership lists but requires careful bit mapping.
- **Union by rank or size:** Adding it to path compression gives the standard strongest amortized union-find guarantee and prevents unnecessarily tall parent trees.
- **One-cell grid:** Start and target are the same node, so the method returns true; a zero-move path is valid.
- **Street points outside the grid:** The boundary guard rejects that opening without changing the street.
- **One-sided adjacency:** If the neighbor lacks the opposite opening, no union occurs.
- **Duplicate union attempt:** Merging an already connected pair is harmless.
- **Cycles:** Union-find naturally represents them without traversal loops or a visited set.
- **Street type 3 versus 4:** Type 3 is left-down, while type 4 is right-down; swapping them changes connectivity and is a common mapping error.
- **Start or target with unusable exits:** They remain disconnected unless another reciprocal opening joins them.
- **No grid mutation:** The method reads street types and changes only the separate parent array.
- **Recursive `find` depth:** Without union by rank, an adversarial parent chain can deepen recursion before compression; an iterative find or rank heuristic improves robustness.
