## General
**Discard candidates that a newer value dominates**

Maintain a deque of indices whose values are in non-increasing order. Before adding a new index, remove smaller or equal values from the back because the newer value will outlive and dominate them.

**Expire indices by position, report by value**

Remove the front index when it lies left of the current window. Once the first full window is reached, the deque front is its maximum.

The deque contains exactly the undominated indices in the current window, ordered by position from front to back and by value from largest to smallest.

Every removed-back index has a newer value at least as large, so it can never again be a maximum. Expired fronts cannot belong to the window. Therefore the surviving front is both in the window and at least as large as every other member.

An index missing from the deque is either outside the window or has a later surviving index with an equal or larger value. Following those dominance replacements always leads to a deque member, so the front represents a value at least as large as every current window element.

## Complexity detail
Each index enters and leaves the deque at most once, giving $O(n)$ time. At most `k` window indices are stored.

## Alternatives and edge cases
- **Scan every window:** costs $O(nk)$ time.
- **Heap with lazy deletion:** costs $O(n \log n)$ and retains stale entries.
- Width one returns the input values; width `n` returns one maximum; duplicates require index-based expiry.
