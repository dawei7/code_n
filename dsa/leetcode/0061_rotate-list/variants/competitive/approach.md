## General

**Turn the list into a ring, then choose where the ring opens**

A right rotation preserves the circular order of all nodes; it only changes which node is considered first and which link is considered the end. The competitive solution exploits this by connecting the old tail to the old head, temporarily forming a cycle. It then walks to the desired new head and breaks the link immediately before it.

This avoids separately managing suffix and prefix chains. The ring already contains the desired order from any chosen starting node.

**Find both length and old tail**

The source begins with `n = 1` and `cur = head`. While `cur.next` exists, it moves forward and increments `n`. At termination, `cur` is the old tail and `n` is the exact node count.

The initial guard returns empty and one-node lists before this traversal. Thus `head` and `head.next` are valid for the general case, and the resulting length is at least two.

**Close the cycle**

`cur.next = head` replaces the old tail's null link with a link to the old first node. Every node now has a successor, and following `next` repeatedly circles through the list.

Immediately afterward, `cur` is reset to `head`, while `tail` keeps the old-tail reference. At this moment, `tail` is the node immediately before `cur` on the cycle.

**Walk to the new opening**

Let $r = k \bmod n$ be the effective right rotation. The desired new head was originally at index $n-r$. The loop runs `n - k % n`, which is exactly $n-r$, iterations.

Each iteration first assigns `tail = cur` and then moves `cur = cur.next`. Therefore, after every step, `tail` remains the predecessor of `cur`. After $n-r$ steps, `cur` is the desired new head and `tail` is the desired new tail.

The code then sets `tail.next = None`, opening the ring at that point, and returns `cur`.

**Why the zero-remainder case still works**

If `k % n == 0`, the loop runs `n` times. A full traversal around the cycle returns `cur` to the original head and `tail` to the original tail. Breaking `tail.next` restores the original null link, so the unchanged list is returned.

This source does not need a special zero-rotation branch. It performs one extra full-cycle walk, which remains $O(n)$.

**Trace for `k` larger than the length**

For `[0,1,2]` and `k = 4`, the effective rotation is $4 \bmod 3 = 1$. The loop takes $3-1=2$ steps around the ring. Starting with `cur` at 0, it moves to 1 and then 2; `tail` ends at 1. Breaking `1.next` returns the chain `2 -> 0 -> 1`.

**The predecessor invariant**

Before and after every loop iteration, `tail.next` is `cur` within the temporary cycle. The paired assignments advance this adjacent pair by one node. This invariant proves that breaking `tail.next` always places a null immediately before the returned head.

The number of advances determines which node becomes `cur`. Moving $n-r$ positions from original index 0 lands at index $n-r$ modulo $n$, which is precisely the first node of the final $r$-node suffix. The remainder of the ring then lists suffix followed by prefix.

**Temporary-cycle caution**

Between `cur.next = head` and `tail.next = None`, the list has no null terminator. Any unrelated traversal or recursive `__repr__` during that interval would loop indefinitely. The method performs no such operation and always breaks the cycle before returning, so the externally observed result is a normal finite list.

The module-level `ListNode` class is harness structure; the rotation itself creates no new nodes.

## Complexity detail

The first traversal visits all $n$ nodes to count and find the tail. The cycle walk takes between 1 and $n$ steps because `n - k % n` lies in that range. Sequential passes give $O(n)$ time.

Only the count and a constant number of node references are stored. The temporary cycle reuses an existing `next` field and allocates no collection, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Two-pointer gap without a cycle:** Advance one pointer by the reduced `k`, move two pointers together, then cut and reconnect. It avoids temporarily cyclic structure.
- **Array of node references:** It makes the new-head index immediate but uses $O(n)$ additional space.
- **Repeated tail extraction:** It is simple conceptually but can rescan the list for every rotation and cost $O(nk)$.
- **Empty or one-node list:** The early return avoids cycle construction and modulo concerns.
- **Rotation multiple of length:** One full ring traversal restores the original head and tail.
- **Huge `k`:** `k % n` prevents the walk from depending on the magnitude of `k`.
- **Effective rotation one:** The old tail becomes the new head, and the old second-to-last node becomes the new tail.
- **Cycle must be broken:** Omitting `tail.next = None` would return an infinite cyclic list rather than a valid result.
- **Values do not matter:** The algorithm changes node positions through links and never inspects `val`.
- **Input mutation:** The original nodes are relinked in place; callers must use the returned head.
