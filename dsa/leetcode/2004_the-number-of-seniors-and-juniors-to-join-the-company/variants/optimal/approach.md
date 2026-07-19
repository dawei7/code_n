## General
**Translate maximum count into cheapest prefixes.** Within one experience group, hiring the cheapest salaries first maximizes how many candidates fit any fixed budget. Order each group by `salary`, using `employee_id` only as a deterministic tie-breaker, and compute a cumulative salary with a partitioned window function.

**Reserve the senior budget first.** Among senior rows, every cumulative total at most $70{,}000$ represents an affordable prefix. Count those rows and take the largest qualifying cumulative total as senior spending. Aggregating this filtered set still returns one row when no senior qualifies; `COALESCE` converts its missing spending total to zero.

**Apply only the remainder to juniors.** Cross join the one-row senior summary to the ranked candidates. Count junior rows whose own cumulative salary is at most `70000 - senior_spending`. Emit the senior count and junior count with `UNION ALL`, guaranteeing both required experience rows even when either count is zero.

The senior result is maximal because no set of the same size can cost less than the cheapest prefix. Once that prefix is fixed, the identical argument makes the affordable junior prefix maximal under the remaining budget.

## Complexity detail
Partition ordering for the window calculation takes $O(N\log N)$ time in the general database execution model. The filtered aggregates and final union scan the ranked rows linearly. Materializing window state and sorted partitions may use $O(N)$ space.

## Alternatives and edge cases
- **Correlated cumulative subquery:** Recomputing the cheaper-prefix sum for every candidate is correct but can require $O(N^2)$ row comparisons.
- **Maximize total hires across both groups:** This violates the required senior-first priority; juniors may be considered only after the senior count is maximal.
- A salary equal to the remaining budget is affordable because spending must not exceed $70{,}000$.
- When no senior fits, all $70{,}000$ remains available to juniors.
- When seniors consume the full budget, the junior result must still appear with count zero.
- Equal salaries do not change the maximum count; the unique employee identifier supplies stable window ordering.
