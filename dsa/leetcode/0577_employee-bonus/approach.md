## General

Every output row is about an employee, including employees who have no row in `Bonus`. That observation determines which table must drive the query and which join type is required. `Employee` is the complete set of people under consideration, so the query starts there. `Bonus` contains optional information: some employee IDs occur in it and others do not.

An inner join would keep only employees with matching bonus rows and would silently discard the people who received no bonus. The query instead uses:

```sql
Employee
LEFT JOIN Bonus USING (empId)
```

A left join preserves every row from its left-hand table, `Employee`. When a matching `Bonus.empId` exists, the joined row receives that bonus value. When no match exists, SQL fills the columns from the right-hand table with `NULL`. That generated `NULL` is how the joined relation represents “this employee did not get any bonus.”

**What `USING (empId)` means**

Both tables have a column named `empId`. `USING (empId)` is shorthand for joining on equality of those same-named columns, conceptually:

```sql
ON Employee.empId = Bonus.empId
```

The schema says `Employee.empId` is unique, `Bonus.empId` is unique, and the latter references the former. Therefore, each employee can match at most one bonus row, and every bonus row belongs to a real employee. The left join consequently produces exactly one joined row per employee rather than multiplying an employee into several rows.

The requested output does not include `empId`, `salary`, or `supervisor`. After joining and filtering, `SELECT name, bonus` projects only the two requested columns. The problem permits any result order, so no `ORDER BY` is necessary.

**Why ordinary comparison is not enough for missing bonuses**

SQL uses three-valued logic: conditions can be true, false, or unknown. If `bonus` is `NULL`, the expression `bonus < 1000` is not true; it evaluates to unknown. A `WHERE` clause retains only rows for which its condition is true. Therefore, writing only `WHERE bonus < 1000` would incorrectly remove the employees whose left-joined bonus is missing.

The exact solution handles that with:

```sql
WHERE COALESCE(bonus, 0) < 1000
```

`COALESCE` returns its first non-`NULL` argument. For an employee with a bonus row, `bonus` is a number, so `COALESCE(bonus, 0)` returns that number. The condition then keeps it exactly when it is below 1000. For an employee with no bonus row, `bonus` is `NULL`, so `COALESCE` returns zero; zero is below 1000, and the employee is kept.

This single predicate therefore represents the required logical disjunction:

```sql
bonus < 1000 OR bonus IS NULL
```

The explicit disjunction is often the clearest version for discussing SQL null behavior. The `COALESCE` form is compact and is equivalent under the intended bonus domain, where an actual bonus value of zero would also correctly qualify as less than 1000.

**Following the sample row by row**

Dan has a matching bonus row with value 500. The left join attaches 500, `COALESCE` keeps 500, and `500 < 1000` is true, so `(Dan, 500)` is returned.

Thomas has value 2000. `COALESCE` returns 2000, but `2000 < 1000` is false, so his row is removed.

Brad and John have no matching bonus rows. The left join still retains both employee rows and supplies `NULL` as each `bonus`. The predicate temporarily treats each missing value as zero for comparison, so both rows pass. Importantly, `COALESCE` appears only in the `WHERE` condition. The selected column is the original `bonus`, so their output values remain `NULL` rather than being displayed as zero. The query uses zero only to make the filter decision; it does not rewrite the result.

**Why the query is correct**

Take any employee. Because `Employee` is the left side of a left join, that employee appears in the joined relation. Uniqueness of `Bonus.empId` means the employee appears only once. There are two cases.

If a matching bonus exists, `COALESCE(bonus, 0)` equals the actual bonus. The row passes exactly when that value is less than 1000, satisfying the first rule. If no matching bonus exists, the joined `bonus` is `NULL`, `COALESCE` supplies zero for the predicate, and the row passes, satisfying the second rule. A present bonus of 1000 or more fails; a present bonus below 1000 passes.

Thus every qualifying employee is retained and every nonqualifying employee is removed. Selecting `name` and the original `bonus` gives exactly the required schema and preserves `NULL` for employees without bonuses.

## Complexity detail

Let $E$ be the number of `Employee` rows and $B$ the number of `Bonus` rows. The logical query must consider the employee rows and match optional bonus rows. With a hash join, building a lookup for one input and probing it with the other takes expected $O(E+B)$ time and $O(E+B)$ worst-case working space, often reducible to the size of the hashed side. With suitable indexes, an optimizer may instead scan employees and perform indexed bonus lookups.

The variant manifest states the conservative bounds $O((E+B)\log(E+B))$ time and $O(E+B)$ space. The time bound allows a sort-merge join or other plan that sorts relation data before joining. There is no explicit `ORDER BY` in the query, so SQL syntax itself does not require output sorting; an engine using a hash join can do better than the declared conservative bound. The filter and projection are linear in the number of joined rows, which is $E$ here because both join keys are unique.

The output may itself contain up to $E$ rows. Whether result storage is counted separately depends on the complexity convention, but the database also needs buffers or join structures chosen by its physical plan. SQL is declarative, so indexes, statistics, engine configuration, and optimizer decisions influence measured cost.

## Alternatives and edge cases

- **Explicit null predicate:** `WHERE bonus < 1000 OR bonus IS NULL` states the two requirements word for word and does not depend on a replacement value. It is generally the clearest alternative.
- **Inner join:** This is incorrect because it removes employees without a `Bonus` row before the filter gets a chance to include them.
- **Right join from `Bonus`:** Driving from the optional table is easy to get wrong. A left join from `Employee` directly expresses that every employee must remain eligible.
- **`NOT EXISTS` plus a joined query:** Separate branches could find low bonuses and employees without bonus rows, then combine them with `UNION ALL`. That is longer and may scan data multiple times.
- **Correlated scalar subquery:** Looking up a bonus separately for every employee can produce the correct relation, but performance may depend heavily on an index and the null filtering becomes less direct.
- **Bonus exactly 1000:** The condition is strictly “less than,” so 1000 does not qualify.
- **Bonus above 1000:** The employee is excluded because the numeric comparison is false.
- **No bonus row:** The left join produces `NULL`; `COALESCE` makes the predicate true while `SELECT bonus` still returns `NULL`.
- **Actual zero bonus:** Zero is a present numeric bonus and is below 1000, so it correctly qualifies just like any other small bonus.
- **Actual `NULL` stored in `Bonus.bonus`:** If the schema allowed it, the query would treat it the same as no bonus row. The problem’s intended data model uses the joined `NULL` to represent absence; the explicit `IS NULL` alternative has the same behavior.
- **Unique join keys:** The uniqueness guarantees prevent duplicate output rows per employee. Without uniqueness in `Bonus.empId`, one employee could appear once per matching bonus record.
- **Employees table empty:** The left side has no rows, so the result is empty, which is consistent.
- **Bonus table empty:** Every employee is preserved with `NULL` bonus and therefore qualifies.
- **Any output order:** Omitting `ORDER BY` is intentional. Adding one would do unnecessary work unless a consumer imposed an ordering requirement.
- **Preserving display semantics:** Applying `COALESCE` in `SELECT` would display missing bonuses as zero, changing the requested result. Its placement only in `WHERE` is significant.
