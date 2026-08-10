## General

The target is defined by two priorities:

1. choose the deepest tree level;
2. within that level, choose its leftmost node.

Breadth-first search processes nodes one level at a time, so the solution can remember the first node of each level and let deeper levels overwrite earlier candidates.

The queue starts with only `root`. Because the tree is guaranteed nonempty, this initialization always contains a real node.

**Queue invariant at the start of each outer iteration.** Before `while q` processes a level, the queue contains exactly all nodes of one depth, ordered from left to right.

This is true initially because the root is the sole node at depth zero. Assuming it is true for one level, processing parents from left to right and appending each parent's left child before its right child produces the next depth in left-to-right order. Therefore the invariant holds inductively for every level.

Given that invariant, `q[0]` is the leftmost node of the current level. The code assigns

`ans = q[0].val`

before removing any node. Every new outer iteration overwrites `ans` with the leftmost value at a deeper level.

**Process exactly one level.** `len(q)` is evaluated when the `range` is created. It snapshots the number of nodes currently in the level. The loop pops exactly that many nodes.

Children appended during those pops belong to the next level. They increase the live queue length, but they do not increase the already-created range. This prevents the algorithm from mixing two depths in one outer iteration.

For each popped `node`, its left child is appended first and its right child second. Combined with left-to-right parent processing, that preserves the required ordering for the next queue snapshot.

It helps to separate the queue's two roles during an iteration. The nodes that were present when the level began are the work still to be consumed now. The newly appended children are the ordered description of the next level. The fixed iteration count creates an invisible boundary between those two regions even though one physical deque stores both. When the last current-level node is popped, only the next-level region remains, ready for the next outer iteration.

Once the final level has been processed, no children were appended and the queue becomes empty. The outer loop ends without another overwrite, so `ans` remains the first value of that final level—the requested bottom-left value.

For tree `[2, 1, 3]`, the first iteration records two and enqueues one then three. The second records one and empties the queue. The result is one.

In the deeper example, intermediate levels may record values one, two, and four, but the level containing node seven is deeper. When that final level begins, seven is at `q[0]` and becomes the last stored candidate.

**Why “leftmost” is about position, not numeric value.** The algorithm never compares node values. A large negative value can be leftmost, and a much smaller or larger value elsewhere on the level is irrelevant. Queue order represents tree geometry directly.

Correctness follows from the queue invariant and overwrite behavior. Every outer iteration corresponds to exactly one depth, `q[0]` is its leftmost node, and `ans` records it. Levels are processed from shallowest to deepest. The last assignment therefore comes from the deepest existing level and selects that level's leftmost node.

The algorithm does not need to know the tree height in advance. Queue exhaustion tells it that the most recently processed level had no following level. This is why repeatedly replacing `ans` is safe: an early candidate is provisional, while the candidate left after exhaustion is final.

The initial `ans = 0` is only a placeholder. Since the root exists, the first outer iteration always replaces it before return. Node values may span the full 32-bit range, but no sentinel comparison uses zero.

## Complexity detail

Let $n$ be the number of nodes and $w$ the maximum width of any level. Every node is enqueued and dequeued once, with constant work for its children, so time is $O(n)$.

The queue holds at most one complete level plus children being formed for the next level, which is $O(w)$ and at worst $O(n)$. The scalar answer uses $O(1)$ space. The manifest records worst-case $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Left-first depth-first search:** Track depth and update the answer only on first reaching a new maximum depth. It uses $O(h)$ recursion or stack space and also runs in $O(n)$ time.
- **Right-to-left BFS:** Enqueue right children before left children and return the last node popped. It avoids explicit level snapshots but makes the leftmost result emerge from traversal order less directly.
- **Store every level list:** Collect level values and read the first of the last list. This works but retains unnecessary output-sized intermediate data.
- **Single node:** The first and only queue head is the root, so its value is returned.
- **Only left children:** Each level contains one node and the deepest descendant wins.
- **Only right children:** Each level also contains one node; “leftmost” still means that sole deepest node.
- **Negative values:** No numeric comparison is used, so sign and magnitude do not affect selection.
- **Snapshot `len(q)`:** Processing until the queue is empty inside the inner loop would mix all remaining levels and break the level-head invariant.
- **Child order:** Appending left before right is essential for `q[0]` to be the next level's leftmost node.
