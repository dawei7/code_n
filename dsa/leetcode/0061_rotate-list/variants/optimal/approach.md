## General

**A right rotation is one cut plus one reconnection**

For a list of length $n$, rotating right by `k` moves the final `k` nodes in front of the first $n-k$ nodes. The internal order of both pieces stays unchanged. Therefore, the algorithm does not need to move nodes one at a time. It needs to find the node immediately before the new head, cut there, and connect the old tail to the old head.

For `[1,2,3,4,5]` rotated by 2, the cut is between 3 and 4. The suffix `[4,5]` becomes the front, and the prefix `[1,2,3]` follows it.

**Reduce a huge `k` with the list length**

The first traversal counts nodes. `cur` begins at `head`, and each non-null node increments `n`. After the loop, `n` is the exact list length.

Rotating by $n$ positions returns every node to its original place. More generally, rotations that differ by a multiple of $n$ have the same effect. The assignment `k %= n` reduces even a value near $2 \times 10^9$ to an effective rotation from 0 through $n-1$.

If the remainder is zero, no links need to change and the original `head` is returned. This early return also avoids later pointer movement that would otherwise have to represent a cut after the tail.

**Handle lists with fewer than two nodes first**

An empty list has no nodes to rotate. A one-node list looks identical after any number of rotations. The first condition returns either list immediately.

This guard also prevents division by zero in `k %= n` for an empty list and guarantees that later pointer dereferences have enough structure.

**Create a fixed gap between two pointers**

After reduction, `fast` and `slow` both start at the old head. Advancing `fast` exactly `k` times creates a gap of `k` edges between them.

The second loop advances both pointers together while `fast.next` exists. When it ends, `fast` is the old tail. Because the gap never changes, `slow` is exactly `k` edges behind the tail. In zero-based positions, the tail is at $n-1$, so `slow` is at $n-k-1$.

That is the desired new-tail position. Its next node, at index $n-k$, is the first of the suffix that must move to the front.

**Perform link changes in a safe order**

`ans = slow.next` saves the new head before any link is cut. Then `slow.next = None` makes `slow` the new tail and separates the suffix from the prefix. Finally, `fast.next = head` connects the old tail to the old head.

After those operations, the chain beginning at `ans` runs through the old suffix to `fast`, continues through the old prefix at `head`, and ends at `slow`. Every original node appears once, and the new tail points to `None`.

Saving `ans` first is essential. If the code cut `slow.next` and had no other reference to the suffix head, the returned front piece could become inaccessible from local variables. Cutting before connecting also avoids leaving a temporary cycle in this implementation.

**Pointer trace for five nodes and two rotations**

After counting, `k` remains 2. `fast` advances from node 1 to node 3, while `slow` stays at node 1. They then move together: first to `(4,2)`, then to `(5,3)`. `fast.next` is now null, so `slow` is node 3.

The new head is node 4. Cutting after 3 and connecting 5 to 1 produces `4 -> 5 -> 1 -> 2 -> 3`.

**Why the method is correct**

Length reduction preserves the desired rotation. The constant-gap invariant proves that when `fast` reaches the old tail, `slow` is the node immediately before the last `k` nodes. The three link operations preserve both segment orders and concatenate suffix before prefix. Since the cut makes the old prefix end at `slow`, the returned structure is a proper acyclic singly linked list.

No node object is copied or deleted; only two `next` references change. This proves the returned list contains exactly the original nodes in the right-rotated order.

## Complexity detail

Counting visits $n$ nodes. Advancing `fast` uses fewer than $n$ steps, and the paired traversal uses at most $n$ more. These passes are sequential rather than nested, so time is $O(n)$.

The method stores a length, reduced rotation, and a constant number of node references. It allocates no array, node, or recursion stack, so auxiliary space is $O(1)$, matching the manifest. The linked list is modified in place.

## Alternatives and edge cases

- **Temporary cycle:** Connect the old tail to the head, walk to the new tail, and break the cycle. It is equally linear and constant-space but temporarily makes the structure cyclic.
- **Store nodes in an array:** Indexing makes the cut easy, but the array requires $O(n)$ extra memory.
- **Repeat one-step rotations:** Moving the tail to the front `k` times can cost $O(nk)$ and is infeasible for large `k`.
- **Empty list:** The early return avoids counting and modulo by zero.
- **One node:** Its only possible rotation is itself.
- **`k = 0` or a multiple of `n`:** Modulo gives zero, and no links are touched.
- **`k > n`:** Only the remainder matters, as shown by full-cycle rotations.
- **Effective `k = n-1`:** The cut occurs after the old head, moving every later node before it.
- **Node identity:** Existing nodes are relinked; values are neither copied nor reordered independently of nodes.
- **Caller-visible mutation:** The original head may no longer be the returned head, and its incoming relationship changes through tail reconnection.
