## General

**First compute the benchmark for every team.** The CTE `T` joins `Project` to `Employees` by `employee_id` so each workload gains its employee's team. It groups by team and computes `AVG(workload)`.

The resulting CTE has one row per represented team:

`(team, avg_workload)`.

Employees without a project row contribute no workload and therefore do not enter the average. This follows the source model, where workload is stored only in `Project`.

**Rejoin each allocation to its benchmark.** The outer query again joins `Project` with `Employees` to obtain employee name and team. `JOIN T USING (team)` attaches that team's average to every allocation row.

The predicate `workload > avg_workload` retains strict exceedances. A workload exactly equal to the team average is excluded, matching “exceeds” rather than “at least.”

**Project schema simplifies row identity.** The local schema declares `employee_id` the primary key of `Project`, so each employee has at most one project allocation row. The outer result therefore cannot duplicate an employee through multiple projects under this contract.

If the intended real-world model allowed an employee on several projects, the key and average semantics would need reconsideration. The exact query follows the stated one-row-per-employee allocation table.

**Select and rename the requested information.** The output keeps `employee_id` and `project_id`. It aliases `name` to `employee_name` and `workload` to `project_workload`. The team average is used only for filtering and is not returned.

**A trace.** Team A has workloads 45 and 68, so its average is 56.5. The first employee is excluded because $45\not>56.5$; the second is retained because $68>56.5$. Team B with workloads 90 and 12 has average 51, retaining only 90.

**Why the CTE aggregation is correct.** For every team, `AVG` equals the sum of joined member workloads divided by their count. Each allocation is compared to exactly that team's value because the outer join key is `team`. No workload from another team can enter its threshold.

**The source differs from the manifest's mechanism.** The local manifest says a partitioned window computes the average. The protected SQL instead uses a grouped CTE and joins that result back. Both can have similar asymptotic behavior, but they are different relational plans and should not be described interchangeably.

**Required ordering.** `ORDER BY 1, 2` sorts first by selected column 1, `employee_id`, then by selected column 2, `project_id`, both ascending by default.

**Why the table is joined twice.** The first join builds team aggregates. The second returns detailed rows for filtering and projection. A window-function version could attach averages in one joined CTE, but the exact source chooses the explicit aggregate-and-rejoin pattern.

## Complexity detail

Let $P$ be project rows and $E$ employee rows. With indexed employee identifiers, both joins are approximately linear in the matched rows. Grouping team workloads is $O(P)$ expected with hash aggregation, while final output ordering can cost $O(Q\log Q)$ for $Q$ qualifying rows. A broad bound is $O(P+E+Q\log Q)$.

The CTE stores one row per team, $O(T)$ space, and the engine may use additional $O(Q)$ sort storage. The manifest's $O(N\log N)$ time and $O(N)$ space are reasonable database-level upper bounds, although the stated window implementation is inaccurate.

## Alternatives and edge cases

- **Window average:** Join allocations to employees once, compute `AVG(workload) OVER (PARTITION BY team)`, then filter in an outer query. This matches the manifest but not the exact source.
- **Correlated subquery:** Recompute a team's average for each employee. It is correct with optimization but can repeat work and be harder to reason about.
- **Workload equals average:** It is excluded because the predicate is strictly greater.
- **One employee in a team:** Their workload equals the team's average, so that team contributes no result.
- **Employees without projects:** They do not participate because both paths begin from `Project`.
- **Project with missing employee:** The inner join removes it; ordinary foreign-key integrity should prevent this.
- **Several teams with equal averages:** Comparisons remain independent because joining uses team identity, not average value.
- **Decimal average:** MySQL preserves fractional averages, so an integer workload is compared with the true non-rounded team mean.
- **Manifest mismatch:** The exact SQL uses grouped aggregation and a rejoin, not a window function.
- **Ordering:** Ordinals 1 and 2 correctly implement employee then project ascending.
- **Why the average is not rounded:** Filtering against the full `AVG` result preserves the true strict comparison. Rounding a team average first could incorrectly include or exclude a workload near the boundary.
- **Team with no allocated employee:** It has no row in CTE `T` and cannot produce an output employee, which is consistent because no project workload exists to evaluate.
- **Name is descriptive only:** Employee identity and joining use `employee_id`. Duplicate employee names across teams or within a team cannot merge rows or alter averages.
- **Strict team isolation:** The CTE key prevents an employee from being compared with a global company average or another team's workload distribution.
