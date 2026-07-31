## General

**Put workload and team on the same row.** Join `Project` to `Employees` by
`employee_id`. Each resulting row now contains the allocation to evaluate and
the team that defines its comparison group.

**Keep the individual row while computing its group average.** Apply
`AVG(workload)` as a window function partitioned by `team`. Unlike a grouped
query, the window calculation annotates every allocation with the relevant
team average without discarding its project ID, employee ID, name, or original
workload. Filter the annotated rows with `workload > team_average`; a workload
equal to the average must not pass.

Finally, rename the requested output columns and order by `employee_id` and
then `project_id`, both ascending. Since each average is computed from exactly
the joined allocations in that row's team, every retained employee and only
such an employee exceeds the correct comparison baseline.

## Complexity detail

Let $n$ be the number of project-allocation rows. The join is expected $O(n)$
with indexed or hash lookup. Partitioning for the window average and ordering
the result require $O(n\log n)$ time in the general case. Window and sorted-row
state use $O(n)$ working space.

## Alternatives and edge cases

- **Global average:** This compares employees from unrelated teams and violates the team-specific baseline.
- **Grouped average joined back:** A team-average CTE followed by a second join is correct, but a window aggregate expresses the same calculation without a separate grouped relation.
- **Grouped query without joining back:** It loses the employee and project rows that must appear in the output.
- The comparison is strict, so workloads exactly equal to their team average are excluded.
- A singleton team never contributes a row because its sole workload equals its own average.
- Decimal team averages must remain fractional; truncating the average can admit an employee incorrectly.
- The final ordering uses both identifiers even though the current schema makes `employee_id` unique in `Project`.
