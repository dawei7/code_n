## General

**Evaluate the profit after every possible paid service rotation**

Choosing when to stop means choosing a prefix of paid wheel rotations. The solution simulates those rotations in chronological order and records the earliest prefix with the largest positive cumulative profit.

Its state variables are:

- `i`: the number of rotations already performed and the index of the next arrival entry;
- `wait`: customers who have arrived but have not yet boarded;
- `t`: cumulative profit after `i` paid rotations;
- `mx`: highest positive-or-zero profit seen so far;
- `ans`: earliest rotation count at which a strictly positive record profit was achieved.

`ans` starts at negative one and `mx` starts at zero. Therefore, a non-positive profit never becomes an accepted operating plan.

**Why the loop condition includes arrivals and backlog**

The loop continues while:

`wait or i < len(customers)`.

If arrival entries remain, the operator must simulate the corresponding rotations to evaluate plans that serve those future customers. This includes arrival entries equal to zero: reaching a later arrival time still requires the intervening paid rotation described by the schedule.

After the final arrival, customers may remain in the queue because only four can board per rotation. `wait` keeps the loop running until that backlog is exhausted.

Once both conditions are false, there are no future customers and nobody waiting. Another paid rotation would board zero customers and subtract `runningCost`, so it cannot improve profit. Ending the simulation is safe.

**Arrival happens before boarding**

At the start of an iteration, the source adds:

`customers[i] if i < len(customers) else 0`

to `wait`. This follows the timing rule that `customers[i]` arrive just before the corresponding rotation. After the arrival list is exhausted, the conditional contributes zero while backlog rotations continue.

The next calculation is:

`up = wait if wait < 4 else 4`.

This is `min(wait, 4)` written as a conditional expression. It boards every waiting customer when fewer than four are present, or exactly the gondola capacity when at least four are waiting.

The rule says customers cannot be kept waiting when room exists, so the operator has no choice to board fewer people in hopes of changing later timing. `wait -= up` leaves exactly the unboarded queue.

**Profit for one rotation**

Each boarded customer pays `boardingCost`, while every paid rotation costs `runningCost`. The incremental profit is:

`up * boardingCost - runningCost`.

Adding it to `t` makes `t` the profit of operating through the current rotation. Then `i += 1` converts the zero-based arrival index into the one-based number of rotations completed.

The simulation does not track which gondola customers occupy or when they exit. Boarding revenue is earned immediately, and after the operator stops serving, any rotations required to bring onboard customers down are free. Therefore, departure timing does not affect the choice of profitable paid prefix.

**Recording the earliest maximum**

After each rotation, the code tests `if t > mx`. On a strict improvement, it stores the new profit in `mx` and the current rotation count in `ans`.

The strict greater-than comparison is important. If a later rotation returns to the same maximum profit, the problem asks for the minimum number of rotations achieving that maximum, so the earlier `ans` must remain unchanged.

Because `mx` begins at zero, a profit of exactly zero does not update `ans`. If profit never becomes positive, `ans` remains negative one, matching the requirement.

**A trace of waiting customers**

For `customers = [8,3]`, capacity four:

- Before rotation one, eight arrive. Four board, four wait, and one rotation’s profit is added.
- Before rotation two, three more arrive, making seven waiting. Four board and three remain.
- There is no third arrival, but `wait` is nonzero, so a third iteration boards the remaining three.

The simulation evaluates cumulative profit after all three prefixes and retains the earliest highest one.

**Why checking every simulated prefix is sufficient**

Any legal choice to stop paid service occurs after some number of rotations. Up to that point, arrivals, mandatory boarding, backlog, revenue, and running costs are deterministic; the operator has no alternative per-rotation boarding decision. Thus `t` after rotation `i` is exactly the profit of stopping after that prefix.

The loop visits every potentially useful prefix from the first scheduled rotation through the rotation that clears the final waiting queue. Prefixes after that point only add cost and no revenue. Taking the greatest observed cumulative profit therefore finds the optimal stopping point, and updating only on strict improvement returns its smallest rotation count.

## Complexity detail

Let $N$ be the number of arrival entries and let $A$ be the total number of arriving customers.

The loop performs $N$ scheduled iterations plus enough extra iterations to board the final backlog, at most $\lceil A/4\rceil$ boarding rotations in total order. A precise bound is $O(N+A)$.

Under the constraints, each `customers[i]` is at most 50, so $A\le50N$. Consequently, $O(N+A)$ simplifies to $O(N)$. Every iteration performs constant work.

The method stores a fixed number of integers and does not allocate storage proportional to customers or rotations. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Queue individual customer objects:** Only the waiting count affects boarding and profit. Storing each person wastes $O(A)$ space.
- **Stop simulation at the final arrival index:** This can miss profitable rotations that serve customers still waiting after arrivals end.
- **Simulate gondola positions:** Capacity at the boarding gondola and free safety rotations after stopping make occupant positions irrelevant to profit.
- **Update on `t >= mx`:** This would replace an earlier optimal rotation count with a later tie, violating the minimum-rotations requirement.
- **Initialize the best profit below zero:** That could accept a negative plan even though operating zero rotations yields profit zero and the required answer is `-1` when no positive plan exists.
- **Zero arrivals between future arrivals:** The scheduled rotation still incurs cost if the operator continues toward later customer batches, and the simulation includes it.
- **No positive profit:** `t` never exceeds initial `mx = 0`, so `ans` remains `-1`.
- **Profit becomes positive and later declines:** The record remains at the earlier profitable prefix.
- **Profit later exceeds the record:** `ans` updates to that rotation because the true maximum has improved.
- **Later tie with the maximum:** Strict comparison preserves the earlier rotation count.
- **Fewer than four waiting:** Every waiting customer boards because unused capacity cannot be withheld.
- **More than four waiting:** Exactly four board and the remainder stays for later rotations.
- **Backlog after final arrival:** The `wait` part of the loop condition continues service until it is empty, evaluating all useful prefixes.
- **No backlog and no future arrivals:** The loop stops because further paid rotations have negative incremental profit `-runningCost`.
- **Free rotations after stopping:** They safely unload onboard customers but do not alter the recorded paid-service profit or rotation choice requested by the problem.
