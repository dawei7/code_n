## General

**Build the reversed list by front insertion**

The exact solution creates an empty dummy-headed list and moves original nodes
into its front one at a time. After processing nodes from the original head
through some current position, `dummy.next` points to those processed nodes in
reverse order. The remaining original suffix begins at `curr` and still has its
original forward links.

This is slightly different in presentation from the editorial's usual
`previous` pointer, but `dummy.next` serves the same role: it is the head of the
already reversed portion.

**Start with an empty reversed prefix**

`dummy = ListNode()` creates a node whose `next` is initially null under the
platform template. `curr = head` points to the first unprocessed original node.

Before the loop begins, no original node has been reversed, so the reversed
prefix is empty and `dummy.next` is null. The entire input remains in the
unprocessed suffix beginning at `curr`.

The dummy is never returned as a data node. It provides a stable object whose
`next` field can be updated whenever a new node becomes the reversed head.

**Save the following node before changing a link**

At the start of an iteration, `curr.next` points to the rest of the unreversed
input. The assignment `next = curr.next` saves that reference.

Saving it must happen before assigning a new value to `curr.next`. Otherwise,
the only link to the unprocessed suffix could be lost, making the remaining
nodes unreachable from local variables.

The local name `next` shadows Python's built-in `next()` function. That does
not break this method because the built-in is not called, but a name such as
`following` or `next_node` would be clearer and would preserve access to the
built-in.

**Insert the current node at the reversed front**

`curr.next = dummy.next` points the current node backward toward the head of
the already reversed portion. On the first iteration, that value is null, so
the original head becomes the tail of the final list.

Then `dummy.next = curr` makes the current node the new front of the reversed
portion. These two assignments perform a standard singly linked-list front
insertion using the original node object rather than allocating a copy.

Finally, `curr = next` advances to the saved first node of the unreversed
suffix. The two portions remain disjoint and together contain every original
node.

**Trace `[1,2,3]`**

Initially, reversed portion is empty and `curr` points to 1.

- Save node 2. Point 1 to null and make dummy point to 1. Reversed part is
  `1`; unprocessed part is `2 -> 3`.
- Save node 3. Point 2 to 1 and make dummy point to 2. Reversed part is
  `2 -> 1`; unprocessed part is `3`.
- Save null. Point 3 to 2 and make dummy point to 3. Reversed part is
  `3 -> 2 -> 1`; no unprocessed node remains.

The loop stops and returns `dummy.next`, which points to node 3, the required
new head.

**Why the loop invariant proves reversal**

Before every iteration, nodes already removed from the original prefix appear
exactly once behind `dummy.next` in reverse original order. Nodes beginning at
`curr` appear exactly once in original order and have not yet been added.

The iteration removes the first unprocessed node, places it before every
previously processed node, and advances to the rest. Front insertion changes
the reversed sequence from `reverse(processed)` to
`current + reverse(processed)`, which is exactly the reverse of the newly
extended original prefix.

When `curr` becomes null, the unprocessed suffix is empty. The reversed portion
then contains all original nodes in exact reverse order, so `dummy.next` is the
correct returned head.

**Why no cycle remains**

The original head's link is set to null during the first iteration, establishing
the new tail. Every later processed node points only into the already reversed
portion, whose chain ends at that null. No reversed node points forward into the
unprocessed suffix.

Saving the forward link in a local variable does not keep it as a list edge.
Therefore the final structure is one acyclic chain rather than a cycle.

**Empty and one-node inputs**

If `head` is null, `curr` is null and the loop never runs. `dummy.next` remains
null and represents the reversed empty list.

For one node, its saved successor is null, its next pointer becomes the dummy's
null next, and it becomes `dummy.next`. The same node is returned with a null
successor, so no special case is needed.

**Mutation and node identity**

The method changes each original node's `next` pointer. It does not change node
values and does not create replacement data nodes, so every original node
identity appears in the result exactly once. The old `head` object becomes the
tail and is no longer the returned entry point unless the list has one node.

The commented template indicates that `ListNode` is platform-provided. The
exact `ListNode()` call assumes a constructor with default arguments. A
standalone helper requiring a value argument would need `ListNode(0)` instead.

## Complexity detail

Let $n$ be the node count. `curr` advances once per original node, and each
iteration performs a constant number of pointer assignments. Time is $O(n)$.

The method allocates one dummy node and stores a constant number of references,
so auxiliary space is $O(1)$. The output reuses input nodes and is not counted
as extra storage.

## Alternatives and edge cases

- **Previous/current iteration:** Keep `prev`, save `curr.next`, redirect to `prev`, and advance; equivalent without allocating a dummy node.
- **Recursive reversal:** Reverse the suffix, point the successor back to the head, and clear the old forward link; elegant but uses $O(n)$ stack space.
- **Value copying:** Build a new list from copied values; violates the constant-space goal and loses original node identity.
- **Empty list:** Returns null naturally.
- **Single node:** Returns the same node with its null link unchanged in effect.
- **Two nodes:** The first iteration creates the final tail; the second makes the old tail the new head.
- **Long list:** Iteration avoids recursion-limit risk.
- **Duplicate values:** Reversal depends on node order, not value uniqueness.
- **Saved successor:** Must be captured before overwriting `curr.next`.
- **Constructor defaults:** The exact dummy creation requires the platform's no-argument-compatible `ListNode` constructor.
