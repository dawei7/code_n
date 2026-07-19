## General
**Give the employee table two reporting roles**

Self-join `Employees`: one alias represents a possible manager and the other represents a direct report. Match a report to a manager only when `report.reports_to = manager.employee_id`. An inner join naturally removes employees with no direct reports, which is exactly the stated definition of a manager.

**Aggregate only the matched direct reports**

Group the joined rows by the manager's identifier and name. Each joined row corresponds to one direct report because `employee_id` is unique, so counting report identifiers yields `reports_count`. Averaging the report alias's `age` excludes the manager's own age and all indirect descendants. Apply `ROUND` to that average to obtain the required nearest integer.

**Make the output order explicit**

Order the grouped manager rows by `manager.employee_id`. This is required even if a particular execution plan happens to visit employee records in identifier order.

## Complexity detail
With the unique index on `employee_id`, each of the $E$ report rows can locate its manager in constant expected time, and each manager group maintains a count and an age sum. The complete aggregation therefore takes $O(E)$ time and stores $O(M)$ group states. Database implementations may use an equivalent hash join or ordered-index plan.

## Alternatives and edge cases
- **Correlated subqueries:** Counting and averaging reports separately for every employee can rescan the table and take $O(E^2)$ time without a suitable `reports_to` index.
- **Pre-aggregate then join:** Grouping reports by `reports_to` first and joining those aggregates back to `Employees` is equally valid and can make the two phases explicit.
- **No direct reports:** An employee with no matching report row is not a manager and must be omitted rather than returned with zeroes.
- **Indirect reports:** A report's own reports never contribute to the original manager's count or average.
- **Manager who reports upward:** The same employee may appear as a manager in one relationship and as a report in another; the aliases keep those roles independent.
- **Half-integer average:** Apply rounding after computing the full average; truncating ages or integer-dividing the sum would give the wrong result.
- **Null `reports_to`:** Top-level employees can still be managers, but their null relationship does not create a report for anyone else.
