## General
**Index every value's occurrences**

During construction, scan `arr` from left to right and append each index to the list associated with its value. Because indices arrive in increasing order, every occurrence list is already sorted without an additional sorting step. Across all values, these lists store exactly $n$ indices.

**Turn an inclusive range into two boundaries**

For a query, select the occurrence list for `value`. Binary-search for the first stored index greater than or equal to `left`; call its insertion position `lower`. Then search for the first stored index strictly greater than `right`; call that position `upper`. Exactly the entries from `lower` through `upper - 1` lie inside the inclusive range, so the answer is `upper - lower`.

**Handle absent values without special traversal**

If a value never occurs, use an empty position list. Both binary searches return zero, producing frequency zero. Repeated queries are read-only and need no state changes.

## Complexity detail
Construction takes $O(n)$ time and stores $O(n)$ indices. A query performs two binary searches on a list of length $f$, taking $O(\log f)$ time and $O(1)$ auxiliary space. Across $Q$ calls, the total is $O(n+Q\log n)$ time. The index uses $O(n)$ space, while an app-level operation sequence also returns $O(Q)$ outputs.

## Alternatives and edge cases
- **Scan each subarray:** Counting directly from `left` through `right` uses no index but can take $O(nQ)$ total time.
- **Prefix counts for every value:** A full value-by-position table answers in constant time but can require $O(nV)$ space for $V$ possible values.
- **Segment tree of frequency maps:** Supports related dynamic or richer range queries, but this immutable point-frequency problem needs only sorted position lists.
- **Inclusive right boundary:** Use an upper-bound search for `right`, not a lower-bound search, so an occurrence exactly at `right` is counted.
- **Absent value:** Both insertion positions are zero and the answer is zero.
- **Single-element range:** It returns either one or zero according to that exact position.
