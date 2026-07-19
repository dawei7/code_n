## General
**Measure each task's reserved-energy gap.** The quantity `minimum - actual` is the energy that must remain available beyond the task's own cost when it begins at its threshold. A large gap is restrictive: postponing that task until energy has already been consumed can force a larger starting reserve.

**Order larger gaps first.** Sort tasks by `minimum - actual` in descending order. For two adjacent tasks $A=(a,m)$ and $B=(b,q)$, order $A,B$ requires at least $\max(m,a+q)$ energy at that boundary, while $B,A$ requires $\max(q,b+m)$. When $m-a \ge q-b$, placing $A$ first never makes the former bound larger than the latter. Repeatedly exchanging inverted adjacent pairs therefore transforms an optimal schedule into the sorted order without increasing its required energy.

**Simulate only the necessary top-ups.** Start with zero tracked energy and zero initial reserve. Before each sorted task, if current energy is below its minimum, increase both the initial reserve and current energy by exactly the deficit. Then subtract the actual cost. Each top-up is unavoidable for that fixed prefix, and adding only the deficit keeps the final initial amount minimal for the greedy order.

**Why the result is globally minimal.** The exchange argument proves that some globally optimal schedule follows the gap order. The simulation computes the least energy capable of executing that exact schedule because every added unit responds to a violated threshold and no unnecessary unit is introduced. Its accumulated reserve is therefore the minimum across all task orders.

## Complexity detail
Sorting $n$ tasks costs $O(n\log n)$ time, and the simulation costs $O(n)$. The sorted task storage and language sorting workspace require $O(n)$ auxiliary space in the worst case.

## Alternatives and edge cases
- **Backward requirement recurrence:** After sorting by the same gap, process the schedule backward with `required = max(minimum, required + actual)` in the corresponding orientation.
- **Quadratic selection:** Repeatedly scan the unscheduled tasks for the largest gap, then simulate it. This preserves correctness but costs $O(n^2)$ time.
- **Sort by minimum alone:** A high threshold paired with a high actual cost is not equivalent to a high reserved-energy gap and can produce a nonoptimal order.
- **Sort by actual cost alone:** Cost does not capture how much energy must be present before the task begins.
- A single task requires exactly its minimum energy.
- When `actual == minimum` for every task, initial energy must cover the sum of all actual costs.
- Equal-gap tasks may appear in any relative order without changing optimality.
- The answer can exceed every individual minimum because earlier tasks consume energy needed by later tasks.
