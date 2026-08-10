## General

**Identify the two splice boundaries**

The nodes at indices `a` through `b` in `list1` must disappear from the returned chain. The list therefore needs two new connections:

1. node `a - 1` of `list1` must point to the head of `list2`;
2. the tail of `list2` must point to node `b + 1` of `list1`.

The constraints guarantee `a >= 1` and `b < list1.length - 1`, so both boundary nodes exist. There is always a node before the removed segment and a node after it, which lets the implementation avoid dummy-head special cases.

**Locate the predecessor and the removed segment’s last node**

Both pointers `p` and `q` begin at the head, which is index zero.

The first loop advances `p` exactly `a - 1` times. Each step follows one `next` edge, so `p` finishes at index `a - 1`.

The second loop independently advances `q` exactly `b` times from the head. It therefore finishes at index `b`, the last node that must be removed.

Starting both searches at the head repeats some traversal, but keeps the index reasoning simple. It does not change the worst-case linear bound.

At this point:

- `p.next` is the original node at index `a`;
- `q.next` is the original node at index `b + 1`;
- the chain from `p.next` through `q` is precisely the segment being replaced.

**Connect the prefix to `list2`**

`p.next = list2` overwrites the predecessor’s old link into the removed segment. The prefix of `list1` from its head through index `a - 1` now flows directly into the head of `list2`.

The variable `p` is then deliberately reused to find the tail of the inserted list. The loop `while p.next: p = p.next` begins at the predecessor. Its first step enters `list2` because of the newly assigned link, then continues until `p.next` is `None`. Because `list2` is guaranteed nonempty and originally terminates at null, `p` finishes at its tail.

Reusing `p` avoids another named pointer, but the explanation must remember that `p` no longer denotes node `a - 1` after this loop.

**Connect the inserted tail to the suffix**

`p.next = q.next` makes the tail of `list2` point to original node `b + 1`. The visible result is now:

the prefix of `list1`, followed by all of `list2`, followed by the suffix after `b`.

The order of the final statements matters. The source reads `q.next` and installs it as the inserted tail’s successor before executing `q.next = None`. If `q.next` were cleared first without saving it, the only convenient pointer to the suffix boundary would be lost.

Setting `q.next = None` is not required to make the returned head traverse correctly, because the removed segment was already disconnected from the prefix. It cleanly detaches its final node from the retained suffix, ensuring that the old removed chain does not keep a second outgoing reference into the result.

**A trace**

For `list1 = [10, 1, 13, 6, 9, 5]`, `a = 3`, and `b = 4`, `p` stops at value `13` at index two, while `q` stops at value `9` at index four. The suffix head is `q.next`, the node containing `5`.

After `p.next = list2`, value `13` points to `1000000`. Walking `p` reaches `1000002`, the inserted tail. Linking that tail to `q.next` attaches value `5`. Clearing `q.next` detaches value `9` from `5`. Returning the original head yields `[10, 1, 13, 1000000, 1000001, 1000002, 5]`.

**Why the resulting chain is correct**

Nodes before `a` retain all original links except the one from index `a - 1`, so the prefix is preserved in order. That changed link enters `list2` at its head, and no internal `list2` link is changed until its tail, so all inserted nodes appear in order. The tail then points to original index `b + 1`, whose following links remain unchanged, preserving the suffix.

No returned path reaches any node from original indices `a` through `b`. Conversely, every node outside that interval and every node in `list2` is reachable exactly once from `list1`’s head. Therefore the returned original head represents precisely the required merged list.

## Complexity detail

Let `n` be the length of `list1` and `m` the length of `list2`. The two boundary loops take `a - 1` and `b` steps, and the tail scan takes `m` steps plus the transition from the predecessor. Total time is $O(a + b + m)$, which is $O(n + m)$ in the worst case.

The algorithm allocates no new list nodes or growing data structure. It stores only pointer variables and loop counters, so auxiliary space is $O(1)$.

The input lists are mutated in place. The output reuses the original `list1` prefix and suffix nodes and every `list2` node.

## Alternatives and edge cases

- **Single traversal for both boundaries:** Advance one pointer through `list1` and record nodes at `a - 1` and `b`. This reduces repeated prefix walking but keeps the same $O(n+m)$ asymptotic time.
- **Copy values into an array and rebuild:** This is straightforward but allocates $O(n+m)$ storage and new nodes, losing the linked-list advantage.
- **Dummy head:** A dummy predecessor simplifies a generalized version where `a` may be zero. The stated `a >= 1` guarantee makes it unnecessary here.
- **One-node replacement interval:** When `a == b`, `p` and `q` bracket exactly one removed node, and the same two splice links work unchanged.
- **`list2` has one node:** After the prefix link, the tail-search loop enters that node and stops; it is then connected to the suffix.
- **Removal near the front:** Since `a` may be one, the first loop can run zero times and `p` remains the original head, correctly preserving index zero.
- **Removal near the back:** `b` may be the second-to-last index, so `q.next` is the original tail and remains a valid suffix.
- **Save suffix before detaching:** `p.next = q.next` must precede `q.next = None` unless the suffix pointer is stored separately.
- **Old removed nodes:** They are not explicitly freed. They become unreachable from the returned list, and normal memory management can reclaim them when no external references remain.
- **Aliasing outside the contract:** The proof assumes `list1` and `list2` are separate ordinary acyclic lists. Shared nodes could create cycles or duplicate paths, but the problem supplies standard independent inputs.
