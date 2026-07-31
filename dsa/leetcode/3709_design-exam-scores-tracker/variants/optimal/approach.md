## General

Strictly increasing record times mean the tracker receives its searchable keys already sorted. Store those times in one array. In a parallel prefix array, keep a leading zero followed by the cumulative score after each record. Appending a record therefore needs no insertion or reordering: append its time and add its score to the previous cumulative total.

For `totalScore(startTime, endTime)`, binary search finds the half-open slice of records whose times lie in the inclusive query interval. The first included position is `bisect_left(times, startTime)`, while `bisect_right(times, endTime)` is one position after the last included record. Using the right-biased search for `endTime` is what makes that endpoint inclusive.

If those positions are `left` and `right`, the desired total is `prefix[right] - prefix[left]`. The prefix at `right` contains every score before the slice plus all included scores; subtracting the prefix at `left` removes exactly the earlier records. When the interval contains no exam, both positions are equal and the difference is naturally zero.

## Complexity detail

Let $q$ be the total number of calls after construction and $r$ the number of recorded exams. Each `record` takes $O(1)$ time, while each `totalScore` performs two binary searches in $O(\log r)$ time. The complete sequence is therefore bounded by $O(q\log r)$ time. The timestamp and prefix arrays use $O(r)$ space.

## Alternatives and edge cases

- **Scan every record per query:** Storing `(time, score)` pairs alone makes `record` easy, but a query can cost $O(r)$ and a query-heavy sequence can take $O(qr)$ time.
- **Ordered map with recomputed sums:** A tree can locate interval endpoints, but summing all nodes inside the interval still repeats work unless cumulative aggregates are maintained.
- **Prefix sums without binary search:** Prefix totals solve the summation step, but exact-time lookup is insufficient because query boundaries need not coincide with recorded times.
- **Inclusive boundaries:** Records exactly at `startTime` or `endTime` must be counted; left-biased and right-biased searches implement those two sides correctly.
- **Empty interval in the record set:** Equal binary-search positions produce a prefix difference of zero without special handling.
- **Large cumulative score:** Up to $10^5$ scores of $10^9$ can total $10^{14}$, so fixed-width implementations need a 64-bit result and prefix type.
- **Chronological guarantee:** Appending is valid only because record times are strictly increasing; the source contract supplies this ordering.
