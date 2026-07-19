## General
**Split the window around its median**

Maintain a max-heap `small` for the lower half and a min-heap `large` for the upper half. Keep either equal valid sizes or one extra valid value in `small`. The median is then the top of `small` for odd `k`, or the average of both tops for even `k`.

**Delete outgoing values lazily**

Binary heaps cannot remove an arbitrary value efficiently. Record each outgoing value in a delayed-deletion counter and decrement the logical size of the heap to which it belongs. Whenever a delayed value reaches a heap top, physically pop it and reduce its pending count. Buried stale entries remain harmless until exposed.

**Rebalance logical heap sizes**

After insertion or erasure, move one top value if `small` has more than one extra valid item or fewer valid items than `large`. Prune the source top after moving because it may expose delayed entries. These rules restore the median invariant before reading either top.

**Why duplicates remain correct**

Delayed deletion counts values rather than identities. Classifying an outgoing value relative to the current lower-half top removes one logical occurrence from the appropriate side; equal copies are interchangeable for the multiset median, and pruning consumes exactly the recorded multiplicity.

## Complexity detail
Each value is inserted, moved, and physically popped only a constant number of times, with every heap operation costing $O(\log k)$. Across `n` positions the total is $O(n \log k)$ time. Two heaps and delayed counts store $O(k)$ active or pending values.

## Alternatives and edge cases
- **Balanced ordered multiset:** supports insert, erase, and middle iterators in $O(\log k)$ where the language provides one.
- **Sorted list with binary insertion:** finds positions quickly but shifts $O(k)$ elements for each update.
- **Sort every window independently:** is simple but costs $O((n - k + 1) \cdot k \log k)$.
- **$k = 1$:** every value is its own median.
- **Even window:** average the two central values with floating-point division.
- **Duplicate outgoing value:** delayed multiplicity prevents removing too many equal entries.
- **Negative and large values:** heap ordering and averaging work without special cases.
