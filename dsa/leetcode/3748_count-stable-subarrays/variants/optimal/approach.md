## General

A subarray has no inversions exactly when its adjacent values are non-decreasing. Indeed, adjacent decreases are themselves inversions; if every adjacent pair is ordered, transitivity rules out every longer-distance inversion. Thus, the stable subarrays are precisely the subarrays contained within maximal non-decreasing runs.

During a left-to-right scan, track the start of the run containing each ending index $i$. Exactly $i-\textit{runStart}+1$ stable subarrays end at $i$. Store prefix sums of these counts. A right-to-left scan also records the end of the run containing every possible query-left index.

For a query `[left,right]`, let `boundary` be the earlier of `right` and the end of the run containing `left`. The query truncates that first run at `left`, so its contribution is the triangular number for `boundary - left + 1` elements. Every position after `boundary` belongs to a later run whose natural start is already inside the query. The difference of the precomputed prefix sums therefore counts all stable subarrays ending at those later positions without adjustment.

These two portions are disjoint and cover every possible ending index in the query, so their sum is the requested count.

## Complexity detail

Let $n=\texttt{nums.length}$ and $q=\texttt{queries.length}$. The two preprocessing scans take $O(n)$ time, and each query uses $O(1)$ arithmetic, for $O(n+q)$ total time. The prefix and run-end arrays use $O(n)$ auxiliary space; the returned answer array is output space.

## Alternatives and edge cases

- **Run starts plus binary search:** Locating the first run boundary after each `left` and using the same prefix sums takes $O(n+q\log n)$ time.
- **Scan every query segment:** Extending a current non-decreasing length while traversing each range is correct but can take $O(nq)$ time when many queries cover most of the array.
- **Enumerate every subarray:** Checking all candidate ranges inside every query repeats even more work and is unnecessary.
- **Equal adjacent values:** Equality does not form an inversion, so equal values remain in the same non-decreasing run.
- **Single-element query:** Its first-run length is one and its answer is `1`, matching the source Note.
- **Query inside one run:** The boundary is `right`, the prefix-sum remainder is empty, and the answer is the triangular number of the query length.
- **Query across several runs:** Only the first run is truncated on the left; all later runs are counted by the global ending-count prefix.
