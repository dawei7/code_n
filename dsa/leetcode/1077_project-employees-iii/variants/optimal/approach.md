## General

**Combine project membership with experience**

`Project` identifies which employees belong to each project. `Employee` supplies `experience_years`. The ranking decision needs both facts, so the CTE joins them:

```sql
FROM
    Project
    JOIN Employee USING (employee_id)
```

`Project.employee_id` is a foreign key and `Employee.employee_id` is a primary key. Every assignment therefore matches exactly one employee record. The join neither drops valid assignments nor duplicates them.

`USING (employee_id)` is an equality join on the same-named column and exposes one merged employee identifier.

**Create a ranked intermediate relation**

The CTE is named `T`:

```sql
WITH
    T AS (
        SELECT
            *,
            ...
        FROM ...
    )
```

The wildcard carries the joined columns, including `project_id`, `employee_id`, and `experience_years`. The query also adds a computed rank `rk`.

Although the final answer needs only two identifiers, experience must remain available long enough to establish which employees are maximal.

**Restart ranking independently for every project**

The window definition contains:

```sql
PARTITION BY project_id
```

Partitioning divides joined rows into independent project groups for the window calculation. Rank values restart at one for every project.

This matters when one employee works on several projects. That employee is evaluated against different colleagues in each partition and may be a winner in one project but not another.

Without `PARTITION BY`, the query would rank employees globally and fail to return the most experienced employee of projects whose members are below the global maximum.

**Put the greatest experience first**

Within each project:

```sql
ORDER BY experience_years DESC
```

sorts larger experience values before smaller ones. The maximum value therefore receives the first rank.

Descending order is essential. Ascending order would rank the least experienced employees first and solve the opposite problem.

Employee name and identifier are not additional ordering keys because ties must be preserved rather than broken.

**Use RANK so every maximum tie receives one**

The complete window expression is:

```sql
RANK() OVER (
    PARTITION BY project_id
    ORDER BY experience_years DESC
) AS rk
```

`RANK` assigns the same rank to rows whose ordering values tie. Thus every employee with the project's maximum `experience_years` receives `rk = 1`.

For experiences five, five, and three, ranks are one, one, and three. The gap after the tie does not matter because the outer query keeps only rank one.

`ROW_NUMBER` would be wrong because it assigns different numbers even to tied rows and would keep only one arbitrary maximum employee. `DENSE_RANK` would also work for a rank-one filter because it preserves ties.

**Filter the ranked rows**

The outer query is:

```sql
SELECT project_id, employee_id
FROM T
WHERE rk = 1
```

Window functions are computed for the CTE before the outer `WHERE` runs. Filtering on `rk` directly in the same select level is generally not allowed because `WHERE` precedes window evaluation. The CTE supplies the necessary second query level.

The projection removes `experience_years`, names, and the helper rank, leaving exactly the required columns.

**Why the result is correct**

Fix one project. The join creates one row for every assigned employee with that employee's experience. Descending project-local ranking gives rank one exactly to rows whose experience equals the project maximum. The outer filter keeps all such rows and rejects every smaller value.

Because partitions are independent, the same reasoning applies to every project. Ties are retained by `RANK`, proving the result contains all and only the most experienced assigned employees for each project.

**Why the composite Project key matters**

`(project_id, employee_id)` is unique, so one employee cannot appear twice in the same project partition. No deduplication is required, and each output pair is unique.

## Complexity detail

Let `R` be the number of project-assignment rows and `E` the number of employee rows.

Physical SQL cost depends on indexes and the optimizer. Accessing or hashing employee records and joining assignments can take expected `O(E + R)` time. Ranking typically requires ordering rows by project and descending experience, which can cost `O(R log R)` without a useful index.

The manifest's `O(E + R log R)` time and `O(E + R)` space describe this join-plus-sort plan. Hash tables, sorting buffers, or materialized CTE rows may occupy linear working space.

An index aligned with the partition and ordering columns can change the physical cost, but not the query semantics.

## Alternatives and edge cases

- **Group maximum plus join:** Compute maximum experience per project and join it back on both `project_id` and `experience_years`. This also preserves every tie.
- **Correlated maximum:** Keep an assignment when its employee experience equals a project-local scalar maximum. It is correct but may be harder for readers and optimizers.
- **DENSE_RANK:** Filtering dense rank one is equivalent because ties receive the same first rank.
- **ROW_NUMBER:** It is incorrect for this contract because it discards tied maximum employees.
- **FIRST_VALUE alone:** It identifies the maximum value but still needs a comparison to retain all rows sharing it.
- **One employee on a project:** That row receives rank one and is returned.
- **Several maximum ties:** Every tied row receives rank one and survives.
- **Employee on several projects:** Partitioning ranks that employee independently in each project.
- **Equal names:** Names are irrelevant and never break experience ties.
- **Composite assignment key:** It prevents duplicate project-employee output pairs.
- **Window filter level:** The CTE is necessary so `rk` exists before the outer `WHERE`.
- **Any output order:** No `ORDER BY` is required in the final result.
