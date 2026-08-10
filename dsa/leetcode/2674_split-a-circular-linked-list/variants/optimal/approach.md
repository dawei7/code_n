## General

**The two required halves**

The input is a nonempty circular singly linked list: following `next` from the last node returns to the original head instead of reaching `null`.

The task must split its nodes, in their existing order, into two circular lists. If the original length is odd, the first list receives one more node than the second. Thus their sizes are:

$$
\left\lceil\frac{n}{2}\right\rceil
\quad\text{and}\quad
\left\lfloor\frac{n}{2}\right\rfloor.
$$

To rewire the list, the algorithm needs two boundary nodes:

- `a`, the last node of the first half;
- `b`, the last node of the original list.

Then `a.next` is the first node of the second half.

**Find the midpoint and tail together**

Both pointers start at the head:

`a = b = list`.

On each loop iteration, `a` advances by one link and `b` advances by two. This is the familiar slow-and-fast pointer idea, adapted to a circular list.

The loop continues only while:

- `b.next != list`, meaning the next step has not reached the head;
- `b.next.next != list`, meaning the second step has not reached the head.

These conditions use the known head as the stopping marker. A test for `null` would never work in a valid circular list.

**Why the loop conditions stop at the correct places**

For an odd number of nodes, the two-step pointer eventually lands on the original tail. Its next pointer is the head, so the first condition becomes false. At that moment the one-step pointer `a` is the last node of the larger first half.

For an even number of nodes, the two-step pointer eventually lands one node before the original tail. Its next node is the tail and the following node is the head, so the second condition becomes false. Again, `a` is the last node of the first half.

The loop avoids allowing `b` to wrap around and begin another lap. That is essential because a circular list has no natural terminal null pointer.

**Normalize the fast pointer to the tail**

After the loop, `b` is already the tail for odd length. For even length it is one node before the tail.

The condition `if b.next != list` distinguishes these cases:

- if `b.next == list`, `b` is already the tail;
- otherwise, `b = b.next` advances it once to the tail.

After this short adjustment, the same rewiring code works for both parities.

**Identify the second head before cutting**

The statement

`list2 = a.next`

saves the first node of the second half. This must happen before changing `a.next`. Otherwise, closing the first circle would lose the only direct reference to where the second half begins.

The first result head remains the original `list`. Node order is never changed; only the two links at the split boundaries are redirected.

**Close the second circle**

Originally, tail `b` points to the original head. The assignment

`b.next = list2`

changes the tail so it points to the second half's head. The nodes from `list2` through `b` now form their own circular list.

No internal link in this range changes, so walking from `list2` visits precisely the second-half nodes in original order and then returns to `list2`.

**Close the first circle**

The assignment

`a.next = list`

changes the last node of the first half so it points back to the original head. The original head through `a` now forms the first circular list.

The solution returns `[list, list2]`, the two heads in the required order.

**Trace an even-length list**

For nodes `1 -> 2 -> 3 -> 4 -> 1`, both pointers begin at node 1.

One loop iteration moves `a` to 2 and `b` to 3. The loop then stops because `b.next` is 4 but `b.next.next` is the head.

The post-loop condition advances `b` from 3 to tail 4. `list2` becomes node 3. Redirecting 4 to 3 closes `3 -> 4 -> 3`, and redirecting 2 to 1 closes `1 -> 2 -> 1`.

Both halves contain two nodes.

**Trace an odd-length list**

For `1 -> 2 -> 3 -> 4 -> 5 -> 1`, the slow pointer ultimately reaches node 3 while the fast pointer reaches tail 5.

Because `b.next` is already the head, the post-loop adjustment does nothing. `list2` is node 4. The new circles are `1 -> 2 -> 3 -> 1` and `4 -> 5 -> 4`.

The first receives three nodes and the second receives two, as required.

**Why the sizes are correct**

Each completed fast-pointer advance covers two original links while the slow pointer covers one. Stopping immediately before the fast pointer would cross the head places `a` after half the nodes have been assigned to the first section.

For even $n$, `a` is the $n/2$-th node. For odd $n$, it is the $\lceil n/2\rceil$-th node. Therefore `list2 = a.next` begins exactly at the required second-half boundary.

**Why no node is lost or duplicated**

Before rewiring, the first segment runs from `list` through `a`, and the second runs from `list2` through `b`. These segments are consecutive, disjoint, and together contain every original node.

The two assignments only replace cross-boundary closing links. Each segment keeps all of its internal links and receives exactly one link back to its own head. Hence both outputs are circular, preserve order, and partition the original nodes.

## Complexity detail

The fast pointer makes at most one traversal around the original circle, while the slow pointer makes about half a traversal. All remaining work is a constant number of pointer reads and writes. Total time is $O(n)$ for $n$ nodes.

The algorithm uses only pointers `a`, `b`, and `list2` in addition to the provided head. It allocates no nodes and no arrays proportional to input size, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Count nodes, then walk to the midpoint:** Correct and still $O(n)$ time with $O(1)$ space, but it requires two passes instead of finding midpoint and tail together.
- **Copy nodes into an array:** Makes indexing easy but uses $O(n)$ extra space and is unnecessary.
- **Create new lists:** Violates the in-place spirit and duplicates nodes rather than reusing them.
- **Look for `null`:** Incorrect because a well-formed circular list never reaches `null`.
- **Two nodes:** The loop does not run; the tail adjustment finds node two, and each result becomes a one-node self-cycle.
- **Odd length:** The first output contains one more node than the second.
- **Even length:** The halves have equal size, and the fast pointer needs its final one-step adjustment.
- **Save `list2` too late:** Closing the first half first would lose the second head reference.
- **Forget to close the second half:** It would still point into the first list rather than form an independent circle.
- **Forget to close the first half:** Traversal from the original head would enter the second list.
- **Node identity and order:** The algorithm preserves both; only the two boundary links change.
- **Input ownership:** The original circular structure is destructively transformed into the two returned structures.
