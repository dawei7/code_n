## General

The competitive source builds consecutive-value intervals as numbers arrive. A hash table named `lengths` records whether a value has been processed and stores full component lengths at component boundaries.

When a new value `i` arrives, it examines the consecutive interval ending at `i - 1` and the interval beginning at `i + 1`. The new value joins those intervals into one larger interval.

**Initialization and duplicate marker**

`lengths = {key: 0 for key in num}` creates one entry for every distinct input value, initially marked zero.

Zero means the value exists but has not yet been processed by the outer loop. Any positive value means it has already been incorporated into some interval.

The check `if lengths[i] == 0` therefore causes only the first occurrence of a duplicate value to perform a merge. Later duplicates contribute nothing, as required.

**What boundary lengths mean**

For a completed consecutive interval from $a$ through $b$, the algorithm guarantees:

- `lengths[a] = b - a + 1`; and
- `lengths[b] = b - a + 1`.

Interior entries need only remain nonzero to mark them processed. Their stored number does not have to equal the full interval length because a future outside value can touch an existing interval only at one of its boundaries.

This boundary-only storage is the key optimization.

**Finding adjacent component sizes**

For new value `i`, `lengths.get(i - 1, 0)` returns the full length of the interval immediately to the left, or zero if no processed consecutive neighbor exists.

Likewise, `lengths.get(i + 1, 0)` returns the right interval length or zero.

If `i - 1` is present inside an interval, it must actually be that interval's right boundary: no value larger than it and smaller than new `i` exists. The same reasoning makes `i + 1` the left boundary of its interval. Their stored lengths are therefore accurate for merging.

**Merging through the new value**

The combined interval length is:

`1 + left + right`.

Its new left endpoint is `i - left`, and its new right endpoint is `i + right`. The tuple assignment stores the combined length at both endpoints and updates `result`.

The source first sets `lengths[i] = 1`, ensuring the new value is marked processed. If `i` itself is also a new boundary, the later tuple assignment overwrites it with the full length. If it becomes interior between two intervals, retaining one is enough as a nonzero duplicate marker.

Python evaluates all right-hand expressions of the tuple assignment before writing targets, so coinciding keys in one-sided or singleton cases do not corrupt calculation.

**Why every component remains represented**

A singleton starts with left and right zero, giving length one at its only endpoint.

Joining one existing interval moves one boundary outward to `i` and updates the unchanged far boundary. Joining two intervals writes their total length at the far left and far right.

No other component is affected. Inductively, every processed consecutive component has its correct length at both boundaries, and every processed value is nonzero.

`result` tracks the largest merged length, so after all distinct values are processed it is the longest consecutive sequence.

**Tracing an interval bridge**

Suppose values one, two and four have already formed intervals `[1, 2]` of length two and `[4, 4]` of length one. Processing three reads `left = 2` from boundary two and `right = 1` from boundary four.

The combined length is four. New endpoints are `3 - 2 = 1` and `3 + 1 = 4`, so both boundary entries become four.

Interior entries two and three do not need correction for future merging; a new zero can only touch endpoint one, and a new five can only touch endpoint four.

**The empty-input defect**

`result` initializes to one. If `num` is empty, the dictionary and loop are empty and the method returns one.

The Reference contract allows an empty array and requires zero. Thus the exact selected source is incorrect for that legal edge case. Initializing `result = 0` would repair it without changing nonempty behavior or complexity.

For every nonempty input, at least one distinct value is processed and longest length is at least one, so the initial one is harmless.

## Complexity detail

Let $n$ be input length. Dictionary construction and the outer loop each take expected $O(n)$ time. Every first occurrence performs a constant number of expected constant-time hash accesses and assignments. Total expected time is $O(n)$.

`lengths` stores one entry per distinct value, using $O(n)$ auxiliary space in the worst case. Other state is scalar.

The result is one integer, and the input list is not sorted or modified.

As with all hash-table solutions, the linear bound relies on expected constant-time dictionary operations.

## Alternatives and edge cases

- **Empty-case repair:** Initialize `result` to zero or explicitly return zero when `num` is empty.
- **Start-only set scan:** Count upward only from values lacking a predecessor. It is simpler and also expected linear-time.
- **Destructive unprocessed set:** Remove rightward runs once and join to stored suffix summaries, as in the Optimal source.
- **Sorting:** Easier to inspect but violates the required linear time and may mutate input.
- **Duplicates:** Positive table entries prevent them from triggering another merge.
- **Singleton:** Left and right lengths are zero, producing one.
- **Bridge two intervals:** Add both boundary lengths plus the new value.
- **Extend only left:** The new value becomes the right endpoint.
- **Extend only right:** The new value becomes the left endpoint.
- **Interior stored length:** It may be stale or one, but future outside merges never query an interval interior as the adjacent boundary.
- **Negative integers:** Neighbor lookup with plus or minus one works identically.
- **Unsorted arrival:** Boundary merging is order-independent.
- **Empty legal input:** Exact source returns one and violates the contract.
- **Hash expectation:** Worst-case collision behavior is outside the ordinary expected $O(n)$ claim.
- **Input preservation:** All updates occur in `lengths`, not `num`.
