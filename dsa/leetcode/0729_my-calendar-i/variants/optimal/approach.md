## General
**Represent the large coordinate domain sparsely**

Use a dynamic segment tree covering integer coordinates from `0` through $10^{9} - 1$. A node records whether its entire segment is booked and allocates children only when a successful partial-range update descends through it. The half-open interval `[start, end)` maps exactly to the inclusive integer range `[start, end - 1]`.

**Detect overlap before changing state**

Query the requested range. A fully covered node proves an overlap immediately; an absent child represents a completely unbooked segment. If any covered point is found, return `False` without allocating or updating nodes. Otherwise assign the whole requested range as covered and return `True`.

**Update only the canonical range pieces**

During a successful assignment, stop when the update range fully contains the current segment and mark that node covered. For a partial intersection, create only the needed children and recurse into the left half, right half, or both. No deletion is required because accepted calendar intervals are permanent.

**Why booking decisions are exact**

The tree initially represents an empty domain. Every accepted booking marks precisely its half-open time points, while every rejected booking leaves the representation unchanged. The overlap query returns true exactly when the new range shares at least one represented point with an accepted range. Touching intervals share no mapped integer coordinate, so one may end exactly where another begins.

## Complexity detail
Let `q` be the number of booking calls and $C = 10^{9}$ the coordinate-domain size. A range query or assignment follows $O(\log C)$ segment-tree levels and visits only the range-boundary paths, so all calls take $O(q \log C)$ time. Successful updates allocate $O(\log C)$ sparse nodes each in the worst case, for $O(q \log C)$ space.

## Alternatives and edge cases
- **Balanced ordered map:** find the predecessor and successor intervals around `start`; checking only those neighbors gives $O(\log q)$ booking time, but Python has no built-in balanced ordered map.
- **Sorted Python list:** binary search finds the insertion position in $O(\log q)$, but inserting near the front shifts $O(q)$ entries.
- **Scan every accepted interval:** reject on the first overlap and append otherwise; it is simple but takes $O(q^2)$ time across many disjoint bookings.
- **Store every time point:** the coordinate range reaches $10^{9}$, so unit expansion is infeasible.
- **Touching endpoints:** `[a,b)` and `[b,c)` do not overlap and must both be accepted.
- **Contained or duplicate interval:** it overlaps stored time and must be rejected.
- **Containing interval:** a new range that surrounds an existing booking must also be rejected.
- **Rejected booking:** it must not reserve any portion of its requested interval.
- **Coordinate boundaries:** both time zero and an end value of $10^{9}$ are valid.
