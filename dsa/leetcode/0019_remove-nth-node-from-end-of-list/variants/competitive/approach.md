## General

**Translate an end-relative position into a maintained distance**

A singly linked list supports only forward movement, yet the requested position is measured backward from the tail. The competitive solution avoids storing nodes or traversing the list once just to learn its length. It gives one pointer an $n$-node head start and then advances two pointers together. When the leading pointer reaches the last node, the trailing pointer is positioned immediately before the node to delete.

This works because the contract guarantees $1 \le n \le sz$, where $sz$ is the number of nodes. Every required lead step is therefore valid, and there is exactly one target node.

**Introduce a predecessor for the real head**

The source constructs

```python
dummy = ListNode(-1)
dummy.next = head
```

The value `-1` is only a placeholder; it is never compared with list values and is never returned as part of the answer. The structural purpose of `dummy` is to ensure that every real node has a predecessor. Without it, deleting the original `head` would require a special branch because no real node points to the head. With it, every deletion becomes the same link update.

Both `slow` and `fast` start on `dummy`. The final result is `dummy.next`, which automatically reflects whether the original head survived.

The `ListNode` class defined above `Solution` is support structure for this standalone source. The algorithm itself does not rebuild that class or create a node for every input value; it allocates only the one dummy node.

**Move `fast` exactly $n$ times**

The first loop is

```python
for i in range(n):
    fast = fast.next
```

The loop variable `i` is not used inside the body; `range(n)` simply guarantees exactly `n` link traversals. If the dummy is position zero and real nodes are positions one through $sz$, `fast` ends at position $n$ while `slow` remains at zero. The pointers are now $n$ positions apart.

Some versions of this technique advance a leading pointer `n + 1` times and stop it at `None`. This source instead advances `n` times and later stops `fast` on the tail by testing `fast.next`. Its initialization and termination condition form a matched pair. The chosen pair ensures that `slow` ends at the target's predecessor.

**Keep the separation constant**

While `fast.next` exists, this assignment moves both pointers one node:

```python
slow, fast = slow.next, fast.next
```

Python evaluates both right-hand sides before assigning either left-hand name, so both moves are based on the old state. Since each pointer advances once, their $n$-position gap remains unchanged.

The loop ends when `fast` is the last node. It does not continue until `fast` becomes `None`. Numbering positions makes the endpoint precise: `fast` has advanced from position $n$ to position $sz$, a further $sz-n$ moves. `slow` makes the same number of moves from zero and therefore ends at position $sz-n$. The target node is position $sz-n+1$ from the beginning, so `slow.next` is exactly the target.

**Splice the target out of the reachable chain**

The line

```python
slow.next = slow.next.next
```

changes one link. Before it executes, `slow.next` names the target. Its `next` field names the successor, or `None` if the target is the tail. Assigning that successor to the predecessor's link bypasses exactly one node.

No node values are changed. Nodes before `slow` remain connected exactly as before, and nodes after the target preserve all their links. Returning `dummy.next` yields the head of this modified chain.

**Follow the pointers for an interior deletion**

For `[1, 2, 3, 4, 5]` with `n = 2`, start both pointers on the dummy. The lead loop moves `fast` first to `1` and then to `2`. The gap is two positions. The paired loop moves the pointers through these states:

| State | `slow` points to | `fast` points to |
|---|---|---|
| After the lead loop | dummy | `2` |
| Paired move 1 | `1` | `3` |
| Paired move 2 | `2` | `4` |
| Paired move 3 | `3` | `5` |

Because node `5` has no successor, the loop stops. `slow.next` is node `4`, the second node from the end. Redirecting node `3` to node `5` returns `[1, 2, 3, 5]`.

**See why both extremes need no branch**

If `n = 1`, the initial gap is one. When `fast` reaches the tail, `slow` is the node just before it, so setting `slow.next` to `None` removes the tail.

If `n = sz`, moving `fast` `n` times places it on the tail immediately. `fast.next` is already `None`, so the paired loop performs zero iterations and `slow` remains at the dummy. The splice makes `dummy.next` skip the original head. For a one-node list, the same operation makes `dummy.next` equal `None`.

**Why the invariant proves correctness**

Immediately after the first loop, `fast` is exactly $n$ positions ahead of `slow`. Every iteration of the second loop advances both once and preserves this invariant. At termination, `fast` is the tail; therefore the node after `slow` is exactly $n$ nodes from that tail when counting the tail as the first node. The splice removes that node and no other. Because the dummy handles position zero uniformly, this proof includes deletion of the head as well as interior and tail deletions.

## Complexity detail

Let $sz$ denote the number of nodes in the input list.

- **Time complexity: $O(sz)$.** The leading pointer makes `n` preliminary moves and then `sz - n` paired-loop moves, so it traverses the list once from the dummy to the tail. `slow` makes `sz - n` moves. Altogether there are at most $2sz$ pointer advances, which is linear.
- **Auxiliary space: $O(1)$.** The dummy node, two node references, and loop variable occupy a fixed amount of storage independent of $sz$. The existing list nodes are relinked rather than copied, and the returned chain is not counted as auxiliary memory.

Calling this a one-pass method does not mean each physical node object is read by only one pointer. It means there is no first full traversal followed by a restarted second traversal; the pointers progress together within one algorithmic sweep.

## Alternatives and edge cases

- **Length followed by deletion:** A first walk computes $sz$; a second walk moves $sz-n$ steps from a dummy to the predecessor. It remains $O(sz)$ time and $O(1)$ space but does not meet the one-coordinated-pass follow-up as directly.
- **Reference stack:** Saving each node permits backward indexing but costs $O(sz)$ additional memory.
- **Recursion:** The return phase can count nodes from the end, but the call stack grows to $O(sz)$ and is unnecessary here.
- **Optimal variant:** It uses the same pointer invariant and differs mainly in type annotations, dummy construction, and naming; both selected algorithms have identical asymptotic behavior.
- **Remove the tail (`n = 1`):** `slow` stops at the penultimate node and redirects its link to `None`.
- **Remove the head (`n = sz`):** `slow` stays at the dummy and `dummy.next` advances to the second node.
- **One node:** Head and tail are the same target, so the returned pointer is `None`.
- **Duplicate values:** Position, not value, determines the target; equal node values require no special handling.
- **The removed node is bypassed, not erased:** Python reclaims it only when no references remain. An external reference could still access the detached node object.
- **In-place mutation:** Links in the supplied list are changed. The caller must use the returned head because the correct head may differ from the original one.
- **Out-of-contract `n`:** The implementation intentionally trusts $1 \le n \le sz$. A reusable library function with untrusted input would need to detect a failed lead step and choose an error policy.
