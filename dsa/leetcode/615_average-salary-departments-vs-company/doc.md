# Average Salary: Departments VS Company

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 615 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/average-salary-departments-vs-company/) |

## Problem Description
### Goal
Given employee-department assignments and dated salary payments, compare each department's average salary with the average salary of the entire company for the same month. Treat a month as the `YYYY-MM` portion of `pay_date`, and use only payments made in that month for both averages.

Return `pay_month`, `department_id`, and a column named `comparison` for every department-month represented in the salary data. Set `comparison` to `higher`, `lower`, or `same` according to how the department average relates to the company-wide average for that month; months and departments must not be mixed across comparison groups.

### Function Contract
**Inputs**

- `Salary(id, employee_id, amount, pay_date)`: dated salary payments
- `Employee(employee_id, department_id)`: each employee's department

**Return value**

- `pay_month`: the payment month formatted as `YYYY-MM`
- `department_id`: the department being compared
- `comparison`: `higher`, `lower`, or `same` relative to the company average in that month

### Examples
**Example 1**

- Input: in March, department 1 averages `9000`, department 2 averages `8000`, and the company averages about `8333.33`
- Output: department 1 is `higher`; department 2 is `lower`

**Example 2**

- Input: in February, both departments and the company average `7000`
- Output: both departments are `same`

### Required Complexity

- **Time:** $O((S + E) \log(S + E))$
- **Space:** $O(S + E)$

<details>
<summary>Approach</summary>

#### General

**Attach each payment to a month and department**

Join `Salary` to `Employee` by `employee_id`, and derive `pay_month` from `pay_date`. Each resulting row is now a salary amount with both grouping dimensions needed by the result.

**Compute the company average at the row level**

Use `AVG(amount) OVER (PARTITION BY pay_month)` so every payment row carries the one company-wide average for its month. This aggregate includes all departments and is computed independently for each month.

**Collapse rows to department averages**

Group the enriched rows by `pay_month` and `department_id`. `AVG(amount)` gives the department average. The windowed company average is constant within a month, so `MAX(company_average)` safely carries that value through the grouping.

**Classify the exact averages**

Compare the two averages in a `CASE` expression and emit `higher`, `lower`, or `same`. Every salary payment contributes once to its department and once to its month's company window, so both sides of the comparison use exactly the intended populations.

#### Complexity detail

Let `S` be the number of salary rows and `E` the number of employee rows. Joining, partitioning, grouping, and ordering require $O((S + E) \log(S + E))$ time in the general database model and $O(S + E)$ execution space. Hash joins and aggregation can reduce the main passes toward linear time.

#### Alternatives and edge cases

- **Two aggregate CTEs:** compute company averages by month and department averages by month and department, then join them; this has the same asymptotic bound and is often the clearest alternative.
- **Correlated company average:** recompute the monthly company average for every department group; it is correct but can rescan salary rows and become quadratic.
- **Average department averages:** incorrect when departments have different numbers of payments; the company average must weight every salary row equally.
- Compare the unrounded averages so formatting does not turn a real difference into `same`.
- A month containing one department reports `same` for that department.
- Departments without a salary payment in a month produce no row for that month.
- Each month is compared only with its own company-wide payments.

</details>
