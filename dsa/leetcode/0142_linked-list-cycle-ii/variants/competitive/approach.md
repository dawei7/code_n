## General

**Use a fast pointer to obtain a cycle witness**

`fast` and `slow` start at the same head node. While two forward edges exist for `fast`, one iteration moves:

- `fast` two edges;
- `slow` one edge.

The tuple assignment evaluates both old pointer expressions first, so one move does not affect the other.

If `fast` reaches the end, the list is acyclic and the function returns `None`. If a cycle exists, the faster pointer eventually catches the slower pointer inside it. The source uses `fast is slow`, an identity check, so equal stored values cannot create a false meeting.

**Why different speeds guarantee the first meeting**

Once both pointers are in a cycle of length $\lambda$, consider their relative positions modulo $\lambda$. Fast gains one node per iteration because it advances two while slow advances one.

Starting from any relative offset, repeatedly adding one modulo $\lambda$ reaches zero within at most $\lambda$ steps. Zero means both references identify the same node.

This proves detection but not entry location. The meeting node depends on the noncyclic prefix length and cycle length.

**Connect travel distances to the entrance**

Let $\mu$ be the number of steps from the head to the cycle entrance, and let $b$ be the number of steps from the entrance to the phase-one meeting point.

Slow travels $\mu+b$ steps by that meeting. Fast travels twice that amount. Since they finish at the same cycle position, fast’s extra distance is some whole number $k$ of cycles:

$$
2(\mu+b)-(\mu+b)=k\lambda.
$$

Rearranging gives:

$$
\mu=k\lambda-b.
$$

Starting at the meeting point, moving $k\lambda-b$ steps goes forward from offset $b$ to offset $k\lambda$, which is the cycle entrance. Thus the distance from the head to the entrance equals a valid forward distance from the meeting point to the entrance.

**Reset one pointer and synchronize their speeds**

Immediately after finding the first meeting, the source sets `fast = head`. `slow` remains inside the cycle.

The inner loop advances both one node at a time. After $\mu$ moves, `fast` reaches the entrance from the head, while `slow` reaches the same entrance from the meeting point using the distance derived above.

The source returns `fast`, though `slow` is the identical object at that moment.

They cannot meet before the entrance: until `fast` takes $\mu$ steps, it occupies nodes in the noncyclic prefix, whereas `slow` remains in the cycle. This establishes that the returned meeting is precisely the first cycle node.

**Short cases make the control flow concrete**

For an empty list, the outer condition fails immediately.

For one node ending at `None`, `fast.next` is null and the result is `None`.

For a self-loop, the first move leaves both pointers at the only node. Resetting fast to head changes nothing, so the inner loop skips and returns that node.

If the tail points back to `head`, the prefix length is zero. Phase two returns the head without walking outside the cycle.

The algorithm reads no `pos` argument. That value belongs only to the input encoding used to construct the pointers.

**No mutation occurs**

Only local references are reassigned. The solution never changes `next` or `val`, satisfying the explicit prohibition on modifying the linked list.

The module-level `ListNode` definition is harness structure. The actual cycle algorithm uses only node identity and `next`.

## Complexity detail

Let $n$ be the number of distinct reachable nodes.

For an acyclic list, the fast pointer reaches the end after at most a linear number of moves. For a cyclic list, slow takes at most the prefix length to enter the cycle and at most $\lambda$ further relative steps to meet fast. Phase one is $O(n)$.

Phase two advances both pointers $\mu$ times, also $O(n)$. Total time is $O(n)$.

The method retains two node pointers and loop state, all independent of input size. Auxiliary space is $O(1)$, and the list itself is unchanged. These bounds match the manifest.

## Alternatives and edge cases

- **Hash set of identities:** The first repeated node is the cycle entry. It is simpler to derive but uses $O(n)$ memory.
- **Measure cycle length:** After phase-one meeting, count one lap, then separate two head pointers by that count. Advancing them together finds the entrance.
- **Brent’s method:** Power-of-two checkpoints can detect the cycle with constant memory and then support entry discovery.
- **Empty input:** Returns `None` without dereferencing a node.
- **Self-cycle:** The first identity comparison succeeds after one move.
- **No cycle:** A null fast pointer ends the outer loop, and the final return is `None`.
- **Cycle begins at head:** Resetting fast places it at the entry, and the meeting pointer is also entry-aligned modulo the cycle.
- **Repeated values:** `is` compares objects, so duplicate `val` fields are irrelevant.
- **Safe condition order:** `fast and fast.next` checks non-nullness before evaluating the second hop.
- **Immediate return after phase two:** Once both one-step pointers meet, the distance proof identifies the entry; no additional lap is required.
- **Helper `__str__` caveat:** The provided `ListNode.__str__` returns `None` in an unreachable `if self` else branch for a real instance; this representation helper is unused by cycle detection.
