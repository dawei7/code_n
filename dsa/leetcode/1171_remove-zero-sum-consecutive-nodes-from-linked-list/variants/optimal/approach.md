## General

**Equal prefix sums reveal a zero-sum block**

Let the prefix sum at a node mean the sum from a position before the list through that node. If two positions have the same prefix sum, then the nodes strictly after the first position through the second position contribute zero:

`prefix(B) - prefix(A) = 0`.

Therefore, those consecutive nodes may be removed by connecting `A.next` directly to `B.next`.

This converts the search for arbitrary zero-sum sequences into repeated-prefix detection.

**Add a dummy node for blocks beginning at the head**

`dummy = ListNode(next=head)` creates a zero-valued node before the original head. Its prefix sum is zero.

If an initial block of real nodes sums to zero, the prefix sum at its final node is also zero. Treating the dummy as the earlier equal-prefix position lets the same pointer-rewiring rule delete that head block. No separate head special case is needed.

The method ultimately returns `dummy.next`, which is the possibly changed head of the final list.

**First pass: remember the last node for every prefix sum**

Starting at `dummy` with `s = 0`, the first loop adds each node's value and assigns

`last[s] = cur`.

When a prefix sum repeats, the newer node overwrites the older map value. After the pass, `last[s]` is the farthest node in the original list having prefix sum `s`.

Keeping the last occurrence is deliberate. When the second pass reaches an earlier position with prefix `s`, jumping past the farthest equal-prefix node removes the largest zero-sum interval beginning immediately after that position. This also absorbs nested or overlapping zero-sum blocks that might otherwise require repeated deletions.

**Second pass: bypass every removable interval**

The second traversal resets `s` and `cur` to the dummy. At each currently reachable node, it rebuilds that node's prefix sum and performs

`cur.next = last[s].next`.

If the current node itself is the last occurrence of `s`, the assignment leaves its next pointer unchanged.

If a later node `B = last[s]` has the same prefix, all nodes from `cur.next` through `B` sum to zero. Setting `cur.next` to `B.next` removes exactly that block from the reachable linked list.

After rewiring, `cur = cur.next` advances through the shortened list. Nodes that were bypassed are never processed again in the second pass.

**Trace the first example**

For `[1, 2, -3, 3, 1]`, the prefix sums including the dummy are:

`0, 1, 3, 0, 3, 4`.

The last occurrence of zero is the node containing negative three. During the second pass at the dummy, the code connects directly to the node after negative three, removing `1, 2, -3`.

The remaining reachable list is `[3, 1]`, which contains no zero-sum consecutive sequence.

The later occurrence of prefix three also supports a different valid removal order in the original list, which explains why the problem may accept more than one final answer. Choosing last occurrences consistently produces one valid normal form.

**Why one large jump handles repeated deletion**

A naive process could find one zero-sum block, remove it, then restart because the deletion might make a new zero-sum block adjacent. Prefix sums over the original list already encode these combined possibilities.

If several removable blocks overlap or become adjacent after deletions, the farthest repeated prefix captures their union as one zero-sum interval from the current position. The second pass's rewiring therefore performs the effect of repeated deletions without rescanning from scratch.

**Why the algorithm is correct**

Every pointer jump is safe: it skips from a node with prefix sum `s` past a later node with the same prefix, so the removed consecutive values sum to zero.

After applying the jump for every reachable prefix position, suppose a zero-sum consecutive block remained. The prefix sum before that block and at its end would be equal. The first pass would have mapped that sum to an occurrence at least as late as the block's end, so when the second pass visited the block's preceding reachable node, it would have jumped beyond the block. This contradiction shows no zero-sum block remains.

Only zero-sum sequences are removed, and the relative order of every retained node is unchanged. Thus the returned list is a valid result.

## Complexity detail

Let `n` be the number of original nodes. The first pass visits each node once, and the second pass visits each node that remains reachable at most once. Total time is `O(n)` with expected constant-time dictionary operations.

The `last` dictionary stores at most one entry per distinct prefix sum, no more than `n + 1` including the dummy. Auxiliary space is `O(n)`.

The algorithm reuses original nodes and modifies their `next` pointers. It allocates only one additional dummy node.

## Alternatives and edge cases

- **Try every starting node and accumulate forward:** This can find zero-sum blocks but takes `O(n^2)` time in the worst case.
- **One-pass prefix map with cleanup:** On a repeated prefix, immediately remove the interval and delete its intermediate prefix sums from the map. It is also linear amortized but has more delicate bookkeeping.
- **Store the first prefix occurrence:** That may remove a smaller interval and leave cascading work. The two-pass method relies on the farthest occurrence.
- **Zero-sum prefix:** Repeated prefix zero connects the dummy past the removable initial block.
- **Entire list sums to zero:** `last[0]` is the tail, so `dummy.next` becomes null and an empty list is returned.
- **A node with value zero:** Prefix sum repeats at that node, and the node is bypassed.
- **No repeated prefix sums:** Every `last[s]` is the current node itself, so all links remain unchanged.
- **Nested zero-sum sequences:** Last occurrences let one pointer jump remove the larger encompassing block.
- **Multiple valid answers:** The problem permits any list obtainable after repeated legal deletions. This strategy deterministically favors farthest repeated-prefix jumps.
- **Input mutation:** Retained original nodes are relinked in place. A caller needing the untouched list would have to clone it first.
- **Dummy node:** Its zero value is essential for applying the same prefix rule to removals beginning at the original head.
