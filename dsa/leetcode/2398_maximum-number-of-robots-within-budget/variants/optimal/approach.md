## General

**Use positivity to obtain a sliding-window direction.** When a robot is added
to a window, its running-cost sum, its length, and its maximum charge cannot
decrease. Therefore the total cost cannot decrease. If a window ending at the
current right endpoint is over budget, extending it farther left cannot make
it valid; moving the left boundary right is the only useful repair.

**Track the additive term directly.** Maintain the sum of `runningCosts`
inside the current interval. Adding the right endpoint and removing the left
endpoint then each take constant time.

**Maintain the maximum with a decreasing deque.** Store indices whose
`chargeTimes` values decrease from front to back. Before appending a new
index, remove smaller or equal values from the back because the newer value
will remain in the window longer and dominates them. The front is consequently
the maximum charge for the current window. When shrinking past the front
index, remove it so the next candidate becomes visible.

For each right endpoint, repeatedly shrink until the cost is within budget,
then record the resulting length. Because costs are positive, every wider
window ending there is invalid, while the maintained window is the widest
valid one for that endpoint. Considering every right endpoint and taking the
largest maintained length therefore finds the global optimum. Each index
enters the deque once and can leave it only once from either end.

## Complexity detail

Let $n$ be the number of robots. Both window boundaries move only from left to
right, and each index is appended to and removed from the monotonic deque at
most once. The total time is $O(n)$. The deque can hold $O(n)$ indices in the
worst case, while the remaining state is constant, so auxiliary space is
$O(n)$.

## Alternatives and edge cases

- **Enumerate every interval:** Incrementally maintaining each interval's sum
  and maximum still examines $O(n^2)$ intervals and is too slow at the maximum
  input length.
- **Binary search the length:** A prefix sum plus a deque-based or scanned
  feasibility check can exploit monotonic feasibility, but usually costs
  $O(n\log n)$ time.
- **Heap for charge maxima:** A max-heap with lazy deletion supports the same
  window but adds logarithmic operations and stale-entry bookkeeping.
- **No affordable robot:** Shrinking may empty the window; its length is zero
  and the answer correctly remains zero.
- **Maximum leaves from the left:** If the deque front equals the outgoing
  left index, it must be removed before evaluating the shortened window.
- **Equal charge times:** Removing the older equal value from the deque is
  safe because the newer index expires later.
- **Exact budget:** The condition permits total cost equal to `budget`; only a
  strict excess triggers shrinking.
- **Large products:** The product of window length and running-cost sum can
  exceed 32-bit range, so fixed-width implementations require 64-bit
  arithmetic.
