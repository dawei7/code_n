## General

**Use a dummy node so even the only node has a predecessor**

Deleting a node from a singly linked list requires access to the node immediately before it. The middle may be the head when the list contains one node, so the source creates `dummy = ListNode(next=head)`.

The dummy is outside the original list logically, but its `next` points to the head. It gives the original head a valid predecessor and lets one pointer-rewiring statement handle every allowed length.

The method returns `dummy.next` because deleting the original head may change that pointer to `None`.

**Move fast twice as quickly as slow**

`slow` starts at the dummy, while `fast` starts at `head`. During each iteration:

- `slow` advances one node;
- `fast` advances two nodes.

The loop continues while `fast` and `fast.next` both exist. When it stops, `slow` is immediately before the node at index $\lfloor n/2\rfloor$.

Starting slow one position behind the real list is intentional. A more familiar middle-finding pattern starts both pointers at the head and leaves slow on the middle itself. Here, deletion needs the predecessor, so the dummy supplies the one-position offset.

**Check odd and even lengths**

For $n=5$, fast begins at index 0. After one iteration, slow is at index 0 and fast at index 2. After two, slow is at index 1 and fast at index 4. Because `fast.next` is absent, the loop stops. `slow.next` is index 2, which equals $\lfloor5/2\rfloor$.

For $n=4$, after one iteration slow is index 0 and fast is index 2. A second iteration moves slow to index 1 and fast beyond the list. `slow.next` is index 2, the required later of the two central positions.

For $n=1$, the loop never runs because `head.next` is absent. Slow remains at the dummy, and its next node is the sole node, index 0.

These traces show that the same condition implements the stated middle definition for both parities.

**Bypass the middle node**

After the loop, deletion is one link update:

`slow.next = slow.next.next`.

Before the assignment, `slow.next` is the middle node. Its `next` is the node after the middle, possibly `None`. Redirecting the predecessor to that successor removes the middle from the reachable chain.

The deleted node object may still exist temporarily as a Python object, but it is no longer reachable from the returned head. The task asks for the modified linked-list structure, which this bypass provides.

**Why the pointer position is correct**

After $t$ loop iterations, fast has moved to original index $2t$ when that index exists, while slow has moved from the dummy to original index $t-1$ for $t>0$.

For odd $n=2q+1$, the loop runs $q$ times and stops with fast at the last node. Slow is at index $q-1$, directly before middle index $q=\lfloor n/2\rfloor$.

For even $n=2q$, the loop runs $q$ times and fast becomes `None`. Slow is again at index $q-1$, before required middle index $q$.

For $n=1$, the dummy is the predecessor of index 0. Thus the link update is safe for every valid nonempty list.

**Why exactly one node is removed**

Only one `next` field changes. All nodes before `slow` retain their connections. `slow` now points to the former middle successor, so all nodes after the middle remain in their original order. The middle is the only node skipped.

The input contract guarantees at least one node, so `slow.next` exists when the assignment executes.

## Complexity detail

Let $n$ be the number of nodes.

Fast advances over the list two nodes at a time, so the loop performs at most $\lfloor n/2\rfloor$ iterations. Each does constant pointer work, and deletion is constant time. Total time complexity is $O(n)$.

The method stores one dummy node and two pointers. It does not allocate an array, recurse, or copy list nodes, so auxiliary space is $O(1)$.

The list is mutated in place by changing one link. The dummy is a constant-size helper and is not part of the returned list.

## Alternatives and edge cases

- **Count nodes in a first pass:** A second pass can stop at the predecessor of index $\lfloor n/2\rfloor$. This is correct and $O(n)$, but fast/slow pointers find the position in one traversal.
- **Store all nodes in an array:** Direct indexing makes deletion easy but requires $O(n)$ extra space.
- **Start slow at the head:** That common pattern locates the middle node, not its predecessor. An additional previous pointer or different fast initialization would then be needed.
- **Special-case one node:** Returning `None` explicitly works, but the dummy makes the general bypass handle it naturally.
- **One-node list:** Slow remains at the dummy, bypassing the head and returning `None`.
- **Two-node list:** The required middle is index 1. One iteration leaves slow at index 0, which bypasses the second node.
- **Odd length:** The unique central node is removed.
- **Even length:** The definition chooses index $n/2$, the second central node; the loop's stopping rule targets it.
- **Middle is the tail:** This occurs for length two. `slow.next.next` is `None`, safely shortening the list.
- **Preserving order:** No values are copied or swapped; every surviving node remains in its original relative order.
- **Nonempty guarantee:** The exact source assumes `head` exists. An empty list would make `slow.next.next` invalid, but it lies outside the allowed input.
- **Input mutation:** Callers holding the original nodes observe the changed link after the method returns.
