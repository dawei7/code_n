## General

Every successful earlier test decreases the current device once, unless that
would take its battery below zero. If `tested` devices have succeeded before
the current position, its effective battery is
`max(0, battery - tested)`. It is positive exactly when the original `battery`
is strictly greater than `tested`.

Scan the original array without modifying it. Whenever `battery > tested`, the
device is tested and `tested` increases by one; otherwise it is skipped. By
induction, before each position `tested` equals both the number of successful
earlier tests and the total decrement applied to every still-positive later
battery. The comparison therefore makes exactly the same choice as the stated
operations, and the final counter is the required number of tested devices.

## Complexity detail

Let $N=\lvert\texttt{batteryPercentages}\rvert$. The scan takes $O(N)$ time
and stores only one counter, using $O(1)$ space.

## Alternatives and edge cases

- **Explicit suffix updates:** Decreasing every later array element after each successful test directly follows the statement but takes $O(N^2)$ time.
- **Difference-array simulation:** Deferred range decrements can also produce a linear solution, but a single accumulated test count is simpler because every update has the same suffix and decrement.
- **Battery equal to the offset:** The effective charge is zero, so the device is not tested; the comparison must be strict.
- **Leading zeros:** Skipped devices do not increase the offset applied to later devices.
- **All zeros:** No device is tested and the answer is zero.
- **Single device:** It is tested exactly when its battery is positive.
