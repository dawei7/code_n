## General

**Why counting from the end is awkward in a singly linked list**

A singly linked node points only to its successor. Starting from `head`, the program can move toward the tail, but it cannot move backward from the tail to find the $n$th node from the end. A direct solution could first count the list length and then make a second walk to the desired predecessor. The selected implementation instead uses two pointers separated by a fixed distance, so the location is found in one coordinated forward traversal.

The constraint $1 \le n \le sz$ guarantees that the node to remove exists. The method therefore does not contain error handling for an out-of-range `n`.

**Use a dummy node so the head is not a special case**

Deletion in a singly linked list is performed by changing the predecessor's `next` link. If the real head must be deleted, however, there is no real predecessor. The line

```python
dummy = ListNode(next=head)
```

creates a temporary predecessor before `head`. Now every removable node—including the original head—has a predecessor. The algorithm can use the same assignment in every case:

```python
slow.next = slow.next.next
```

The returned head is `dummy.next`, not necessarily the original `head`. When the original head is removed, `dummy.next` has been redirected to the second node or to `None`. In all other cases it still points to the original head.

The dummy node is an implementation aid only. It is not included in the returned list, and its default value is irrelevant because the algorithm never examines it.

**Create an $n$-edge lead**

Both pointers initially reference `dummy`:

```python
fast = slow = dummy
```

The `for` loop moves `fast` exactly `n` links forward while `slow` stays in place. After those moves, `fast` is $n$ node positions ahead of `slow`. It is useful to number the dummy as position $0$ and the real nodes as positions $1$ through $sz$. At this moment, `slow` is at position $0$ and `fast` is at position $n$.

The code advances only `n` times, not `n + 1`, because its later loop stops when `fast` is the tail rather than when `fast` has passed the tail. These two common formulations are equivalent when their stopping conditions are paired correctly. Mixing `n` steps with a `while fast` condition would place `slow` one node too far; mixing `n + 1` steps with `while fast.next` could dereference beyond the list.

**Preserve the gap until the fast pointer reaches the tail**

The loop

```python
while fast.next:
    slow, fast = slow.next, fast.next
```

moves both pointers one link at a time. Moving them together preserves their $n$-position separation. The loop continues while `fast` has a successor, so it ends with `fast` on the last real node at position $sz$.

If both pointers moved $sz-n$ times, then `slow` ends at position

$$
0+(sz-n)=sz-n.
$$

The $n$th node from the end is the $(sz-n+1)$th node from the beginning. Therefore position $sz-n$ is exactly its predecessor. This is why the code deliberately stops `slow` one node before the node being removed rather than on the node itself.

The simultaneous assignment evaluates both right-hand expressions using the old pointer values before updating either name. It is just a compact way to advance both pointers once; it does not make `fast` depend on the newly advanced `slow`.

**Bypass exactly one node**

At loop termination, `slow.next` is the target node and `slow.next.next` is the node after it, possibly `None`. Assigning the latter to `slow.next` removes the target from the chain reachable from `dummy`. No values are copied, and no other links are rearranged.

This operation works for every location:

- Removing the head leaves `slow` at `dummy`, so `dummy.next` skips the original head.
- Removing an interior node links its real predecessor directly to its successor.
- Removing the tail assigns `None` to the previous node's `next`.
- Removing the only node changes `dummy.next` from that node to `None`.

**Trace `head = [1, 2, 3, 4, 5]`, `n = 2`**

Think of the dummy as position zero. After two lead steps, `fast` points to node `2` and `slow` points to the dummy. The paired loop then produces these positions:

| Moment | `slow` | `fast` |
|---|---:|---:|
| After lead creation | dummy | `2` |
| After one paired move | `1` | `3` |
| After two paired moves | `2` | `4` |
| After three paired moves | `3` | `5` |

`fast.next` is now `None`, so `slow` correctly points to `3`, the predecessor of the second node from the end (`4`). Replacing `slow.next` with `slow.next.next` connects `3` directly to `5`, yielding `[1, 2, 3, 5]`.

**Why the method is correct**

After the lead loop, the invariant is that `fast` is exactly $n$ positions ahead of `slow`. Each paired move preserves that invariant. The second loop can only terminate with `fast` on the tail, because it continues precisely while a next node exists. Consequently, `slow` must be $n$ positions before the tail, which is the predecessor of the $n$th node counted from the tail. The bypass changes exactly that predecessor's link, so exactly the requested node becomes unreachable from the returned head. The valid-`n` guarantee ensures every dereference used in this argument exists.

## Complexity detail

Let $sz$ be the number of real list nodes.

- **Time complexity: $O(sz)$.** `fast` first makes `n` moves. Then both pointers make `sz - n` moves until `fast` reaches the tail. The total number of pointer advances is linear: `fast` traverses exactly `sz` links from the dummy to the tail, and `slow` traverses at most `sz - 1`. There is no nested traversal.
- **Auxiliary space: $O(1)$.** The method stores one dummy node, two pointer variables, and loop state regardless of list length. It reuses the original nodes rather than building a replacement list. The input list itself and the returned list are not extra space.

The one-pass follow-up means the list length is not computed in a separate complete traversal. Although different pointers visit some nodes at different times, the algorithm is still a single two-pointer sweep with constant work per pointer move.

## Alternatives and edge cases

- **Two-pass length calculation:** First compute $sz$, then walk $sz-n$ steps from a dummy to the predecessor. It is also $O(sz)$ time and $O(1)$ space, but performs a conceptually separate length pass.
- **Stack of node references:** Push every node, then pop `n` positions to find the target or predecessor. It is intuitive for backward counting but requires $O(sz)$ extra space.
- **Recursive unwinding:** Count positions from the end while recursive calls return. This mirrors the requested direction but consumes $O(sz)$ call-stack space and risks recursion limits.
- **Copy into an array:** An array gives direct indexing from the end, but it uses $O(sz)$ storage and still requires repairing links.
- **`n = 1`:** `fast` reaches the tail with `slow` at the penultimate node, so the final node is removed.
- **`n = sz`:** The lead loop places `fast` at the tail immediately; the paired loop does not run, `slow` remains at the dummy, and the head is removed.
- **Single-node list:** This is the `n = sz = 1` case; `dummy.next` becomes `None`, and the returned list is empty.
- **Node values are irrelevant:** The algorithm uses only links and positions. Duplicate values do not affect which node is removed.
- **Mutation semantics:** The original chain is modified in place. Any external reference to the removed node still names that object, but the node is no longer reachable by following `next` from the returned head.
- **Invalid `n`:** The source assumes the stated contract. If `n` exceeded the length, the lead loop would eventually try to follow `next` from `None`; validation would be required only for a broader API.
