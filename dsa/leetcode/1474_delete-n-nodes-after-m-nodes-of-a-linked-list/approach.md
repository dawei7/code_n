## General

**Keep a pointer to the final retained node of each cycle.** `pre` begins at the first node that should be kept. The loop advances it `m - 1` times, so together with its starting node, exactly `m` nodes belong to the kept block.

Each advance checks whether `pre` still exists. If the list ends before the kept block is complete, there are no nodes left to delete and the original head can be returned immediately.

**Walk across the deletion block without relinking yet.** After locating the last kept node, `cur = pre`. Advancing `cur` exactly `n` times makes it point to the nth node after `pre`, which is the last node scheduled for deletion when all `n` exist.

If the list ends early, `cur` becomes `None`. In that case every remaining node after `pre` belongs to the partial deletion block.

**Bypass deleted nodes with one pointer assignment.** When `cur` exists, `cur.next` is the first node after the deletion block and should begin the next kept block. Assigning `pre.next = cur.next` detaches all `n` skipped nodes at once.

When `cur is None`, the deletion block reaches the tail, so `pre.next = None` terminates the retained list.

The code then sets `pre = pre.next`. This is precisely the first retained node of the next cycle, restoring the loop interpretation.

**Pay attention to the off-by-one meanings.** `pre` already points at the first node being kept, which is why the first loop advances only `m - 1` times. By contrast, `cur` begins at the last kept node, not at the first deletion node. Its first advance reaches deletion node one, and its nth advance reaches deletion node `n`. The bypass must therefore use `cur.next`. Advancing `m` in the first loop or using `cur` as the reconnect target would shift the pattern by one.

**Trace one cycle.** With list one through thirteen, `m = 2`, and `n = 3`, `pre` starts at one and advances once to two. `cur` advances from two to three, four, then five. Linking two directly to six removes three through five. The next cycle starts at six.

On the next cycle, `pre` advances from six to seven, `cur` crosses eight, nine, and ten, and seven is linked to eleven. At the last cycle, eleven and twelve are kept; `cur` advances to thirteen and then reaches `None` before all three deletion positions exist. Linking twelve to `None` deletes the available tail node thirteen. This demonstrates that a short final deletion block is still removed completely.

**Why node identity and order are preserved.** The algorithm never creates replacement nodes and never changes values. It only changes the `next` pointer of each block's last retained node. Retained nodes therefore remain in their original relative order and identity.
At the start of each outer iteration, `pre` is the first node of the next keep block, and all earlier cycles are already correct. The first loop identifies up to `m` retained nodes. The second identifies up to `n` following deletion nodes. The bypass joins the retained prefix to the next cycle start or tail. Thus the invariant advances until the list ends.

The original `head` is always retained because `m >= 1`, so returning it is correct.

**Why no explicit delete operation is needed.** In a singly linked list, membership in the returned structure is determined by reachability from `head`. Once `pre.next` skips the deletion block, those nodes no longer appear during traversal of the result. Python's memory manager handles eventual reclamation; the algorithm's logical deletion is the pointer bypass itself.

## Complexity detail

Let `L` be the number of nodes. Pointers advance only forward. Each node is crossed as part of a keep block or deletion block a constant number of times, so total time is `O(L)`.

The method stores only `pre`, `cur`, and loop counters. It modifies links in place and uses `O(1)` auxiliary space, matching the manifest.

Detached nodes may remain temporarily connected to one another, but they are unreachable from the returned head. Runtime garbage collection can reclaim them when no external references remain.

No recursion or output copy is used.

## Alternatives and edge cases

- **Recursive cycle processing:** Keep `m`, skip `n`, and recurse from the next node. It is clear but uses stack space proportional to the number of cycles.
- **Copy retained values into new nodes:** It works functionally but violates the in-place identity benefit and uses linear space.
- **List shorter than m:** All available nodes are kept and the early return leaves the list unchanged.
- **Exactly m nodes remain:** The kept block reaches the tail and nothing is deleted.
- **Fewer than n deletion nodes remain:** All remaining nodes are removed by setting `pre.next` to `None`.
- **m equals one:** Keep one node, delete the next `n`, and repeat.
- **n equals one:** Delete exactly one node after every kept block.
- **Single-node list:** The node is retained because `m` is positive.
- **Head identity:** The head never changes and is returned directly.
- **No value changes:** Only links are modified.
- **Partial final keep block:** It remains intact because no following deletion phase can begin.
- **Partial final delete block:** Every available node after the kept block is removed by terminating `pre.next`.
- **Off-by-one safety:** Count the starting `pre` node as the first kept node, but count nodes only after moving `cur` as deleted nodes.
- **External references:** Another caller-held reference could still access a detached node, but it is correctly absent from the list reachable through returned `head`.
- **Constant space:** Traversal pointers replace any need for arrays or auxiliary lists.
