## General

**Split the window around its median**

Maintain a max-heap `small` for the lower half and a min-heap `large` for the upper half. Negate values stored in
`small` so that its root is the largest lower-half value. Track valid heap sizes separately from physical lengths and
keep either equal valid sizes or one extra valid value in `small`. The odd-window median is then the root of `small`;
an even-window median is the mean of both roots.

**Remove outgoing occurrences lazily**

A binary heap cannot efficiently locate an arbitrary departing value. Increment its count in `delayed`, decrement
the logical size of the side containing it, and physically pop it only when that value reaches a heap root. Delete a
counter key when its last pending occurrence is consumed. Classifying an outgoing value relative to the valid lower
root is sound even with duplicates: equal occurrences are interchangeable in the window multiset, while the counter
still removes exactly the required multiplicity.

After each insertion or erasure, move roots until `small_size` is either equal to `large_size` or one larger. Prune a
source heap after a move in case removing its root exposes a delayed value. These steps restore the partition and
size invariants before the next median is read.

**Compact buried tombstones before they exceed the window scale**

Lazy deletion alone does not bound Python heap storage: on a monotone input, departed values can remain below a heap
root indefinitely. When the two physical heaps together exceed `2 * k` entries, scan both arrays once. Consume the
recorded delayed multiplicities, retain only live entries, rebuild both heaps, derive their exact live sizes, and
rebalance them. If equal boundary values are consumed from a different side than the logical classification used at
erasure time, rebalancing is sufficient because those equal occurrences have identical ordering value.

Compaction leaves exactly the current window multiset in the two heaps. Between compactions, every new tombstone
represents one departed occurrence and the physical total remains at most a constant multiple of `k`, so delayed
state cannot grow without bound.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Ordinary insertion, root movement, and pruning use heaps whose physical sizes
are $O(k)$, so each heap operation costs $O(\log k)$. A compaction scans and heapifies $O(k)$ entries, but it occurs
only after $\Omega(k)$ unpruned departures have accumulated. Its $O(k)$ work is therefore amortized across those
window shifts. Total time is $O(n \log k)$.

The heaps contain at most a constant multiple of `k` entries. The delayed counter has at most one key per retained
tombstone, and compaction uses another $O(k)$ temporary collection. Auxiliary space is $O(k)$.

## Alternatives and edge cases

- **Unbounded lazy-deletion heaps:** the protected Accepted implementation has correct median logic and
  $O(n \log k)$ time, but buried tombstones and zero-count counter keys can accumulate to $O(n)$ physical storage.
- **Balanced ordered multiset:** supports insertion, erasure, and middle iterators in $O(\log k)$ where the language
  provides such a structure.
- **Sorted list with binary insertion:** finds an update position in $O(\log k)$ but may shift $O(k)$ elements.
- **Sort every window independently:** is direct but costs $O((n-k+1) \cdot k \log k)$ time.
- **`k = 1`:** every value is its own median, and each outgoing root is pruned immediately.
- **Even window:** compute the mean of the two central values with floating-point division.
- **Duplicate boundary values:** delayed multiplicities may be consumed from either heap; compaction then rebalances
  the equal-valued partition without changing the multiset.
- **Negative and 32-bit boundary values:** sign inversion in `small` and Python's unbounded integer addition preserve
  ordering and avoid overflow before averaging.
