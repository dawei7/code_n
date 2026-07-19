## General
A position alone is not a complete search state: reaching the same cell with more eliminations remaining may enable a path that a depleted arrival cannot follow. Breadth-first search therefore carries `(row, column, remaining)`, and entering an obstacle decreases `remaining` by one.

**Dominance at one cell.** For each cell, remember the greatest remaining budget seen there. If a new arrival has no more budget than that record, it is dominated: it occurs no earlier than the recorded BFS arrival and has no additional future choices. Discard it. An arrival with more remaining budget can be useful, so update the record and enqueue it.

Breadth-first layers contain walks in increasing step count. Consequently, the first generated target state has minimum length. Dominance pruning never removes a uniquely useful continuation, because the earlier state at that cell has at least the same budget. If `k` is at least the number of intermediate cells on a Manhattan route, obstacles cannot prevent the direct length $m+n-2$; this safe shortcut also handles large budgets.

## Complexity detail
There are at most $S=mn(k+1)$ distinct position-and-remaining-budget states, and each has four constant-time transitions, giving $O(S)$ worst-case time. The queue may contain $O(S)$ states; the dominance table itself uses only $O(mn)$ entries, so the overall auxiliary-space bound is $O(S)$.

## Alternatives and edge cases
- **Visited positions only:** Marking a cell visited without its budget can discard a later arrival that retains more eliminations and is necessary for a solution.
- **List-based Dijkstra:** Unit edge costs make BFS sufficient; repeatedly scanning an unsorted state list for the minimum distance adds quadratic selection work.
- **Single-cell grid:** Start already equals target, so the answer is zero.
- **Large elimination budget:** When a Manhattan route's intermediate cells can all be removed, return $m+n-2$ immediately.
- **Unreachable target:** Exhausting every nondominated state without reaching the target requires returning `-1`.
