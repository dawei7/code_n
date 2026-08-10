## General

**Rank salary values separately inside each department.** “Second-highest salary” means the second distinct salary, not the employee who happens to appear second after sorting rows. If several employees share the highest salary, all of them occupy the first salary level; the next lower distinct value is still second.

`DENSE_RANK()` implements exactly this definition. The window clause partitions rows by `dept`, so salaries from Sales never affect ranks in IT or another department. `ORDER BY salary DESC` puts the largest salary at rank one and the next distinct salary at rank two.

Unlike ordinary `RANK`, `DENSE_RANK` does not leave gaps after ties. If two employees both earn 80,000 below a 90,000 top salary, both receive dense rank two. If the highest salary itself is tied, all top earners receive one and the next distinct salary still receives two.

**Use a CTE so the computed rank can be filtered.** Window functions are evaluated after a query's ordinary `WHERE` phase, so their result generally cannot be referenced directly in the same select's `WHERE` clause. CTE `T` first produces `emp_id`, `dept`, and alias `rk` for every employee. The outer query then safely filters `WHERE rk = 2`.

Every employee at the department's second distinct salary passes. Departments with only one distinct salary have no rank-two row and disappear naturally; no special department-count test is required.

**Why the salary itself need not be returned.** Salary is required to compute rank but the requested result contains employee ID and department. CTE `T` may omit salary from its projection after the window expression has used it. The outer select returns exactly `emp_id, dept`.

**Final ordering is global by employee ID.** `ORDER BY 1` refers to the first selected output column, `emp_id`. Ascending is the default direction. Departments may therefore be interleaved in the result if employee IDs require it, which matches the stated order rather than grouping by department.
Partitioning creates one independent salary ordering for every department. Dense rank equals one plus the number of distinct higher salary values. Consequently `rk = 2` holds exactly when one distinct salary is higher—precisely the second-highest value. Every employee sharing that salary receives the same rank and is retained. No row from a department lacking a second distinct value can pass.

**Employee count and distinct salary count are different.** The example's HR department has one employee, but the more general exclusion reason is that it has fewer than two distinct salary levels. A department with ten employees all earning the same amount would also have no result. Conversely, a department with exactly two employees at different salaries returns the lower-paid one.

**Potential null semantics.** The schema does not explicitly state that salary and department are non-null. Under SQL window ordering, `NULL` salary placement depends on dialect ordering rules and could become a salary level. Challenge data normally treats these fields as populated. A production query may need `WHERE salary IS NOT NULL` or a defined null policy.

The leading `#` comment, CTE, and window syntax target MySQL 8 or newer. Older MySQL versions without window functions cannot execute this solution.

## Complexity detail

Let $N$ be the number of employees. A general database plan must partition and order rows by department and descending salary, usually costing $O(N\log N)$ time. Filtering and final employee-ID ordering can add another $O(N\log N)$ sort, but the same asymptotic bound remains.

Window sorting, CTE materialization, and result sorting can use $O(N)$ working space. Indexes on department, salary, or employee ID may reduce physical sorting. SQL complexity is optimizer- and storage-plan-dependent; the manifest bounds are reasonable general estimates.

## Alternatives and edge cases

- **Correlated subquery:** Count distinct salaries greater than each employee's and keep rows where that count is one. It is logically direct but can repeat work without optimizer support.
- **Group distinct salaries first:** A department-salary table can be ranked and then joined back to employees. This makes distinctness explicit but adds a join.
- **`RANK` instead of `DENSE_RANK`:** It is wrong when the highest salary is tied because the next salary rank would skip past two.
- **`ROW_NUMBER`:** It keeps only one physical employee at a salary and would incorrectly omit tied second earners.
- **Tied second salary:** Every tied employee receives dense rank two and is returned.
- **Tied highest salary:** The next lower distinct salary remains dense rank two.
- **One distinct salary:** No row has rank two, even if the department has many employees.
- **Exactly two distinct salaries:** All employees on the lower level are returned.
- **Departments are independent:** `PARTITION BY dept` restarts ranking for each one.
- **Final order:** Employee ID, not department, controls presentation.
- **Positional `ORDER BY`:** It is concise but fragile if projection order changes; `ORDER BY emp_id ASC` is clearer.
- **Duplicate employee ID:** The schema prohibits it, ensuring each returned employee appears once.
- **MySQL version:** Window functions require a modern engine.
