## General

**Represent the four worker states explicitly**

A worker is always in one of four relevant groups: waiting on the left, waiting on the right with a box, busy picking on the right, or busy putting down on the left. Waiting workers need a max-priority ordering by crossing-time sum and then index, while busy workers need a min-priority ordering by completion time. Four heaps encode those two different orderings without repeatedly searching all workers.

At each current time, first move every completed pickup or put-down into its corresponding waiting heap. If anyone waits on the right, pop its least efficient worker and perform that worker's right-to-left crossing. Otherwise, if undispatched boxes remain and someone waits on the left, dispatch the least efficient left worker and reserve one box immediately. Reserving at dispatch prevents sending more workers than remaining boxes.

After a crossing, schedule the worker's off-bridge task by its completion timestamp. If nobody can cross, jump directly to the earliest completion that can enable the next useful action instead of advancing one minute at a time. Once every box has been dispatched and no worker is waiting or working on the right, the most recent event was the final box-bearing crossing; left-side put-down work is deliberately ignored.

Every transition follows the stated bridge priority after releasing all tasks completed by that timestamp. The waiting heaps choose exactly the required least-efficient worker, so processing events until the stopping condition reproduces the mandated schedule.

## Complexity detail

Each worker starts in one heap, and every box causes a constant number of worker transitions and bridge crossings. Each heap operation costs $O(\log k)$, giving $O((n+k)\log k)$ time including initialization. Across all four heaps, each worker appears in exactly one state, so the space bound is $O(k)$.

## Alternatives and edge cases

- **Scan worker lists:** Searching all waiting and busy workers for every event is correct but can cost $O((n+k)k)$ time.
- **Minute-by-minute simulation:** Incrementing time through idle intervals can be enormous; jumping to the next completion preserves the event order efficiently.
- **Right-side precedence:** A ready worker carrying a box crosses before any left-side worker, regardless of their relative efficiencies.
- **Efficiency ties:** Larger worker index is considered less efficient and receives priority.
- **Simultaneous completions:** Release every task finishing at the current time before choosing who crosses.
- **Reserved boxes:** Decrement the undispatched count when a worker crosses right, not when pickup finishes.
- **Final put-down:** Return immediately after the last required right-to-left crossing; its subsequent left-side task does not affect the answer.
