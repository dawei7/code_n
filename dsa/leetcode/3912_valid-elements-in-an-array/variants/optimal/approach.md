## General

An element that is strictly greater than every element to its left is a new strict maximum during a left-to-right scan. Keep the largest value seen so far; whenever the current value exceeds it, mark that index valid and update the maximum. Because every input value is positive, starting the maximum at zero also marks the first index.

The second condition is symmetric. Scan from right to left with a fresh maximum and mark every new strict maximum from that direction. This scan marks the last index automatically. A Boolean array combines the two conditions without duplicating a value whose index satisfies both.

Finally, scan `nums` in its original order and emit exactly the marked values. Each marked index has proved one of the two required strict comparisons because its scan maximum represents every element on that side. Conversely, any valid element must exceed the maximum of at least one side and is therefore marked by the corresponding scan.

## Complexity detail

The two directional scans and the final collection each take $O(n)$ time, for $O(n)$ total time. The validity markers require $O(n)$ auxiliary space; the returned array also contains at most $n$ values.

## Alternatives and edge cases

- **Prefix and suffix maximum arrays:** Precomputing both side maxima gives the same $O(n)$ time and space but stores more numeric state than two running maxima plus one marker array.
- **Compare every side directly:** Testing all earlier and later elements for every index is straightforward but takes $O(n^2)$ time.
- **Equal values:** Equality never satisfies a strictly-greater condition, so a repeated maximum is not a new record from that direction.
- **Single element:** The sole index is both endpoints and must appear exactly once.
- **Monotone arrays:** Every value of a strictly increasing array is a left record; every value of a strictly decreasing array is a right record.
