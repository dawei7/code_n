## General

**Every candidate is a unique-valued suffix of a root-to-node path.** Root the given tree at node $0$. During a depth-first traversal, the current ancestor chain from the root to a node contains every possible downward path ending at that node as a contiguous suffix. Among those suffixes, the longest one whose node values are all unique is the only candidate needed for that endpoint.

The source performs DFS iteratively with an explicit event stack. This avoids relying on Python recursion for a tree of up to $5\cdot10^4$ nodes.

**Track cumulative distance by depth.** `path_distances[d]` stores the weighted distance from root $0$ to the node at depth $d$ on the current DFS path. When entering a node, the source sets

`depth = len(path_distances)`

and appends its cumulative `distance` from the root.

If a valid special suffix begins at depth `left` and ends at the current depth, its edge length is

`distance - path_distances[left]`.

Subtracting root distances cancels the shared prefix. Its number of nodes is `depth - left + 1`.

**Move the left boundary past repeated values.** `last_depth[value]` records the deepest occurrence of each value on the current ancestor chain. Before the current node is registered, the source reads

`previous_depth = last_depth.get(value, -1)`.

If the value has appeared at depth $d$, any unique suffix ending here must start after that occurrence, at depth at least $d+1$. The inherited `left` already represents constraints from every other repeated value. Therefore, the exact new boundary is

`left = max(left, previous_depth + 1)`.

This is the tree-path analogue of the sliding window used for longest substrings without repeated characters.

After computing the boundary, the current suffix has no duplicate values. It is also the earliest possible valid start for this endpoint, so it has maximum weighted length because every edge weight is positive. The source compares its `length` with `best_length`. A strictly longer path replaces both result fields. On equal length, `best_nodes = min(best_nodes, nodes)` implements the required secondary objective.

**Register and later undo the current value.** After evaluating the path, `last_depth[value] = depth` makes the current occurrence visible to descendants. But DFS eventually leaves this subtree and explores a sibling branch. Values from the completed branch must not remain in the ancestor history.

The source solves backtracking with an explicit exit event. It pushes

`(1, value, -1, previous_depth, 0)`

before child entry events. Because the stack is LIFO, all descendants finish before this event is processed. In an exit event, the tuple fields are intentionally repurposed: `node` contains the value and `distance` contains that value's saved previous depth. The code pops the current cumulative path distance and either deletes the value from `last_depth` if it had no ancestor occurrence, or restores the saved depth.

This restoration is essential when the same value appears in different branches. A sibling is not a descendant of the completed node and must not treat its value as an ancestor duplicate.

**Build and traverse the rooted tree.** The adjacency list contains both directions of every undirected edge. Each entry event carries `parent`, and children are pushed only when `neighbor != parent`. Since the input is a tree, this is sufficient to avoid returning along the edge just used; a separate visited set is unnecessary.

Children are iterated through `reversed(graph[node])` only to preserve a predictable traversal order after LIFO pushing. The final maximum and tie-breaking result do not depend on child order.

For a repeated value, moving `left` does not physically remove entries from `path_distances`. They remain needed for DFS backtracking and cumulative-distance subtraction. The boundary simply identifies the valid suffix within the full ancestor chain.

**Why considering only the earliest valid suffix is enough.** Every later start also has unique values, but all edge lengths are positive, so dropping one or more leading edges cannot increase path length. Thus the earliest legal start dominates all other special paths ending at the same node. Evaluating it for every node covers a longest special path globally.

The maintained last-occurrence map proves the suffix is valid, and the max update applies the requested length-first, node-count-second ordering. A single-node path has length zero and one node, so initialization `best_length = 0` and `best_nodes = 1` correctly covers trees where no positive-length edge can join distinct values.

## Complexity detail

Let $n$ be the number of nodes. Building the adjacency list takes $O(n)$ time and space because a tree has $n-1$ edges. Every node creates one entry and one exit event. Each adjacency entry is inspected once from each endpoint, and dictionary operations are expected $O(1)$. Total expected time is $O(n)$.

The graph uses $O(n)$ space. The event stack, current path-distance list, and last-depth dictionary can each reach $O(n)$ in a deep tree. Total auxiliary space is $O(n)$, matching the manifest. The iterative traversal avoids an $O(n)$ call stack.

## Alternatives and edge cases

- **Start a DFS from every ancestor:** Enumerating all downward paths can take $O(n^2)$ time on a chain. The sliding boundary evaluates one dominant path per endpoint.
- **Recursive DFS:** It can maintain the same state elegantly, but a depth-$50000$ tree exceeds ordinary Python recursion limits. Explicit events are safer.
- **Global visited-value set only:** A set can detect duplication but cannot tell how far `left` must move after a repeat. The most recent depth is required.
- **No backtracking restoration:** Values from one branch would incorrectly constrain sibling paths. Exit events must restore the ancestor state.
- **All values distinct:** `left` stays zero, so every node evaluates the full root-to-node path and the farthest weighted descendant wins.
- **All values equal:** Every repeat moves `left` to the current depth. Only single-node paths remain valid, yielding `[0,1]`.
- **Zero-length path:** A node by itself is explicitly legal and supplies the initialized result.
- **Weighted rather than node length:** The primary comparison uses cumulative edge distance, while `nodes` is used only to break equal weighted lengths.
- **Positive edge lengths:** They justify keeping only the earliest valid start. With negative edges, a shorter suffix might have greater length, but negative lengths are excluded.
- **Repeated value in separate branches:** The saved `previous_depth` is restored on exit, so branch-local occurrences do not leak into one another.
