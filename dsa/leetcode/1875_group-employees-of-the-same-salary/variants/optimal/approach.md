## General
**Identify only salaries that can form teams**

Group `Employees` by `salary` and count each group. Retain salaries whose count exceeds one. Joining this compact relation back to `Employees` removes unique-salary employees while preserving every member of each valid team and their original columns.

**Number the filtered salary groups**

Apply `DENSE_RANK()` ordered by salary to the filtered employee rows. Equal salary values receive the same rank, and the next distinct repeated salary receives the next integer. Because filtering happens before the window function, unique salaries do not consume ranks.

**Produce the contractual row order**

Order by the calculated `team_id` and then `employee_id`. This groups each team together in increasing salary order and makes member ordering deterministic.

## Complexity detail
Hash grouping and joining can process the $R$ rows in $O(R)$ expected work. Ranking and producing the required order may sort the eligible rows, yielding $O(R\log R)$ total time in the general plan. Group state, join state, window state, sorting workspace, and returned rows use $O(R)$ space. Existing salary and identifier indexes may reduce physical sorting work.

## Alternatives and edge cases
- **Correlated count per employee:** It is correct but can rescan the table for every row and degrade to $O(R^2)$.
- **Self-join on equal salary:** It can detect teammates, but every employee may match several peers and requires deduplication.
- **`RANK()` instead of `DENSE_RANK()`:** `RANK()` would create gaps based on team size; team IDs must be consecutive across salaries.
- **Unique salary between teams:** It is omitted and consumes no team ID.
- **Team larger than two:** Every member receives the same identifier.
- **Several repeated salaries:** Their numeric salary order, not discovery order, controls team IDs.
- **Output order:** Members are ordered by employee ID within each team.
