## General
**Attach each payment to a month and department**

Join `Salary` to `Employee` by `employee_id`, and derive `pay_month` from `pay_date`. Each resulting row is now a salary amount with both grouping dimensions needed by the result.

**Compute the company average at the row level**

Use `AVG(amount) OVER (PARTITION BY pay_month)` so every payment row carries the one company-wide average for its month. This aggregate includes all departments and is computed independently for each month.

**Collapse rows to department averages**

Group the enriched rows by `pay_month` and `department_id`. `AVG(amount)` gives the department average. The windowed company average is constant within a month, so `MAX(company_average)` safely carries that value through the grouping.

**Classify the exact averages**

Compare the two averages in a `CASE` expression and emit `higher`, `lower`, or `same`. Every salary payment contributes once to its department and once to its month's company window, so both sides of the comparison use exactly the intended populations.

## Complexity detail
Let `S` be the number of salary rows and `E` the number of employee rows. Joining, partitioning, grouping, and ordering require $O((S + E) \log(S + E))$ time in the general database model and $O(S + E)$ execution space. Hash joins and aggregation can reduce the main passes toward linear time.

## Alternatives and edge cases
- **Two aggregate CTEs:** compute company averages by month and department averages by month and department, then join them; this has the same asymptotic bound and is often the clearest alternative.
- **Correlated company average:** recompute the monthly company average for every department group; it is correct but can rescan salary rows and become quadratic.
- **Average department averages:** incorrect when departments have different numbers of payments; the company average must weight every salary row equally.
- Compare the unrounded averages so formatting does not turn a real difference into `same`.
- A month containing one department reports `same` for that department.
- Departments without a salary payment in a month produce no row for that month.
- Each month is compared only with its own company-wide payments.
