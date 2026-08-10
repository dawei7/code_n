## General

**Recognize two bundled alternatives**

The competitive file contains a left-self-join query followed immediately by a
correlated-subquery query. There is no semicolon separating them.

As one SQL statement, the second `SELECT` is unexpected syntax after the first
query. Even if a separator were added, a challenge runner generally expects one
statement and one result set. The file must retain exactly one alternative to
be a clean submission.

**First alternative: join employee to manager**

Alias `e` represents the employee. Alias `b` represents the manager. The join
condition:

`e.ManagerId = b.Id`

finds the row whose primary-key ID is stored in the employee's manager field.
The `WHERE` clause then retains cases where `e.Salary > b.Salary`.

The selected projection `e.Name AS Employee` returns the subordinate's name,
not the manager's.

**Why its `LEFT JOIN` behaves like an inner join**

A left join initially preserves an employee with no matching manager and
fills `b.Salary` with null. However, the later condition:

`e.Salary > b.Salary`

is unknown when `b.Salary` is null. `WHERE` retains only true predicates, so
the unmatched employee is discarded.

The final result is therefore the same as an inner join for this predicate.
Using `JOIN` directly would state the intent more clearly and let readers see
that managerless employees cannot qualify.

**Second alternative: correlated manager lookup**

The second query scans outer employee alias `e`, rejects null `ManagerId`
values, and compares the employee salary with a scalar subquery.

Inside that subquery, unqualified `Id` belongs to the inner `Employee` table,
while `e.ManagerId` explicitly refers to the outer row. The condition locates
the manager by primary key and returns that manager's `Salary`.

If the scalar manager salary is lower, the outer employee is returned. If no
manager row exists, the subquery yields null and the greater-than comparison is
unknown, excluding the employee.

**Trace the sample under either alternative**

Joe's manager ID three locates Sam. Joe's 70,000 is greater than Sam's 60,000,
so `Joe` is returned.

Henry's manager ID four locates Max. 80,000 is not greater than 90,000, so
Henry is excluded.

Sam and Max have no manager IDs. The join alternative loses them after the
salary predicate; the subquery alternative rejects them through
`ManagerId IS NOT NULL`.

Both intended queries therefore return the same sample result.

**Why matching by ID is mandatory**

Salary comparison alone could pair an employee with an unrelated lower-paid
employee and create a false positive. The manager relationship is defined by
`managerId`, so every valid comparison must use the row whose `id` equals that
value.

Because `id` is a primary key, the scalar subquery returns at most one row and
the join creates at most one manager match per employee.

Neither approach depends on row order or on manager names being unique. The
identifier relationship alone selects the comparison row.

**Projection and duplicates**

Both alternatives output `Name AS Employee`. They do not use `DISTINCT`.
That is correct at the employee-row level: two different qualifying employees
may share a name, and both records should remain even though the displayed
strings are identical.

Any row order is accepted, so neither intended query requires sorting.

**Material exact-file status**

The two unseparated queries make the source invalid as stored. The first could
be repaired by selecting it alone, preferably changing `LEFT JOIN` to
`JOIN`. The second could be selected alone and is logically correct under the
primary-key manager lookup, though explicit aliasing of every inner column
would improve clarity.

**Null comparisons**

If employee or manager salary is null, strict comparison produces unknown and
does not qualify. This follows standard SQL three-valued logic.

## Complexity detail

The source comment says $O(n^2)$ time and $O(1)$ space. A naive correlated
subquery without an index could indeed scan the table for each employee, but
`id` is a primary key and normally indexed, making manager lookup efficient.

The self-join likewise can scan $n$ employees and probe indexed IDs. A hash
plan may use $O(n)$ memory, while an index nested-loop plan uses different
working space. The manifest's $O(n)$ time and space describe a plausible
optimized plan, not an unconditional property. The combined exact file cannot
execute until one query is chosen.

## Alternatives and edge cases

- **Keep one inner self-join:** The clearest repair and direct expression of the relationship.
- **Keep one correlated query:** Works with primary-key scalar lookup but can be less efficient under poor indexing.
- **Pandas self-merge:** Merge employee rows on `managerId` to manager `id`, then filter the two salary columns.
- **Managerless employee:** Cannot satisfy the comparison.
- **Equal salaries:** Strict inequality excludes the employee.
- **Shared manager:** Multiple subordinates are tested independently.
- **Duplicate names:** Do not deduplicate distinct employee rows.
- **Missing manager row:** Both intended approaches exclude the employee.
- **Two statements:** The exact file must be reduced to a single executable query.
- **Misleading left join:** A right-table predicate in `WHERE` null-rejects unmatched rows.
