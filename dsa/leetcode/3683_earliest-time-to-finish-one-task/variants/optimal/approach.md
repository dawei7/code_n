## General

**Evaluate every task independently.** A task beginning at `start` and lasting `duration` time units completes at `start + duration`. Because tasks are independent, neither input order nor another task's timing changes this value.

Compute that sum for every row and return the minimum. Every task is examined, so the selected value belongs to an actual task and is no larger than any other completion time. Conversely, no task can finish earlier than this minimum by the definition of minimum, making it exactly the earliest possible finish.

## Complexity detail

For $n$ tasks, one pass takes $O(n)$ time. The running minimum requires $O(1)$ auxiliary space; the generator used by the implementation does not materialize a second list.

The complete legal input contains at most 100 tasks, too few for stable timing to distinguish a scan from plausible slower implementations. The package therefore uses a reviewed `bounded_domain` certificate. Its bounded-work proof limits the accepted implementation to one addition and comparison per task, while property tests cover every legal singleton row, every legal length, and boundary arrangements against a direct minimum oracle.

## Alternatives and edge cases

- **Sort completion times:** It returns the same first value but costs $O(n\log n)$ instead of a single scan.
- **Materialize all sums:** It remains linear but uses unnecessary $O(n)$ auxiliary space.
- **Single task:** Its completion time is the answer directly.
- **Equal completion times:** Ties do not affect the returned time.
- **Later start but earlier finish:** Compare sums, not start times or durations in isolation.
- **Maximum values:** A task may finish at time 200 when both fields equal 100.
