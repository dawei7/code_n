## General
**Traverse real and missing positions in level order.** Initialize a queue with the root. Whenever a real node is removed, append both child references, including `None` for a missing child. This produces the conceptual array order of a binary heap without materializing entire empty levels.

**Remember the first gap.** When a `None` entry is removed, set a flag indicating that a missing position has appeared. Every later queue entry in a complete tree must also be `None`; encountering a real node after the flag is set proves that some available position to its left was skipped.

**Accept only a contiguous prefix of nodes.** If traversal finishes without such a later real node, all occupied level-order positions form a contiguous prefix. That condition means all earlier levels are full and the final level is filled from left to right, exactly matching completeness. Conversely, any incomplete placement has a first missing position followed by a real node, which the scan rejects.

## Complexity detail
Each of the $N$ nodes is removed once and contributes two child references. Queue work is $O(N)$ time, and the queue may contain $O(N)$ entries at the widest level, using $O(N)$ space.

## Alternatives and edge cases
- **Heap-index characterization:** Give the root index 1 and children indices `2 * index` and `2 * index + 1`; the tree is complete exactly when the maximum index equals $N$. This is also linear when the maximum is tracked incrementally.
- **Repeated index maximum:** Recomputing the maximum over all collected heap indices after every visited node remains correct but costs $O(N^2)$ time.
- **Level-width bookkeeping:** Verify full widths before the last level and left-packed children within the last. This works but requires more boundary cases than the gap flag.
- **Single node:** A root with no children is complete.
- **Right child without left child:** The right child appears after a missing left position and must be rejected.
- **Gap above the last occupied level:** Any descendants after that gap likewise make the tree incomplete.
