## General

The target is the second-highest **distinct** salary within each department, not the second employee after sorting. Assign a salary rank independently inside every department with `DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC)`. The highest distinct salary receives rank one, the next lower distinct salary receives rank two, and equal salaries always receive the same rank.

Keep `emp_id` and `dept` in the ranked common table expression, then filter for `salary_rank = 2`. Because every employee at the selected salary has rank two, the filter preserves all ties automatically. A department with only one distinct salary never produces rank two and therefore needs no separate exclusion rule.

Finally sort by `emp_id ASC` after combining rows from every department. Ordering within the window controls ranking only; it does not guarantee the required order of the result set.

For each department, descending salary order places every distinct salary level at its corresponding dense rank. Thus rank two is exactly the second-highest distinct salary. Partitioning prevents one department's values from affecting another, and selecting every rank-two row returns precisely all qualifying employees.

The remotely Accepted MySQL query also runs unchanged in the app's SQLite fixture engine because both dialects support this standard window-function syntax.

## Complexity detail

Let $n$ be the number of employee rows. The database may sort rows by department and descending salary to evaluate the window, then sort the selected output by employee identifier. These operations give an $O(n\log n)$ worst-case time bound and can require $O(n)$ sorting and window workspace. Appropriate indexes may reduce physical work, but the logical query does not assume them.

## Alternatives and edge cases

- **`ROW_NUMBER`:** It assigns different positions to employees tied at the same salary, so only one tied employee might be selected and duplicate highest salaries can incorrectly occupy the first two rows.
- **`RANK`:** Ties leave gaps; two employees tied for highest both get rank one and the next distinct salary gets rank three rather than rank two.
- **Correlated maximum subqueries:** Finding the maximum salary below each department's maximum can be correct, but repeated per-row scans are more verbose and can grow quadratically without optimizer decorrelation.
- **One distinct salary:** No row receives dense rank two, even when many employees share that salary.
- **Tied second salary:** Every employee at that salary must appear.
- **Tied highest salary:** All highest earners remain rank one, and the next lower salary remains rank two.
- **Several departments:** `PARTITION BY dept` restarts the rank for each group.
- **Final ordering:** The outer `ORDER BY emp_id ASC` is required; window ordering does not order the returned rows.
