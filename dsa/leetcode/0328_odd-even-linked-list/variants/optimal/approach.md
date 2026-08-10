## General

**“Odd” and “even” refer to positions, not values.**

The first node belongs to the odd-position group, the second belongs to the even-position group, the third is odd-positioned, and so forth. A node's stored `val` has no influence on its group. For example, a node containing the even value `6` belongs to the odd group if it was originally at position five.

The output must contain the same node objects, first in original positions `1,3,5,...` and then in original positions `2,4,6,...`. Relative order within each group must remain unchanged. Allocating arrays of nodes would make the grouping easy, but the $O(1)$ extra-space requirement points to rewiring the existing `next` links as the list is traversed.

**Maintain two chains inside the original nodes.**

After rejecting an empty list, the source establishes three pointers:

- `a = head`: the current tail of the odd-position chain;
- `b = head.next`: the current tail of the even-position chain;
- `c = head.next`: the permanent head of the even-position chain.

Initially, the first node is already the odd chain's tail and the second node, if it exists, is already the even chain's head and tail. The pointer `c` must never advance because the final step needs to append the complete even chain after the odd chain. In contrast, `b` advances as that chain grows.

The assignment `b = c = head.next` does not copy a node. Both variables initially refer to the same second node. Later, reassigning `b` changes only the variable `b`; `c` continues to refer to the saved even head.

**The loop invariant.**

Before each loop iteration:

- `a` is the last odd-position node already placed in odd order;
- `b` is the last even-position node already placed in even order;
- `c` is still the original second node;
- if another pair remains, `b.next` is the next odd-position node, and the node after that is the next even-position node.

The original list alternates positions, so the next unprocessed odd node is directly after the current even tail. This layout lets the algorithm extract one odd node and then one even node using only local links.

The guard `while b and b.next` checks exactly what the iteration needs. `b` must exist, and there must be a next odd-position node to move into the odd chain. The node after that odd node is allowed to be absent; this occurs when the input has odd length, and the assignments handle it naturally.

**Move the next odd-position node.**

The first assignment is

`a.next = b.next`.

At this moment, `b.next` is the next original odd-position node. Linking the current odd tail `a` to it extends the odd chain in its original order. Then

`a = a.next`

advances `a` so it again names the last processed odd node.

No node is cloned, and no value is copied. Only the pointer from the old odd tail is redirected. Because the next odd node is taken from the leftmost unprocessed position, odd-group stability is preserved.

**Move the next even-position node.**

After `a` advances, `a.next` is the node originally following that odd node. If it exists, it is the next even-position node; if it does not, the list ended at an odd position.

The assignment

`b.next = a.next`

therefore extends the even chain or terminates it with `None`. Then

`b = b.next`

advances the even tail. It may make `b` equal to `None` at the end of an odd-length input, which is safe because the next loop-condition check stops.

These four pointer assignments preserve the invariant while consuming the next odd/even pair, or the final lone odd node. Each group's nodes are appended in the same order in which they appeared in the input, satisfying the stability requirement.

**Walk through `[1,2,3,4,5]`.**

Initially, `a` points to node `1`, while `b` and `c` point to node `2`.

During the first iteration:

- `a.next = b.next` links `1` to `3`;
- `a` advances to `3`;
- `b.next = a.next` links `2` to `4`;
- `b` advances to `4`.

The partial odd chain is `1 -> 3`, and the partial even chain is `2 -> 4`. Node `5` is still reachable as `b.next`.

During the second iteration:

- link `3` to `5` and advance `a` to `5`;
- assign `4.next = 5.next`, which is `None`;
- advance `b` to `None`.

The separated chains are now `1 -> 3 -> 5` and `2 -> 4`. Finally, `a.next = c` links node `5` to the saved even head `2`, producing

`1 -> 3 -> 5 -> 2 -> 4`.

**Join the chains exactly once.**

When the loop ends, `a` is the last odd-position node. The statement `a.next = c` appends the even chain after it. This works for both parities:

- with odd length, the final iteration has already set the final even node's `next` to `None`;
- with even length, `b` is the final even node and already ends the original list.

If the list contains only one node, `c` is `None`, the loop is skipped, and `a.next = c` simply preserves the one-node termination. If it contains two nodes, the loop is also skipped and the first node is linked to the already saved second node, leaving the correct order unchanged.

The function returns the original `head` because position one is the first odd-position node and must remain the output head.

**Why every node appears exactly once.**

Each iteration takes the next unprocessed odd node and, when available, the next unprocessed even node. Pointers only move forward along original order; no processed node is selected again. The odd chain receives all and only original odd positions, and the even chain receives all and only original even positions. Their groups are disjoint and together contain every original position. Joining the two tails therefore creates the required permutation without loss, duplication, or a cycle.

## Complexity detail

Let $n$ be the number of nodes. Each iteration advances `a` by one odd-position node and `b` by one even-position node. There are at most $\lfloor n/2\rfloor$ iterations, and every operation inside is constant time. Total time complexity is $O(n)$.

The method uses only `a`, `b`, and `c` in addition to the existing `head` reference. It allocates no nodes, array, set, or recursion stack, so auxiliary space is $O(1)$. The rewired list itself is the required output and does not count as extra storage.

## Alternatives and edge cases

- **Copy values into odd and even arrays:** Collect positions into two temporary lists and rewrite or rebuild the result. This is straightforward but requires $O(n)$ extra space and may violate the requirement to preserve the same nodes rather than merely their values.

- **Create two dummy-headed linked lists:** Append alternating original nodes to odd and even chains, then connect them. This can still use $O(1)$ auxiliary node references, but dummy node allocation is unnecessary because the first and second nodes already provide natural heads.

- **Swap node values:** Rearranging values instead of links can produce the visible sequence, but it changes which logical node occupies each position and is undesirable when node identity matters. The source correctly rewires nodes.

- **Empty list:** The early `head is None` check returns `None` before dereferencing `head.next` or `a.next`.

- **One node:** `b` and `c` are `None`; the loop skips, the sole node remains the odd chain, and the returned head is unchanged.

- **Two nodes:** `b` exists but `b.next` does not, so no loop iteration is needed. Appending `c` leaves `first -> second`.

- **Odd number of nodes:** The final iteration consumes a lone odd node, sets the even tail's next link to `None`, and then appends the saved even head after that odd tail.

- **Even number of nodes:** The loop stops with `b` at the final even node. The last odd tail is then connected to `c`, while the final even node retains its terminating `None`.

- **Repeated or extreme values:** Values are never compared, so duplicates and the full allowed numeric range have no effect. Only original positions determine the grouping.

- **Saving `c` is mandatory:** If the code kept only the moving even pointer `b`, it would lose the even chain's head and could not attach that entire chain after the odd tail at the end.
