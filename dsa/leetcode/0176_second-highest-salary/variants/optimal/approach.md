## General
The word **distinct** changes the problem. The second employee after sorting is not necessarily the second-highest salary because several employees may share the maximum. Instead, characterize the answer directly: it is the greatest salary strictly below the global maximum.

One compact aggregate formulation is:

```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
```

The scalar subquery finds the highest salary. The strict `<` removes every occurrence of that value, not just one row. The outer `MAX` then selects the largest remaining salary, which is the second distinct level.

The aggregate form also handles the required missing case naturally. Even when the filter leaves no rows, an aggregate query without `GROUP BY` returns one row, and `MAX` over the empty input is `NULL`. A query using only `ORDER BY ... LIMIT 1 OFFSET 1` would instead return no row unless it is wrapped as a scalar subquery.

Let `H` be the maximum salary. Every distinct salary other than `H` is less than `H`, and no occurrence of `H` satisfies the filter. Therefore the filtered relation contains exactly the salary levels eligible to be second highest. If it is nonempty, its maximum is by definition the second-highest distinct salary. If it is empty, fewer than two distinct salaries exist, and SQL's null aggregate result matches the required output.

## Complexity detail
Logically, the query identifies the maximum and then the maximum value below it, requiring $O(n)$ row inspection with constant aggregate state. A database may combine scans or use an index on `salary`; actual physical time and memory depend on its optimizer and indexes.

## Alternatives and edge cases
- `SELECT DISTINCT salary ORDER BY salary DESC` with an offset is valid, but it must preserve a one-row `NULL` result when the offset does not exist.
- `DENSE_RANK()` clearly expresses distinct salary levels and generalizes to arbitrary ranks, but ranks more data than this two-level query needs.
- Selecting the second physical row fails when the maximum is duplicated.
- One employee, an empty table, or any table where all salaries are equal produces `NULL`.
- Duplicates of the lower salary do not matter because `MAX` depends only on its value.
