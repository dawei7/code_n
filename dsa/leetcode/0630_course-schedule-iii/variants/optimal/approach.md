## General
**Process deadlines in increasing order**

Sort courses by deadline. Any chosen set can be scheduled in this order without making an earlier deadline harder to satisfy, so feasibility can be checked through one running elapsed time.

**Tentatively accept every course**

Add the current duration to elapsed time and push its negative value into a max-heap. If elapsed time still meets the current deadline, the selected set remains feasible.

**Replace the longest course after a violation**

When the deadline is exceeded, remove the selected course with greatest duration and subtract it from elapsed time. Only one removal is needed because the set was feasible before adding one course. The selected count returns to its previous value, but its total duration becomes as small as possible among ways to keep that many processed courses.

**Why the greedy replacement is safe**

At each deadline, the heap represents a feasible maximum-cardinality subset of processed courses with minimum elapsed time for that cardinality. Adding a feasible course increases the cardinality. If infeasible, no subset containing all selected courses can work; discarding the longest recovers at least as much time as discarding any other one and therefore leaves the best opportunity for every later deadline. Induction preserves the invariant, so the final heap size is optimal.

## Complexity detail
For `C` courses, deadline sorting costs $O(C \log C)$. Every course is pushed once and removed at most once from a heap of size at most `C`, adding $O(C \log C)$ time. The heap and sorted course copy use $O(C)$ space.

## Alternatives and edge cases
- **List instead of max-heap:** apply the same greedy rule but scan for and remove the longest duration after each violation; it is correct but can cost $O(C^2)$ time.
- **Dynamic programming by elapsed time:** maximize course count for each reachable time; large deadlines make the pseudo-polynomial state space impractical.
- **Shortest-duration-first without deadlines:** can miss an urgent course because deadline order is essential.
- A course whose duration exceeds its own deadline can never remain selected.
- Finishing exactly at a deadline is valid.
- Equal deadlines are handled by the same replacement rule regardless of their input order.
- Replacing an earlier long course with a current shorter one may enable more later courses without changing the current count.
