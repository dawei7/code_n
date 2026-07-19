## General
**Use one completed level as the traversal path for the next**

The root level is already a one-node `next` chain. Once any level is linked, traverse its parents horizontally through those pointers instead of a queue. Because parents occur left to right, examining each parent's left child and then right child discovers the next level in exact horizontal order despite missing children.

**Head and tail pointers append only children that actually exist**

Reset `next_head` and `tail` for each parent level. The first discovered child initializes both. Every later child is attached through `tail.next` and becomes the new tail. Absent children are simply skipped; they do not create gaps in a horizontal chain.

Explicitly set the final tail's `next` to null. This makes the invariant robust even if input nodes carry stale pointer values.

**The partially built child chain is always complete through its tail**

Before scanning a level, its nodes form a complete left-to-right `next` chain ending in null. During the scan, `next_head` and `tail` delimit the correctly linked prefix of the next nonempty level.

**Trace a bridge across missing children**

For `[1, 2, 3, 4, 5, null, 7]`, scanning parents `2` then `3` discovers children `4`, `5`, and `7`. The absent left child of `3` is skipped, so the chain becomes `4 -> 5 -> 7 -> null`.

**Horizontal parent order induces exact child order**

Parents are scanned from left to right through the current `next` chain, and each parent's existing children are considered left before right. Appending those children to a dummy-headed chain therefore lists the next level in exact horizontal order while naturally skipping missing positions.

The root is a correctly formed first level. Once one level is correct, this scan constructs the next level's complete neighbor chain, so repeating links every level precisely.

## Complexity detail
Every node is visited once as a parent and appended once as a child, giving $O(n)$ time. Only a constant number of traversal and tail pointers is stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Breadth-first queue:** handles sparse trees naturally but uses $O(w)$ extra space.
- **Perfect-tree cross-parent formula:** fails when a required child is missing.
- **Recursive search for the next child:** can rescan horizontal chains and become less direct.
- Empty and one-node trees return unchanged. A level with no children produces `next_head = None` and ends the outer traversal.
- Unlike problem 116, no child can be assumed present and no direct `parent.next.left` formula is safe.
