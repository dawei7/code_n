## General

**Compute both maxima in one aggregate row**

Use conditional aggregation over `Salaries`. The expression

`CASE WHEN department = 'Marketing' THEN salary END`

returns a salary for Marketing rows and `NULL` for every other department. `MAX` ignores those nulls, so its result is exactly the highest Marketing salary. The analogous expression for Engineering produces that department's maximum. The contract guarantees at least one row in each target department, so neither aggregate is null.

Subtract the two maxima, apply `ABS`, and alias the value as `salary_difference`. Because the query has aggregate expressions and no `GROUP BY`, it returns exactly one row. Every source row is considered by both conditional aggregates, unrelated departments contribute only nulls, and `ABS` makes the result independent of which target department has the larger maximum.

## Complexity detail

Let $S$ be the number of rows in `Salaries`. A database can evaluate both conditional maxima during one table scan, using $O(S)$ time and constant aggregate state, or $O(1)$ auxiliary space apart from the input and output. An index or engine-specific plan may reduce physical reads, but the stated bound does not depend on one.

The benchmark uses $S$ as `size`, with equal numbers of Engineering and Marketing rows. The accepted conditional aggregate scans those rows once. A correct cross join between the two departmental subsets materializes or evaluates every Engineering-Marketing pair, producing $O(S^2)$ work and failing the scaling verdict.

## Alternatives and edge cases

- **Two scalar subqueries:** Compute each filtered `MAX` independently and subtract them. This is correct and still $O(S)$ asymptotically, but it may scan the table twice instead of sharing one pass.
- **Cross join the two departments:** Joining every Engineering row to every Marketing row and then taking both maxima is correct, but it creates quadratic pair work that is unnecessary.
- **Group by department then pivot:** A common table expression can first compute one maximum per department and conditionally combine the two rows. It is valid but more verbose for exactly two named departments.
- **Marketing maximum is larger:** `ABS` is required; relying on a fixed subtraction order can return a negative value.
- **Equal maxima:** The correct difference is `0`.
- **Other departments:** Their salaries must be ignored by both conditional expressions.
- **Output schema:** The single result column must be named exactly `salary_difference`.
