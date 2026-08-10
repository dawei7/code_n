## General

**Use the existing absolute-value order**

The input is not arbitrarily ordered. As the list is traversed, absolute values never decrease.

For nonnegative nodes, actual value equals absolute value. Their current relative order is already non-decreasing and should be preserved.

For negative nodes, larger absolute value means a smaller actual value. Thus negative values appear in the reverse of the order they need: a traversal might encounter `-1`, then `-3`, then `-8`, while sorted actual order requires `-8,-3,-1`.

The source exploits these two facts rather than applying a general linked-list sort.

**Move each later negative node to the front**

`prev` initially points to `head` and `curr` to `head.next`. While `curr` exists, a negative current node is detached from its present location and inserted before the current head.

The exact pointer sequence is:

- save `curr.next` in `t`;
- connect `prev.next` to `t`, removing `curr` from the middle;
- set `curr.next = head`;
- set `head = curr`;
- continue scanning from `t`.

This is a front insertion using the existing node. No value is copied and no new list node is allocated.

**Why `prev` must stay still after a removal**

When `curr` is removed, `prev.next` becomes `t`. The node `prev` is still the predecessor of the next unprocessed node, so advancing it would skip the new link.

The source keeps `prev` unchanged and assigns `curr=t`. If that next node is also negative, it can be detached through the same predecessor.

When `curr` is nonnegative, no link changes. Both pointers safely advance one node.

**Why repeated front insertion sorts all negatives**

Because absolute values are non-decreasing, each newly encountered negative node has absolute value at least as large as every negative encountered earlier. Its actual signed value is therefore less than or equal to those earlier negative values.

Inserting it at the front places it before values that are greater than or equal to it. Repeating this reverses the encounter order of the negative subsequence, which is exactly its non-decreasing signed order.

Equal negative values may reverse their node identity order, but their values are equal, so sortedness is unchanged.

**What happens when the original head is negative**

The loop never explicitly removes the initial head. That is correct. Under absolute-value order, if the head is negative, it has the smallest absolute value among negative nodes and therefore the greatest actual negative value.

Every later negative node is inserted before it. The original head naturally becomes the last node of the final negative block, exactly where the least-negative value belongs.

**Why nonnegative order remains correct**

Nonnegative nodes are never moved relative to each other. Detaching a negative node merely links its predecessor directly to its successor; it does not swap two retained nonnegative nodes.

Since their original order by absolute value is also order by actual value, the remaining nonnegative chain is sorted.

**Why every negative ends before every nonnegative**

Every negative node after the head is moved to the very front. If the head is negative, it already precedes the retained nonnegative chain. If the head was nonnegative, the first encountered negative becomes the new head, and later negatives are placed before it.

Thus the final list consists of a sorted negative block followed by the original sorted nonnegative block. Every negative value is less than every nonnegative value, so their concatenation is globally non-decreasing.

**Trace the main example**

Start with `0 -> 2 -> -5 -> 5 -> 10 -> -10`.

Zero and two remain. When negative five is reached, it is detached after two and inserted at the head, producing `-5 -> 0 -> 2 -> 5 -> 10 -> -10`.

The scan continues through five and ten. Negative ten is then detached and placed at the front, producing `-10 -> -5 -> 0 -> 2 -> 5 -> 10`.

The list now has the required actual-value order.


After processing up to `prev`, all encountered negative nodes form a non-decreasing block at the front, and all encountered nonnegative nodes follow in their original non-decreasing order. `curr` begins the unprocessed remainder.

A nonnegative `curr` extends the second block without violating it. A negative `curr` is no greater than the front block's current first value because its absolute value is no smaller, so placing it at the front preserves the negative block's order. The invariant holds after either case.

At loop termination no unprocessed node remains, so the whole list is sorted.

## Complexity detail

Let $N$ be the number of nodes. Each node becomes `curr` at most once. Detachment and front insertion use a constant number of pointer assignments, so total time is $O(N)$.

The algorithm stores only `head`, `prev`, `curr`, and temporary `t` references. It reuses all existing nodes and uses $O(1)$ auxiliary space. The original linked structure is mutated and the returned head may differ from the input head.

## Alternatives and edge cases

- **General merge sort:** Sorts any linked list in $O(N\log N)$ time, but ignores the stronger absolute-order guarantee.
- **Collect values in an array:** Sort and write them back, using $O(N)$ space and $O(N\log N)$ time.
- **Separate and reverse negatives:** Build negative and nonnegative chains, reverse the negative chain, then concatenate; also $O(N)$ time and $O(1)$ space.
- **All nonnegative:** No node moves and the original list is returned unchanged.
- **All negative:** Repeated front insertion reverses the entire encounter order.
- **Single node:** `curr` is null and the node is already sorted.
- **Zero:** Treated as nonnegative and remains before positive values.
- **Equal absolute values with opposite signs:** The negative is moved before the positive, producing correct signed order.
- **Consecutive negative nodes:** `prev` intentionally remains fixed while each is detached.
- **Original negative head:** Later negatives move before it; it need not be handled separately.
- **Node identity:** Nodes are relinked rather than recreated.
- **Input mutation:** The original list links are changed in place.
