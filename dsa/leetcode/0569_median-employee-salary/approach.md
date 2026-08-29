## General

The query ranks employees within each company, counts that company's rows, and keeps the one or two central ranks.

CTE `t` preserves every Employee column and adds:

- `rk` from `ROW_NUMBER()`;
- `n` from a partitioned `COUNT`.

**Create company-local row positions.** The window:

`ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary ASC)`

starts numbering at one separately for each company and orders rows from lower salary to higher salary.

**Attach company size to every row.** `COUNT(id) OVER (PARTITION BY company)` returns the number of employees in that company without collapsing its rows. Every row in one company receives the same `n`.

The outer query filters:

`rk >= n / 2 AND rk <= n / 2 + 1`.

For odd `n = 5`, the numeric bounds are 2.5 and 3.5, so the only integer row number retained is three.

For even `n = 6`, the bounds are three and four, retaining both middle rows.

For `n = 1`, bounds are 0.5 and 1.5 and row one is kept.

The selected `id`, `company`, and `salary` columns reproduce the original employee rows rather than calculating an average salary. This matches the request for median rows.

**Important tie-ordering distinction.** The local contract says equal salaries must be ordered by `id`. The exact source window orders only by `salary ASC` and omits `id ASC`.

Consequently, when equal-salary employees straddle a median boundary, MySQL may assign their row numbers in an unspecified order and return a different tied employee ID than the contract's deterministic rule. Adding `, id ASC` to the window order would fully implement the stated tie-break. This explanation documents the exact implementation rather than silently claiming that omitted behavior.

When tied rows all lie entirely inside or outside the selected median ranks, the omission does not change the result. It matters specifically when identity at the rank boundary is observable.

**Why window functions are appropriate.** Ordinary `GROUP BY company` could compute counts but would collapse employee rows, losing the IDs that must be returned. Window functions attach company-level facts while retaining row identity.

**Why the rank interval yields medians.** In an ascending list, odd size `2q+1` has central rank `q+1`. Even size `2q` has central ranks `q` and `q+1`. The inequalities using `n/2` select exactly those integer ranks.

The final result needs no presentation `ORDER BY` because any output order is accepted.

For company A with six employees, ranks one through six are attached to the salary-sorted rows. Division gives `n / 2 = 3`, so ranks three and four satisfy both inequalities. For company C with five employees, division gives 2.5; only integer rank three lies from 2.5 through 3.5. The same predicate therefore handles parity without a separate odd/even branch.

`ROW_NUMBER` is important rather than `RANK` or `DENSE_RANK`. Median selection concerns physical row positions, and equal salaries still occupy separate positions. Ranking functions that assign the same rank to ties could skip numbers or return more than two rows. `ROW_NUMBER` guarantees exactly one sequential position per employee, provided its ordering is deterministic.

That last qualification exposes the exact source defect. If three employees share the same salary and only one tied position is central, `ORDER BY salary` can choose any of the three IDs for that row number. The contract's `ORDER BY salary, id` would choose the smallest ID first and make the selected central identity reproducible. The salary value may still be correct while the required row ID is wrong.

The CTE is evaluated logically before the outer filter. Filtering employees before calculating `n` or `rk` would change company sizes and positions, so median conditions must be applied only after both windows are defined.

`COUNT(id)` counts every row because `id` is a non-null primary key. `COUNT(*)` would produce the same company sizes here. Partitioning both windows by exactly the same company key ensures each rank is compared with the correct denominator.

## Complexity detail

Let $E$ be the total Employee rows. A typical database plan partitions and sorts rows by company and salary, costing $O(E\log E)$ comparison work in the absence of a supporting index. Window counting and filtering then take linear work.

The ranked intermediate relation contains $E$ rows and may require $O(E)$ memory or temporary storage, matching the manifest. Physical costs depend on indexes, optimizer, and database engine.

Adding `id` as a secondary order key would preserve the same asymptotic bounds.

The intermediate `SELECT *` also carries columns not returned by the outer query. Selecting only the needed columns plus windows could reduce row width without changing the algorithm.

## Alternatives and edge cases

- **Correct deterministic window order:** Use `ORDER BY salary ASC, id ASC` to satisfy the explicit tie-break.
- **Aggregate then join:** Compute company counts and compare each row's relative rank through joins; it is more complex and may be slower.
- **Average the middle salaries:** That returns a numeric median, not the requested employee rows.
- **One employee:** That sole row is the median.
- **Odd company size:** Exactly one rank is selected.
- **Even company size:** Exactly two ranks are selected.
- **Equal salaries:** The exact query lacks the required ID tie-break and can be nondeterministic at boundaries.
- **Multiple companies:** Partitioning resets both row numbers and counts.
- **Output order:** No final sort is required.
- **Primary-key ID:** It provides a unique deterministic secondary key when included.
