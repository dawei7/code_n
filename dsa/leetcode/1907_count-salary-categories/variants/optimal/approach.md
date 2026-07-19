## General
**Make the output categories structural.** Use three `SELECT` branches joined with `UNION ALL`, one branch per required label. Each branch always emits one aggregate row, even when `Accounts` is empty or no row satisfies its condition. This guarantees the complete three-row output without depending on which categories occur in the data.

**Count conditionally.** In each branch, place `1` inside a `CASE` only when the income belongs to that branch's interval and leave other rows as `NULL`. `COUNT(expression)` ignores `NULL`, so it returns exactly the number of matching accounts and naturally yields zero when there are none. The interval predicates are disjoint and cover every income.

`UNION ALL` preserves the three independently labeled rows without unnecessary duplicate elimination; their category literals are already distinct.

## Complexity detail
Let $A$ be the number of `Accounts` rows. Each of the three fixed aggregate branches scans the table once, so total time is $O(3A)=O(A)$. Each branch maintains one counter and the output has exactly three rows, giving $O(1)$ auxiliary result state.

## Alternatives and edge cases
- **Group a computed category:** A `CASE` plus `GROUP BY` scans once, but categories absent from the input disappear unless joined to a separate category relation.
- **Use `SUM(condition)`:** This is concise in MySQL, but `SUM` over an empty table is `NULL` unless wrapped with `COALESCE`; conditional `COUNT` returns zero directly.
- **Boundary `20000`:** It belongs to `"Average Salary"`, not `"Low Salary"`.
- **Boundary `50000`:** It also belongs to `"Average Salary"`, while high salary starts strictly above it.
- **Empty table:** Aggregate branches must still emit all three zero rows.
- **Output order:** The contract accepts any row order, so no `ORDER BY` is required.
