## General
**Represent the previous direction in the state.** Position alone does not determine the legal next moves: arriving after a backward jump forbids another backward jump, while arriving at the same position after a forward jump permits one. Use states `(position, last_was_backward)` so each state has an unambiguous transition set.

**Search states in jump-count order.** Breadth-first search begins with `(0, false)`. Every state can move forward by `a`; it can move backward by `b` only when its flag is false and the destination is nonnegative. Reject blocked destinations and states already visited. Because every edge represents one jump, the first dequeued state at position `x` has the minimum possible jump count.

**Bound the otherwise infinite axis.** No target or forbidden position exceeds $M$. Searching through $L=M+a+b$ allows every useful overshoot needed to combine one forward and one backward jump near that boundary. Traveling farther into the obstacle-free region cannot create a new alignment that requires more than this extra forward/backward margin; the redundant excursion can be removed from a shortest route. Thus states above $L$ need not enter the queue.

The visited key must include the direction flag. Marking only a position could discard a later arrival that enables a backward move and is therefore behaviorally different.

## Complexity detail
There are at most two direction states for each integer position from 0 through $L$. Each state is enqueued once and has at most two transitions, so breadth-first search takes $O(L)$ time after building the $O(f)$ blocked set. Total time is $O(f+L)$ and the blocked set, visited set, and queue use $O(f+L)$ space.

## Alternatives and edge cases
- **Depth-first search with memoization:** It can determine reachability within the same bounded state graph, but extra bookkeeping is needed to recover a minimum edge count; breadth-first search gives it directly.
- **Visited positions without direction:** This incorrectly merges states whose next backward move has different legality.
- **Linear-list membership:** Keeping blocked or visited states in lists preserves correctness but can make membership checks quadratic in the explored range.
- **Unbounded search:** Continuing forward forever when the target is unreachable prevents termination; a justified upper bound is required.
- If `x == 0`, the answer is zero before any jump.
- The bug may jump past `x` and later return by one legal backward jump.
- A forbidden first forward landing can make every route impossible.
- Consecutive backward destinations must never be generated, even when both positions are otherwise legal.
- Different direction states at the same coordinate must both remain discoverable.
- A common divisor of `a` and `b` that does not divide `x` can make the target unreachable even without useful obstacles.
