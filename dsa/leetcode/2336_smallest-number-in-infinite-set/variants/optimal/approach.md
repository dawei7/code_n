## General

The infinite set does not need to be materialized. Keep `next_fresh`, the
smallest positive integer that has never been removed. Every integer at or
above that frontier is present automatically.

**Store only exceptional restored values**

If a number below `next_fresh` is added back, place it in a min-heap. A
companion set records which values are already in that heap, preventing
duplicate restoration. Adding a number at or above the frontier does nothing
because it is already in the untouched suffix.

For `popSmallest`, a restored heap value is always smaller than
`next_fresh`, so pop the heap minimum when available. Otherwise return
`next_fresh` and increment the frontier.

The representation partitions all present numbers into restored values below
the frontier and the complete suffix beginning at the frontier. Removed
numbers below the frontier occur in neither part. Both updates preserve this
partition, and its smaller component is exactly what `popSmallest` returns.

## Complexity detail

Let $q$ be the number of operations in the trace. At most $q$ restored values
are stored. Heap insertion and removal cost $O(\log q)$; frontier pops and
ignored additions cost $O(1)$. Thus the full trace takes $O(q\log q)$ time and
uses $O(q)$ space.

## Alternatives and edge cases

- **Ordered set of restored values:** A balanced tree provides the same
  asymptotic bounds without a separate deduplication set, but Python's standard
  library has no built-in ordered set.
- **Rescan from one after every pop:** Tracking removed values and restarting
  the search at 1 is correct but can take $O(q^2)$ time.
- **Add an untouched value:** Any `num >= next_fresh` is already present and
  must not enter the heap.
- **Duplicate restoration:** The companion set ensures the same value appears
  at most once.
- **Heap becomes empty:** The frontier immediately supplies the next positive
  integer, preserving the infinite suffix.
