## General

A root-to-leaf path is exactly the sequence of nodes on the active depth-first-search route when traversal reaches a leaf. The solution therefore keeps one mutable list `t` representing the current route, adds a node when entering it, emits the route only at a leaf, and removes the node when leaving. This is the standard choose–explore–undo pattern of backtracking.

The two shared lists have different roles:

- `t` is temporary traversal state containing string forms of node values from the root through the current node;
- `ans` is permanent output containing a completed string for each leaf.

Using a list of components avoids repeatedly copying a whole path string at every internal node. The full arrow-separated string is constructed only when it is actually required for the output.

**Entering a node extends the active path**

The helper first handles `None` by returning immediately. For a real node, it executes `t.append(str(root.val))`. At that moment, `t` contains precisely the root-to-current-node values in order.

Values are converted to strings before storage because the final representation is textual. Keeping the separator out of `t` simplifies both joining and backtracking: each list entry corresponds to exactly one tree node.

**A path ends only at a true leaf**

A leaf has neither a left nor a right child. The exact condition is

```text
root.left is None and root.right is None
```

When it succeeds, `"->".join(t)` inserts the required separator between adjacent values and appends the resulting immutable string to `ans`.

It is not enough to stop whenever either child is missing. A node with one child is not a leaf; its path must continue through the existing child. The explicit two-sided test preserves this distinction.

For an internal node, the helper recursively explores the left child and then the right child. A missing child returns immediately, while an existing child extends the same path list in its own call.

**Why the final `pop` is indispensable**

After the leaf is recorded or both child branches are explored, `t.pop()` removes the current node's value. This restores `t` to exactly the state it had before the current call.

Suppose traversal has reached path `1 -> 2 -> 5`. After recording it, the call for node `5` pops `5`, leaving `[1, 2]`. The call for node `2` then finishes and pops `2`, leaving `[1]`. The traversal can now visit node `3` and form `[1, 3]`. Without those pops, the second answer might incorrectly contain nodes from the completed left branch.

Backtracking makes one list sufficient for every branch. Each recursive call temporarily owns one appended entry and is responsible for removing that same entry before returning.

**Trace through the first example**

For the tree represented by `[1,2,3,null,5]`:

1. Enter root `1`: `t = ["1"]`.
2. Explore left node `2`: `t = ["1", "2"]`.
3. Its left child is missing, so that call returns without changing `t`.
4. Explore node `5`: `t = ["1", "2", "5"]`. It is a leaf, so join and append `"1->2->5"`.
5. Pop `5`, then finish node `2` and pop `2`; `t` is back to `["1"]`.
6. Explore right node `3`: `t = ["1", "3"]`. It is a leaf, so append `"1->3"`.
7. Pop `3`, return to root, and finally pop `1`.

The result contains `1->2->5` and `1->3`. Left-first order follows the source traversal, although the contract allows any ordering.

**Why every returned string is a valid path**

Whenever a call is active, its entry in `t` was appended after its parent's entry and before any descendant entry. Thus `t` always follows actual child edges from the root to the current node. A string is appended only when the current node has no children, so it ends at a leaf. Every emitted string is therefore a valid root-to-leaf path in the required format.

**Why every root-to-leaf path is returned exactly once**

Depth-first traversal calls the helper once for every real node reachable from the root. Every leaf is consequently reached once, and its unique ancestor chain is present in `t` at that moment. The function appends exactly once in that leaf's call. Internal nodes append nothing, and a tree has only one root-to-node path, so no root-to-leaf path can be duplicated.

The completed output string does not share mutable state with `t`. Joining creates a new string, so later pops and appends cannot change an answer already stored in `ans`.

## Complexity detail

Let $n$ be the number of nodes, $h$ the tree height, and $P$ the total number of characters across all returned path strings. Every real node is entered once, converted to text once, appended once, and popped once, giving $O(n)$ structural traversal work. Joining at the leaves writes exactly the output characters and separators, for $O(P)$ additional work. Total time is therefore $O(n+P)$, matching the manifest's `O(n + output)` description.

Excluding returned strings, the recursion stack contains at most one call per node along a root-to-leaf route, and `t` has the same maximum length. Auxiliary space is $O(h)$. For a balanced tree, $h=O(\log n)$; for a skewed tree, $h=O(n)$.

The output list and its strings require $O(P)$ space and must exist because the contract asks to return every formatted path. String versions of current node values in `t` add character storage proportional to the active path; under the bounded node-value range, that remains $O(h)$.

## Alternatives and edge cases

- **Pass an immutable path string into recursion:** Extend the path for each child. It is easy to read but copies prefixes at internal nodes, potentially doing more character work than joining only at leaves.
- **Iterative DFS stack:** Store `(node, path)` pairs explicitly. It avoids recursion depth limits but often stores several copied path strings simultaneously and can use more memory.
- **Parent pointers followed by reconstruction:** Record each node's parent during traversal and reconstruct at leaves. Tree nodes do not provide parent links here, so this adds a map without improving the required output cost.
- **Single-node tree:** The root is also a leaf. `t` becomes its one value, the joined string contains no arrow, and one path is returned.
- **Node with only one child:** It is not a leaf. The missing-child call returns immediately, and traversal continues through the existing child.
- **Negative values:** `str(root.val)` preserves the minus sign, and joining produces negative values correctly.
- **Duplicate node values:** Tree identity comes from structure, not value uniqueness. Different leaves can produce identical-looking value sequences in unusual trees, and both paths should remain in the output.
- **Empty tree outside the stated contract:** `dfs(None)` returns immediately and the method yields `[]`, so the implementation handles it naturally.
- **Repeated separators:** Joining a list of values inserts exactly one arrow between neighbors and none at either end.
- **Backtracking after a leaf:** The leaf must still pop its value. Otherwise its sibling branch would inherit stale path state.
- **Output order:** Left paths appear before right paths because the source calls `dfs(root.left)` first. No sorting is needed because any order is valid.
- **Deeply skewed tree:** The algorithm remains linear, but its recursion depth becomes $h=n$ and may be limited by the language runtime for much larger inputs.
