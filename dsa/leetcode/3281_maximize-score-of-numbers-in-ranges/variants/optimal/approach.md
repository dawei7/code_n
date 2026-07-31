## General

**Check one proposed minimum distance greedily**

Sort the intervals by their left endpoints. For a proposed score $x$, choose the first interval's left endpoint. In every later interval `[s, s + d]`, place its value at `max(s, previous + x)`, the earliest position that respects both the interval and the required gap from the preceding choice. If this position exceeds `s + d`, the proposal is infeasible.

The greedy placement leaves at least as much room as any other feasible prefix. Inductively, its first choice is the earliest possible. If its previous choice is no later than another construction's, then `max(s, previous + x)` is also no later than that construction's next valid choice. Therefore, if the earliest placement cannot fit an interval, no alternative placement can fit all intervals.

Only adjacent chosen values in sorted order need checking. When every adjacent gap is at least $x$, every nonadjacent difference is a sum of one or more such gaps and is also at least $x$.

**Binary-search the monotone answer**

If distance $x$ is feasible, every smaller distance is feasible; if it fails, every larger distance fails. Binary-search this monotone predicate. Zero is always feasible. No score can exceed

$$
\left\lfloor\frac{\max(\texttt{start})+d-\min(\texttt{start})}{n-1}\right\rfloor,
$$

because $n-1$ adjacent gaps must fit inside the total available span. This supplies a tight safe upper bound.

## Complexity detail

Sorting takes $O(n\log n)$ time. Each feasibility check is $O(n)$, and binary search performs $O(\log R)$ checks, for $O(n\log n+n\log R)$ total time. The sorted list uses $O(n)$ space under the branch's input-preserving accounting; language-specific in-place sorting may use less auxiliary storage.

## Alternatives and edge cases

- **Test every distance:** Reusing the greedy check while increasing the candidate one by one costs $O(nR)$ in the worst case.
- **Choose every interval's left endpoint:** This ignores the shared slack `d`, which may substantially improve the minimum gap.
- **Place values as late as possible:** Late choices consume room needed by later intervals; earliest feasible placement has the useful dominance property.
- With `d = 0`, every choice is fixed and the result is the smallest gap between sorted starts, possibly zero.
- Duplicate starts are valid because their intervals can use different points when `d` provides enough width.
- For two intervals, the maximum score is the distance between the earliest point of the left interval and latest point of the right interval.
- Input order does not constrain chosen-value order; sorting intervals is essential to the greedy proof.
- Coordinates and `d` at $10^9$ can make the total span reach $2\cdot10^9$.
