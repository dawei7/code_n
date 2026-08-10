## General

**Build the requested order as two stable chains**

The final list has a single boundary: every value smaller than `x` must appear before every value greater than or equal to `x`. If the final list is cut at that boundary, its left part is the original nodes satisfying `< x`, and its right part is the original nodes satisfying `>= x`.

The source constructs those two parts separately while scanning once. `l` is a dummy head for the smaller chain and `r` is a dummy head for the greater-or-equal chain. `tl` and `tr` are their current tail nodes. The dummy nodes provide a permanent starting object even when a partition is empty, eliminating special cases for assigning its first real node.

**Append rather than prepend to preserve stability**

When `head.val < x`, the source performs `tl.next = head` and advances `tl` to that node. Otherwise it performs the analogous operations through `tr`.

Each node is appended at the end of its category chain in the same order in which it is encountered. Therefore, if node `a` appeared before node `b` in the original list and both belong to the smaller partition, `a` is linked before `b`. The same statement holds for two greater-or-equal nodes. This is exactly the required stable relative order.

Prepending nodes would reverse each category and violate stability. Sorting node values would also be wrong because it would impose more ordering than the partition contract asks for.

**Reuse original nodes while keeping traversal possible**

The algorithm does not allocate copies of input nodes. After attaching the current `head` to one tail, it advances with `head = head.next`. At that moment, the current node still has its original next pointer, so the scan can reach the next original node.

This ordering is deliberate. If the code set `head.next = None` before saving or following the original successor, it would lose the rest of the input list. An alternative implementation could save `next_node = head.next`, detach the current node, append it, and then continue from the saved pointer, but the selected source delays cleanup instead.

While the scan is active, some appended tail nodes may temporarily retain original links into the other category. The final tail cleanup and concatenation repair those stale links before the result is returned.

**Why the greater tail must be terminated**

The last node appended to the greater-or-equal chain may originally have pointed to a later smaller node. After stable partitioning, that smaller node has already moved into the first chain. Leaving the original pointer intact could append an unintended suffix or even create a cycle after the chains are joined.

`tr.next = None` makes the greater-or-equal tail the actual end of the result. It is required even though the original input was a proper acyclic list, because rearranging category order changes which original links remain appropriate.

The source then connects `tl.next = r.next`, linking the smaller tail to the first real node of the greater-or-equal chain. Returning `l.next` skips the smaller dummy.

**Trace the example without changing within-group order**

For `1 -> 4 -> 3 -> 2 -> 5 -> 2` with `x = 3`, the smaller tail receives nodes with values 1, 2, and 2 in that encounter order. The other tail receives 4, 3, and 5 in its encounter order.

After terminating the second chain and connecting the first tail to its head, the result is `1 -> 2 -> 2 -> 4 -> 3 -> 5`. Notice that 4 remains before 3 even though 3 is numerically smaller; both are in the same `>= 3` category, and their relative order must be preserved.

**A two-chain invariant**

After processing any prefix of the original list, the chain after `l` contains exactly the processed nodes whose values are below `x`, in original order. The chain after `r` contains exactly the processed nodes whose values are at least `x`, also in original order. `tl` and `tr` point to the final appended nodes of their respective chains, or to the dummy when that chain is empty.

Appending the next node to its uniquely determined category preserves all parts of the invariant. Every original node is processed once and enters exactly one chain.

After the scan, concatenating smaller then greater-or-equal produces exactly the required category order. Terminating the second tail removes any obsolete original link, so the returned structure contains every original node exactly once and ends at `None`.

**Empty-category behavior comes from the dummies**

If there are no smaller nodes, `tl` is still `l`. Assigning `tl.next = r.next` makes the answer begin directly with the greater chain. If there are no greater nodes, `r.next` is `None`, so the smaller tail is terminated. If the input is empty, both dummy next pointers remain `None` and the method returns `None`.

## Complexity detail

Let $n$ be the number of nodes. The scan advances `head` once per node, and concatenation uses a constant number of pointer assignments. Total time is $O(n)$, matching the manifest.

Two dummy nodes and a constant number of pointers are stored. Original nodes are relinked rather than copied, so auxiliary space is $O(1)$, also matching the manifest. The returned list itself reuses the input storage.

## Alternatives and edge cases

- **Save and detach each successor:** Store `next_node`, set the current node's next to `None`, append it, and continue. It makes intermediate chains cleaner but uses the same asymptotic resources.
- **Partition in place around moving boundaries:** It is possible with more intricate pointer surgery, but preserving stability becomes much harder to reason about.
- **Array of node references:** Collect the two categories and relink afterward. It is straightforward but uses $O(n)$ extra space.
- **Empty list:** Both chains remain empty and `None` is returned.
- **All nodes smaller:** The greater chain is empty, and connecting to `r.next` terminates the smaller tail.
- **No nodes smaller:** The smaller dummy points directly to the complete greater chain.
- **Values equal to `x`:** Equality belongs to the greater-or-equal partition, never the smaller one.
- **Alternating categories:** Stable tail appends preserve each category's original subsequence despite extensive reordering between categories.
- **Already partitioned input:** Relinking reproduces the same logical order.
- **Greater tail cleanup:** Omitting `tr.next = None` can leave stale links or create a cycle.
- **Dummy values:** They are never returned or compared, so their stored values do not matter.
- **Input mutation:** The method intentionally changes original `next` links and returns the rearranged nodes.
