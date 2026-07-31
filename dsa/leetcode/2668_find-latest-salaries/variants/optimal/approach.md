## General

Partition the table by `emp_id` and assign `ROW_NUMBER()` within each employee's records. Order each partition by salary descending, but first cast `salary` from text to a numeric type. The rank-one row is then the current record because the statement guarantees salaries rise over time.

Keep all source columns inside the ranked subquery so the outer query can return the name and department belonging to the maximum salary row, rather than independently aggregating values that might come from different records. The primary key `(emp_id, salary)` makes the maximum unique. Finally, filter to rank one and sort by `emp_id` ascending.

## Complexity detail

Let $R$ be the number of salary rows. Partitioned sorting takes $O(R\log R)$ time in the general case and the window result uses $O(R)$ working space. The benchmark uses `size` as $R$ and places all rows in one employee partition, forcing the salary ordering. A self-join that compares every pair of salaries for the same employee is correct but takes $O(R^2)$ work.

## Alternatives and edge cases

- **Grouped maximum then join:** Compute the numeric maximum per employee and join it back to `Salary`; this is correct but requires an extra relation step.
- **Correlated subquery:** Compare each row with that employee's maximum; without favorable optimization this may repeat work for every record.
- **Lexicographic maximum:** Applying `MAX` directly to the varchar column can rank `"900"` above `"1000"`, so numeric conversion is required.
- Employees with one record still receive rank one and must appear.
- The final `ORDER BY emp_id` is required independently of window-partition order.
