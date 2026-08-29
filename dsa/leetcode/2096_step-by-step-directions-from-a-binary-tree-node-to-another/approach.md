## General

**The shortest tree path turns at the lowest common ancestor**

In a tree there is exactly one simple path between two nodes, so that path is automatically the shortest. From the start node, it moves upward to the lowest common ancestor, or LCA, of the start and destination, then moves downward from the LCA to the destination.

The source first finds this turning node with `lca(root, startValue, destValue)`. If a recursive node is null or matches either target value, it returns that node. Otherwise it searches both subtrees.

If both recursive results are non-null, one target lies on each side, so the current node is their lowest shared ancestor. If only one side returns a node, both targets or the only target found lie on that side, so that result is propagated upward.

Because both values are guaranteed to exist, the final `node` is the LCA.

**Find downward direction paths from the LCA**

The helper `dfs(node, x, path)` searches for target value `x` while maintaining directions from its starting node.

It first tries the left child:

- append `"L"`;
- recurse left;
- if found, return immediately with the successful path unchanged.

If the left search fails, the last tentative direction is replaced with `"R"` and the right subtree is searched. If that also fails, `path.pop()` removes the direction before returning false.

This backtracking ensures `path` always describes the current recursion route. On success, it contains exactly the L/R path from the LCA to the target.

The method calls the helper twice, producing `path_to_start` and `path_to_dest`.

**Convert the start-side path into upward steps**

`path_to_start` describes how to travel downward from the LCA to the start. Its length is therefore the number of edges between those nodes.

Traveling in the opposite direction requires that many parent moves, regardless of whether the downward edges were left or right. The source creates

`"U" * len(path_to_start)`.

It then appends `"".join(path_to_dest)`, which already contains the correct downward directions from the LCA to the destination.

For a start path `["L", "L"]` and destination path `["R", "L"]`, the result becomes `"UU" + "RL" = "UURL"`.

**Why this is the shortest correct direction string**

Any path from the start to the destination must leave the start's branch and reach their first shared ancestor. Going above the LCA would add an unnecessary up-and-down detour. The unique simple path therefore contains exactly the upward edges from start to LCA and exactly the downward edges from LCA to destination.

The first part has the length of `path_to_start` and must consist entirely of `U`. The second part is exactly `path_to_dest`. The returned concatenation follows every edge of the unique simple path once and no other edge, proving both correctness and minimum length.

If the start itself is the LCA, `path_to_start` is empty and the result contains only downward moves. If the destination is the LCA, `path_to_dest` is empty and the result contains only `U` moves.

**Understand the recursive costs**

The LCA traversal may inspect the whole tree. Each later DFS begins at the LCA; depending on child order and tree shape, it may inspect much of that subtree before finding its target. These are a constant number of linear traversals, so total time stays linear.

The implementation reads the tree without changing child pointers.

## Complexity detail

Let $n$ be the number of tree nodes and $h$ its height.

The LCA search is $O(n)$. Each of the two path searches is at most $O(n)$, and building the result is $O(h)$. Total time is $O(n)$.

Recursive call depth and each stored path can reach $O(h)$. In a skewed tree, $h=n$, so worst-case auxiliary space is $O(n)$. The returned direction string can also have length $O(n)$.

Python recursion depth may be a practical concern for a highly skewed tree with $10^5$ nodes, even though the asymptotic analysis is correct.

## Alternatives and edge cases

- **Root paths without explicit LCA:** Find root-to-start and root-to-destination paths, remove their common prefix, replace the remaining start directions with `U`, and append the destination suffix. This is also linear.
- **Parent map plus BFS:** Converting the tree to bidirectional movement and running BFS finds a shortest path, but stores parent and predecessor information for many nodes.
- **Go above the LCA:** This always adds unnecessary edges and cannot be shortest.
- **Start is an ancestor of destination:** No upward moves are needed; the destination path is returned directly.
- **Destination is an ancestor of start:** The result contains only the required number of `U` characters.
- **Targets in different root subtrees:** Their LCA may be the root, and both DFS paths begin there.
- **Unique values:** Value comparisons identify nodes unambiguously.
- **Backtracking mutation:** Replacing the failed `L` with `R` and popping after both failures prevents stale directions from leaking into another branch.
- **Skewed tree:** Correctness is unchanged, but recursion can reach depth $n$.
- **No tree mutation:** Only temporary lists and recursion state are changed.
