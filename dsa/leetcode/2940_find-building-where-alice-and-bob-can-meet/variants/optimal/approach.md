## General

**Reduce each query to one threshold search.** Normalize a query so
`left <= right`. If both starts are equal, that building is already the
leftmost meeting point. If `heights[left] < heights[right]`, Alice can move
directly from `left` to `right`, where Bob may remain, so `right` is the
answer.

The remaining case has `heights[left] >= heights[right]`. Neither person can
meet at an index before `right`, and Alice cannot move to `right`. A later
building is reachable by both exactly when its height is strictly greater than
`heights[left]`, the higher starting threshold. The query therefore asks for
the first index after `right` whose height exceeds that threshold.

**Activate searches only after their right endpoint.** Bucket every unresolved
query at its normalized `right` index. Sweep buildings from left to right,
keeping active queries in a min-heap ordered by required height. At each
building, remove every heap entry whose threshold is strictly below the
current height and assign that building as its answer. Only afterward activate
the queries bucketed at the current index, ensuring their right endpoint
cannot incorrectly answer them.

**The first resolution is leftmost.** A deferred query enters the heap before
the sweep visits any legal candidate. It remains active through every
insufficient building. The first building that pops it is therefore the
smallest index after its right endpoint with height above its threshold, which
is exactly its leftmost common meeting point. Entries left in the heap after
the sweep have no legal answer and retain `-1`.

## Complexity detail

Let $N=\lvert\texttt{heights}\rvert$ and
$Q=\lvert\texttt{queries}\rvert$. Bucketing and sweeping take $O(N+Q)$
outside the heap. Every deferred query is pushed once and popped at most once,
so heap work takes $O(Q\log Q)$ time. Total time is
$O(N+Q\log Q)$, and the buckets, heap, and answer list use $O(N+Q)$ auxiliary
space.

## Alternatives and edge cases

- **Segment tree range maximum search:** Store interval maxima and descend to the first position above a threshold; this answers each query in $O(\log N)$ time after $O(N)$ construction.
- **Monotonic suffix stack plus binary search:** Process queries offline by right endpoint and binary-search the decreasing stack of visible heights; this also gives logarithmic query work but has subtler ordering details.
- **Scan separately for every query:** Searching rightward until a tall-enough building appears is correct but can take $O(NQ)$ time.
- **Same starting building:** Return that index without requiring either person to move.
- **Reversed query endpoints:** Normalize the pair; Alice and Bob's names do not change which buildings are jointly reachable.
- **Equal heights:** Movement requires a strictly taller destination, so an equal-height building cannot satisfy a deferred threshold.
- **No later qualifying building:** Leave the answer as `-1`.

