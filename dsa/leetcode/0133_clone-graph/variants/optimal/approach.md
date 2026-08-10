## General

**A deep copy must preserve relationships, not identities**

Returning the original starting node would reproduce the visible graph but would not be a clone. A deep copy requires one new object for every reachable original node. Each cloned node must have the same value, and its neighbor list must point only to cloned nodes in the same order as the original neighbor list.

Graphs make this harder than copying a tree. A node can have several incoming edges, and an undirected edge appears in both endpoints’ neighbor lists. Cycles are therefore normal. Recursing from `A` to `B` and then following `B` back to `A` would never terminate unless the algorithm remembers that `A` already has a clone.

The dictionary `g` is the central structure. It maps each original node object to the unique new node representing it:

`original node -> cloned node`

This mapping simultaneously prevents infinite traversal, preserves shared references, and guarantees that two edges pointing to the same original also point to the same clone.

**Create the clone before following edges**

The nested function `dfs(node)` first handles `None`, which represents the empty graph. It then checks whether the original node is already in `g`. If so, the function immediately returns the existing clone.

For a newly seen node, the function performs these steps in a crucial order:

1. create a new `Node` containing the same `val`;
2. store that clone in `g`;
3. recursively clone each neighbor;
4. append each returned neighbor clone to the new node’s neighbor list.

The dictionary insertion must happen before recursion. Consider two connected nodes `A` and `B`. While cloning `A`, recursion begins cloning `B`. When `B` follows its edge back to `A`, `A` is already in `g`, so that call returns the partially constructed clone of `A` instead of creating another object or recursing forever.

It is safe to return a clone before all its neighbors have been filled. Graph nodes are mutable reference objects. The returned reference points to the same clone that the original call continues populating, so later appends become visible through every edge already connected to it.

**What one DFS result guarantees**

Whenever `dfs(x)` returns, its return value is the one clone assigned to original node `x`. It has the same value. For each neighbor entry in `x.neighbors`, the clone’s list receives the result of cloning that exact original neighbor.

If a neighbor was unseen, recursion constructs it. If it was already seen, the dictionary supplies the previously created object. This distinction preserves graph topology:

- a cycle closes back to an existing clone;
- two originals sharing one neighbor also share one neighbor clone;
- parallel references would remain parallel references, although the stated graph has no repeated edges;
- the order of neighbor entries is preserved because the loop appends results in original order.

The mapping gives uniqueness. Only the branch for a node absent from `g` calls `Node(node.val)`, and that branch immediately inserts the result. Every later request for the same original returns that object. Thus there is exactly one clone per reachable original.

It also gives independence. Every mapped value was produced by a `Node` constructor, and neighbor lists contain those new values rather than original keys. Mutating a cloned node or its neighbor list therefore does not mutate the original graph.

**Why cloning from one node covers the whole graph**

The contract says the graph is connected and every node is reachable from the supplied node. Depth-first traversal follows every neighbor of every discovered node, so it eventually discovers all nodes. If the graph were disconnected, no method receiving only one node reference could discover components having no path from that node; the returned clone would appropriately cover only the reachable component.

For an isolated node, the constructor creates one clone, its neighbor loop does nothing, and that clone is returned with an empty neighbor list. For an empty graph, `dfs(None)` returns `None`.

The final call `dfs(node)` returns the clone corresponding specifically to the supplied starting node, which is the required entry point into the copied graph.

## Complexity detail

Let $V$ be the number of reachable vertices and $E$ the number of undirected edges.

Each original vertex enters the construction branch once. Across all vertices, the loops inspect every neighbor-list entry. An undirected edge appears twice in adjacency lists, but $2E$ is still $O(E)$. Dictionary lookup and insertion are expected $O(1)$ operations, so total time is $O(V+E)$.

The mapping stores $V$ original-to-clone pairs. The recursive call stack can contain up to $V$ frames for a path-shaped traversal. Standard auxiliary space excluding the returned clone graph is therefore $O(V)$. The newly constructed graph itself contains $V$ nodes and $O(E)$ neighbor references, so counting output storage gives $O(V+E)$, matching the manifest.

This distinction matters: the algorithm cannot avoid output storage because a deep copy inherently contains all vertices and edges. The `g` dictionary and recursion are the avoidable working memory.

## Alternatives and edge cases

- **Breadth-first cloning:** Create the starting clone, then use a queue to discover originals and connect their clones. It avoids recursion depth while using the same original-to-clone map.
- **Iterative depth-first cloning:** A manual stack follows depth-first order without relying on Python’s call stack. Its asymptotic bounds are unchanged.
- **Two-pass traversal:** First discover every vertex and create every clone, then traverse edges to fill neighbor lists. It can make the phases explicit but requires revisiting adjacency lists.
- **Map by node value:** Unique values make this possible under the stated contract, but mapping by original object is more robust and directly preserves identity even if value uniqueness changes.
- **Empty graph:** `None` returns `None`; no clone or dictionary entry is created.
- **Single isolated node:** Exactly one new node is returned with an empty neighbor list.
- **Cycles:** Storing a clone before descending is essential; moving `g[node] = cloned` after the neighbor loop would recurse forever.
- **Self-loops and repeated edges:** The contract excludes them, but the mapping-based algorithm would still clone them faithfully, including repeated neighbor-list entries.
- **Hashability:** Original nodes are dictionary keys. Ordinary Python objects are identity-hashable unless their class overrides equality without a compatible hash.
- **Runtime dependency:** The selected file imports `Optional` but calls `defaultdict` without importing it. A standalone execution needs `from collections import defaultdict`; a plain `{}` would also provide every operation this code uses.
- **Platform-provided type:** `Node` appears only inside a triple-quoted template block because the platform supplies it. The user solution should not recreate it in the native LeetCode environment.
