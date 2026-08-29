## General

**Turn equal email rows into groups**

The query begins by selecting `email` from `Person` and grouping by that same
expression. All rows with identical email text belong to one group.

The primary key `id` distinguishes people but is irrelevant to duplication:
two different IDs with the same email are exactly the condition being sought.
The query therefore neither selects nor groups by `id`.

The guarantee that email contains no uppercase letters means comparisons do not
need application-level case normalization. Actual SQL collation can still be
case-insensitive, but every supplied value is already lowercase.

**Understand positional `GROUP BY 1`**

`GROUP BY 1` is MySQL shorthand for grouping by the first expression in the
`SELECT` list. Here that expression is `email`, so it is equivalent to:

`GROUP BY email`.

The positional form is concise, but it couples grouping to select-list order.
If another expression were inserted before `email`, the meaning could change.
Writing the column name explicitly is usually clearer for maintenance.

Under the exact current query, each output candidate row represents one unique
email group.

**Filter groups with `HAVING`**

`WHERE` filters individual input rows before grouping. The duplicate condition
depends on the number of rows in a completed group, so it belongs in `HAVING`.

`COUNT(1)` counts one non-null constant for every row in a group. Therefore it
equals the number of people sharing that email. The predicate:

`COUNT(1) > 1`

keeps groups containing at least two rows and rejects groups containing exactly
one.

`COUNT(*)` would have the same behavior. `COUNT(email)` is also equivalent
under the explicit non-null email guarantee, but would ignore null values if
they were allowed.

**Trace the sample**

Rows one and three contain `a@b.com`, so their group count is two and passes
the `HAVING` condition.

Row two contains `c@d.com` alone. Its group count is one and is removed.

Grouping already returns one row per email group, so the result contains
`a@b.com` once. No additional `DISTINCT` is needed.

**Why the result is sound and complete**

Every returned group has count greater than one, proving its email occurs in at
least two source rows. Thus no unique address can be returned.

Conversely, every duplicate email has at least two rows. Grouping puts all of
them together, `COUNT(1)` records a value above one, and `HAVING` retains the
group. Therefore no duplicate is missed.

Since each group produces one selected `email`, a value repeated ten times
still appears once in the output.

This also explains why the query does not need to identify which two people
prove the duplication. The task asks for the repeated value, not the matching
row IDs. Once a group size exceeds one, the identities and ordering of its
members cannot change whether that group qualifies.

**Column naming**

The query projects the source column as `email` without an explicit alias. The
Reference describes the requested output column as `Email`. MySQL identifiers
are case-insensitive in ordinary use, and the logical column is the same, but
some result consumers preserve display-case metadata.

For an exact case-sensitive presentation contract, write
`SELECT email AS Email`. The stored query leaves capitalization to the source
identifier and driver.

**NULL behavior is intentionally irrelevant**

The Reference guarantees email is not null. If null were allowed, `GROUP BY`
would place all null emails in one group, and `COUNT(1)` could report that
group as duplicated. Whether multiple missing emails should count as one
duplicate address would require a separate rule.

Because null is excluded, every group key is an actual lowercase email string.

**Result order**

Any order is accepted, so no `ORDER BY` appears. Group output order is not
guaranteed and should not be treated as alphabetical even if one execution
happens to look sorted.

## Complexity detail

Let $n$ be the number of people and $u$ the number of unique emails. A
sort-based grouping plan can take $O(n\log n)$ time and $O(n)$ working space,
matching the manifest.

A hash aggregate can run in expected $O(n)$ time with $O(u)$ memory, while an
index on email may support another plan. SQL query text does not fix the
physical algorithm; the manifest is a conventional safe sort-based bound.

## Alternatives and edge cases

- **Explicit named grouping:** `GROUP BY email` is clearer than positional `GROUP BY 1`.
- **Derived count table:** Group and count in a subquery, then filter `num > 1` outside; correct but more verbose than `HAVING`.
- **Self-join on equal email and different IDs:** Can find duplicates but may create many row pairs and then require `DISTINCT`.
- **Exactly two occurrences:** The group passes and emits one row.
- **Many occurrences:** Still emits one row because grouping collapses them.
- **All emails unique:** No group passes, returning an empty table.
- **Empty table:** Also returns no rows.
- **Non-null guarantee:** Makes `COUNT(1)`, `COUNT(*)`, and `COUNT(email)` equivalent here.
- **Output case:** Add `AS Email` if exact displayed capitalization is enforced.
- **Any order:** No sorting is required.
