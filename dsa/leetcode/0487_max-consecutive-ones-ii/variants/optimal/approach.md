## General
**Reframe one flip as one allowed zero**

A segment can become all ones with at most one flip exactly when it contains no more than one zero. The problem is therefore a longest-window problem.

**Expand and repair the window**

Advance the right boundary and count zeros entering the window. When the count reaches two, move the left boundary until the older zero leaves. The restored window is valid and can update the best length.

**Why the left boundary is monotonic**

For each right endpoint, shrinking only until validity returns leaves the smallest possible left endpoint and thus the longest valid window ending there. A discarded prefix contains the extra zero and can never become valid again as the right boundary moves farther right.

**Allow no flip when none is needed**

A window containing zero zeros already satisfies the at-most-one condition, so an all-one array correctly returns its full length.

## Complexity detail
Each boundary advances at most `n` times, giving $O(n)$ total time. The boundaries, zero count, and best length use $O(1)$ extra space.

## Alternatives and edge cases
- **Two-state dynamic programming:** tracks runs ending at each position with zero flips and with at most one flip.
- **Store zero indices:** moving past the older of the last two zeros is another constant-space window form.
- **Restart from every index:** is correct but takes $O(n^2)$ time on all ones.
- **All ones:** no flip is required.
- **All zeros:** only one position can become one.
- **Single element:** both zero and one yield length one.
- **Boundary zeros:** move past the older zero rather than shrinking by only one position.
