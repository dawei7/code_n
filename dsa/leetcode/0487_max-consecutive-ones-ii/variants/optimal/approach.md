## General

**Turn the optional flip into a window condition**

A contiguous segment can become all ones with at most one flip exactly when it contains no more than one zero. The
task is therefore to find the longest window satisfying that condition.

**Maintain the longest valid window ending at `right`**

`left` starts at zero, and `zero_count` records the zeros in the inclusive window `[left, right]`. For each `value`
at position `right`, increment the count when the value is zero. If the count exceeds one, advance `left`, reducing
the count whenever the departing value is zero, until the window is valid again. Then update `best` with
`right - left + 1`.

After this repair, the window contains at most one zero. Its left boundary is the earliest possible one for the
current `right`: any earlier boundary would retain the older zero as well as the newer one. Consequently it is the
longest valid window ending at that position.

**Why the maximum is found**

Every feasible segment has at most one zero. When its right endpoint is processed, the algorithm's repaired window
starts no later than that segment because it discards only prefixes needed to remove a second zero. The maintained
window is therefore at least as long as every other feasible segment with the same endpoint. Taking the maximum
over all endpoints returns the global optimum. A window with no zero is valid too, so the method correctly leaves
the optional flip unused for an all-one run.

## Complexity detail

Let $n = \lvert \texttt{nums} \rvert$. The right boundary advances $n$ times, and the monotonic left boundary also
advances at most $n$ times. The total time complexity is therefore $O(n)$.

The boundaries, zero count, and maximum use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Last-zero stream state:** for the follow-up, retain the position of the most recent zero. When another zero
  arrives, move the logical left boundary just past the saved position. This preserves $O(1)$ state without storing
  the stream.
- **Two-state dynamic programming:** track the run ending at each position with no flip and with at most one flip;
  it also runs in linear time and constant auxiliary space.
- **Restart from every position:** scanning forward from every possible left boundary is correct but takes $O(n^2)$
  time on an all-one array.
- **All ones:** no flip is needed, and the entire array is one valid window.
- **All zeros:** every valid window has one element because only one zero may be changed.
- **Boundary zeros:** shrinking must move past the older zero, not merely advance by one arbitrary position.
- **Single element:** either possible value yields an answer of one.
