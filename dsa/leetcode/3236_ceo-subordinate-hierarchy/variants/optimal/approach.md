## General

**Anchor recursion at the CEO.** A recursive common table expression begins with the row whose `manager_id` is `NULL`. Give this anchor hierarchy level $0$ and copy its salary into a `ceo_salary` column that will travel through the recursion.

**Expand one reporting edge per recursive step.** Join each current hierarchy row to employees whose `manager_id` equals that row's `employee_id`. Increment the hierarchy level and retain the unchanged CEO salary. Because each recursive step follows one direct-report edge, the stored level is exactly the number of edges from the CEO.

After recursion reaches every descendant, exclude level $0$. Rename the required employee columns, compute `salary - ceo_salary`, and order first by level and then by employee ID.

The anchor is the unique CEO. Every subordinate has one manager chain leading to that anchor, so it is reached once at its exact depth. Carrying the CEO salary through every row makes all differences use the same required baseline.

## Complexity detail

Let $e$ be the employee count. With an index on `manager_id` (or the database engine's equivalent recursive-join optimization), following the hierarchy and ordering the result has a conservative $O(e\log e)$ time bound. Without such an access path, rescanning the employee table for every expanded manager can approach $O(e^2)$.

The recursive working table, lookup structures, and final sort may use $O(e)$ auxiliary database storage. The output contains $e-1$ rows when every non-CEO employee belongs to the CEO's hierarchy.

## Alternatives and edge cases

- **Fixed-depth self-joins:** A query with a predetermined number of joins misses hierarchies deeper than that limit.
- **Forced full scan per recursive row:** It is correct but can repeatedly inspect all employees and become quadratic on a long chain.
- **Compare with immediate-manager salary:** The required difference always uses the CEO's salary.
- The CEO is the unique row with a `NULL` manager and must not appear in the result.
- Direct reports have level $1$, not level $0$.
- A subordinate may earn more than the CEO, producing a positive difference.
- Equal salaries produce a zero difference.
- Employee identifiers need not be consecutive and the CEO need not have identifier `1`.
- Input row order does not affect the required level/ID ordering.
- A table containing only the CEO produces an empty result.
