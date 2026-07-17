# The Number of Employees Which Report to Each Employee

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1731 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/) |

## Problem Description

### Goal

The `Employees` table contains one row per employee. Besides the employee's identifier, name, and age, a row may store the identifier of the manager to whom that employee reports. A null `reports_to` value means that the employee does not report to anyone.

For this task, an employee is a manager only when at least one other employee reports directly to them. Return every such manager's identifier and name, the number of direct reports, and the direct reports' average age rounded to the nearest integer. Indirect descendants in the reporting hierarchy do not contribute. Order the result by `employee_id`.

### Function Contract

**Inputs**

- `Employees(employee_id, name, reports_to, age)`: `employee_id` is unique; `reports_to` is either another employee identifier or null.

Let $E$ be the number of employee rows and $M$ the number of employees having at least one direct report.

**Return value**

- Return a table with columns `employee_id`, `name`, `reports_count`, and `average_age`.
- Include one row per manager, with `average_age` rounded to the nearest integer, ordered by `employee_id` in ascending order.

### Examples

**Example 1**

- Input: Hercy (`9`, age `43`) has direct reports Alice (age `41`) and Bob (age `36`); Winston reports to nobody.
- Output: `(9, "Hercy", 2, 39)`
- Explanation: Hercy's direct reports average $(41 + 36) / 2 = 38.5$, which rounds to $39$.

**Example 2**

- Input: Michael manages Alice and Bob; Alice manages Charlie and David; Bob manages Eve.
- Output: Michael with `(2, 40)`, Alice with `(2, 37)`, and Bob with `(1, 37)`, in employee-ID order.
- Explanation: Each manager's count and average use only that manager's immediate reports.

**Example 3**

- Input: employee `20` reports to employee `10`, and employee `30` reports to employee `20`.
- Output: one row for employee `10` based only on employee `20`, and one row for employee `20` based only on employee `30`.
- Explanation: The grandchild employee `30` is not included in employee `10`'s aggregate.

### Required Complexity

- **Time:** $O(E)$
- **Space:** $O(M)$

<details>
<summary>Approach</summary>

#### General

**Give the employee table two reporting roles**

Self-join `Employees`: one alias represents a possible manager and the other represents a direct report. Match a report to a manager only when `report.reports_to = manager.employee_id`. An inner join naturally removes employees with no direct reports, which is exactly the stated definition of a manager.

**Aggregate only the matched direct reports**

Group the joined rows by the manager's identifier and name. Each joined row corresponds to one direct report because `employee_id` is unique, so counting report identifiers yields `reports_count`. Averaging the report alias's `age` excludes the manager's own age and all indirect descendants. Apply `ROUND` to that average to obtain the required nearest integer.

**Make the output order explicit**

Order the grouped manager rows by `manager.employee_id`. This is required even if a particular execution plan happens to visit employee records in identifier order.

#### Complexity detail

With the unique index on `employee_id`, each of the $E$ report rows can locate its manager in constant expected time, and each manager group maintains a count and an age sum. The complete aggregation therefore takes $O(E)$ time and stores $O(M)$ group states. Database implementations may use an equivalent hash join or ordered-index plan.

#### Alternatives and edge cases

- **Correlated subqueries:** Counting and averaging reports separately for every employee can rescan the table and take $O(E^2)$ time without a suitable `reports_to` index.
- **Pre-aggregate then join:** Grouping reports by `reports_to` first and joining those aggregates back to `Employees` is equally valid and can make the two phases explicit.
- **No direct reports:** An employee with no matching report row is not a manager and must be omitted rather than returned with zeroes.
- **Indirect reports:** A report's own reports never contribute to the original manager's count or average.
- **Manager who reports upward:** The same employee may appear as a manager in one relationship and as a report in another; the aliases keep those roles independent.
- **Half-integer average:** Apply rounding after computing the full average; truncating ages or integer-dividing the sum would give the wrong result.
- **Null `reports_to`:** Top-level employees can still be managers, but their null relationship does not create a report for anyone else.

</details>
