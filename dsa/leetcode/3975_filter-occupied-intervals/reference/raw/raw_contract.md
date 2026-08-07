## Function Contract

`solve(occupiedIntervals, freeStart, freeEnd) -> list[list[int]]`

**Inputs**

- `occupiedIntervals`: A nonempty array of inclusive integer intervals `[start, end]`; intervals may overlap, touch, and arrive unsorted.
- `freeStart`: The inclusive first integer point of the free interval.
- `freeEnd`: The inclusive final integer point of the free interval.

**Output**

Return all integer points covered by at least one occupied interval but not by `[freeStart, freeEnd]`, encoded as sorted inclusive intervals. Consecutive remaining integer points belong to the same output interval, so the result is non-overlapping and uses the minimum possible number of intervals.
