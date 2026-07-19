## General
**Carry the chef's next available time**

Maintain `finish`, the completion time of every order processed so far. For a customer arriving at `arrival`, preparation cannot begin before either the arrival or the previous completion. The start time is therefore `max(finish, arrival)`, and adding the current preparation duration gives the new `finish`.

This single value contains all relevant effects of earlier customers. Their individual arrival times no longer matter once their combined workload has determined when the chef becomes available. When there is a gap between customers, the maximum discards the stale earlier finish and correctly restarts the schedule at the new arrival.

**Accumulate complete arrival-to-finish intervals**

After computing a customer's completion time, add `finish - arrival` to a running total. This includes both any delay behind earlier orders and the customer's own preparation duration, exactly matching the definition of waiting time in the contract.

The input order is the mandated service order, so applying this recurrence from left to right uniquely reconstructs the chef's schedule. Each contribution is consequently the true waiting time for its customer. Divide the total by $n$ only after the scan so intermediate calculations remain exact integers.

## Complexity detail
The algorithm performs constant work for each of the $n$ customers, taking $O(n)$ time. It stores only the current finish time and accumulated wait, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Recompute every prefix schedule:** rebuilding the chef's timeline from the first customer for every requested wait is correct but repeats work and takes $O(n^2)$ time.
- **Explicit waiting queue:** a queue can simulate pending customers, but the fixed service order means the single finish timestamp already represents all outstanding work.
- **Average incrementally:** repeatedly updating a floating-point mean is possible, but summing exact integer waits first is simpler and avoids accumulated rounding error.
- **Idle gap:** when `arrival > finish`, the chef starts at `arrival`; carrying the earlier finish directly would invent waiting time.
- **Simultaneous arrivals:** equal arrival times remain in their input order and accumulate behind one another.
- **Waiting-time meaning:** include the customer's own preparation duration, not only time spent before cooking starts.
- **Single customer:** the average equals that order's preparation time.
- **Large backlog:** integer totals may exceed individual input bounds, so fixed-width implementations need a sufficiently wide accumulator.
