## General
**Binary-search a monotone assignment count**

Sort both arrays. If $k$ tasks can be assigned, then any smaller number can also be assigned by discarding assignments. To test $k$, only the $k$ easiest tasks and $k$ strongest workers can improve feasibility. Binary-search the greatest feasible $k$ between zero and $r$.

**Match workers while preserving scarce options**

Process the selected workers from weakest to strongest. Before handling a worker, append every still-unconsidered selected task whose requirement is at most `worker + strength` to a deque. These are exactly the remaining tasks this worker could perform with a pill.

If the deque's easiest task requires no pill, assign that front task: spending a pill would be unnecessary, and saving harder tasks cannot hurt stronger later workers. Otherwise a pill is mandatory, so spend one and assign the hardest task at the deque's back. Using the boosted worker on that hardest reachable task preserves easier work for later unboosted assignments. An empty deque or exhausted pill supply makes $k$ infeasible.

The selected tasks and workers are optimal candidates by sorted dominance. At each worker, the no-pill choice consumes the least demanding feasible task, while the pill choice consumes the most demanding task that this weaker worker can rescue. Standard exchange arguments replace any feasible assignment's choice with these choices without reducing what later, stronger workers can do. Thus the predicate accepts exactly feasible counts, and binary search returns the maximum.

## Complexity detail
Sorting costs $O(n\log n+m\log m)$. One feasibility check processes at most $r$ tasks and workers in $O(r)$ time, and binary search performs $O(\log r)$ checks, for $O(n\log n+m\log m+r\log r)$ total time. A check's deque holds at most $r$ requirements, using $O(r)$ auxiliary space.

## Alternatives and edge cases
- **Ordered multiset feasibility:** Remove the weakest unboosted candidate or weakest pill-eligible candidate with balanced-tree operations; this is correct but adds a logarithmic factor per assignment.
- **Linear-list front removal:** The same greedy choices remain correct, but repeatedly shifting the candidate list can make a check quadratic.
- **Try every matching:** Exhaustive assignment and pill choices grow combinatorially and are infeasible at the input limits.
- The $k$ easiest tasks, not an arbitrary $k$, must be tested for a candidate count.
- The $k$ strongest workers dominate every other size-$k$ worker subset.
- A pill with `strength == 0` cannot create any new feasible pairing, though it may remain unused.
- Workers that already meet a requirement should not consume scarce pills.
- Zero-strength workers can complete zero-requirement tasks without pills.
- Extra workers or tasks do not force assignments; the answer is at most $r$.
