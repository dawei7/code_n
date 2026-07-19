## General
**Treating each retained block as an anchor**

Maintain `current` at the first node of the next keep block. That node is retained because both `m` and `n` are positive and every cycle begins by keeping. Move `current` forward at most `m - 1` links, stopping early if the list ends. If the traversal reaches `None`, there is no deletion block and the transformation is finished.

Otherwise, `current` is the last retained node in this cycle. Its `next` link is the only link that must change: it currently points to the first node scheduled for deletion and must eventually point to the first node after the deletion block.

**Advancing over nodes to delete**

Set a second pointer, `after_deleted`, to `current.next`. Advance it up to `n` times. Each advance crosses one deleted node; stopping at `None` means the deletion block reaches the tail.

Assign `current.next = after_deleted`. This single rewire removes the entire skipped block from the list reachable through `head`. Then set `current = after_deleted`, which is exactly the first retained node of the next cycle, and repeat.

**Why no dummy node is necessary**

The first $m$ nodes are always retained and $m\ge1$, so the original head can never be deleted. Every modification occurs after a known retained node, and the return value is always `head`. A dummy predecessor would be harmless but would not simplify a possible head deletion because that case does not exist.

**Why every node receives the required treatment**

At the start of each cycle, `current` points to the first unprocessed node and that node is retained. The first traversal retains it plus the next at most $m-1$ nodes, so exactly the next $m$ available nodes form the keep block unless the list ends.

The second traversal advances across exactly the next $n$ available nodes unless the list ends sooner, and rewiring bypasses precisely those nodes. The new `current` is the first node not yet classified. Thus every completed iteration consumes one keep block followed by one delete block, never revisiting or reordering a node. When the list ends, all nodes have been classified according to the repeating pattern, proving the returned chain is correct.

## Complexity detail
Each node is crossed by at most one keep traversal or one deletion traversal. Although the algorithm contains two bounded inner loops, their work over all cycles sums to at most $L$, so the running time is $O(L)$.

Only `current`, `after_deleted`, and loop counters are stored. The list is modified in place and no recursion, array conversion, or replacement nodes are needed, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Copy retained values into an array:** Selecting indices by their position in the $m+n$ cycle is straightforward, but rebuilding a new list uses $O(L)$ extra space and discards the retained nodes' identities.
- **Dummy head:** A sentinel can make generic deletion code uniform, but the source rule always keeps the true head, so it adds an unnecessary node.
- **Recursive cycle processing:** Recursing once per keep/delete block mirrors the pattern, but uses stack space and may exceed recursion limits on long lists.
- **Rescan from the head for each position:** This can identify and copy the correct retained values, but repeated index lookup takes $O(L^2)$ time.
- **List shorter than `m`:** Every node belongs to the first keep block, so the original list remains unchanged.
- **Deletion reaches the tail:** Set the final retained node's `next` to `None`; no complete delete block is required.
- **`m == 1`:** Retain the cycle's first node and immediately bypass up to `n` successors.
- **`n == 1`:** Each keep block is followed by deletion of exactly one available node.
- **Repeated values:** Decisions depend only on position, never on value equality.
- **Cycle longer than the list:** Retain the first `m` available nodes and delete whatever portion of the following block exists.
