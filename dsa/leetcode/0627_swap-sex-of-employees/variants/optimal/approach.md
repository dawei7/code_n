## General

**This task changes stored rows rather than returning a derived table.** The required statement must update every employee's `sex` value in place. The exact source uses one `UPDATE Salary` statement and assigns a new expression to the `sex` column. It contains no `SELECT`, temporary table, or separate intermediate update.

The table guarantees that `sex` belongs to the two-value domain `('m', 'f')`. That closed domain makes the swap a simple two-way choice.

**Read the `IF` expression as a complete mapping.** MySQL's `IF(condition, value_if_true, value_if_false)` evaluates

`IF(sex = 'f', 'm', 'f')`

for each row:

- when the original `sex` is `'f'`, the condition is true and the new value becomes `'m'`;
- when the original `sex` is `'m'`, the condition is false and the new value becomes `'f'`.

Because those are the only allowed values, every row enters exactly one correct branch. The expression does not need a second explicit comparison with `'m'`.

**Why both directions can happen in one statement.** A beginner may worry that rows changed from `'f'` to `'m'` could then be changed again by the false branch. That is not how a scalar assignment works. For a given row, the right-hand expression is evaluated once from that row's value as seen by the statement, and its one result is assigned. `IF` selects one branch; it does not execute the true branch and then retest the updated value.

Likewise, the database does not run the assignment once for all female rows and a second time for all male rows. It applies the same mapping independently to every qualifying row within one update operation.

**Why omitting `WHERE` is intentional.** The requirement says to swap all employees. An `UPDATE` without `WHERE` targets every row in `Salary`. Adding a filter such as `WHERE sex = 'f'` would change only one side of the mapping and leave male rows untouched. Two separate filtered updates would also violate the single-statement requirement and risk turning values twice if ordered carelessly.

**Only one column changes.** The `SET` clause assigns only `sex`. The primary key `id`, employee `name`, and `salary` remain exactly as stored. Row count and row identities are unchanged.

For the sample, row A begins with `'m'`, so its condition is false and its value becomes `'f'`. Row B begins with `'f'`, so it takes the true branch and becomes `'m'`. C and D follow the same independent rule. The numeric salaries never participate in the expression.

**Why the update is correct.** Fix any table row. By the ENUM guarantee, its original sex is either `'f'` or `'m'`. In the first case, `sex = 'f'` is true and the statement writes `'m'`, the required opposite. In the second case, the condition is false and the statement writes `'f'`, also the required opposite. Since the statement has no row filter, this reasoning applies to every row. Since no other column is assigned, the final table differs from the original only by the required swap.

The transformation is an involution: applying the exact update a second time returns every valid row to its first value. That is a useful sanity check, although the challenge expects the statement to be run once.

**The domain guarantee is essential to the concise false branch.** For any unexpected non-`'f'` value, the expression chooses `'f'`. If `sex` were `NULL`, `sex = 'f'` would be unknown; MySQL's `IF` treats the condition as not true and also returns `'f'`. This is acceptable only because the Reference defines the column's values as `'m'` or `'f'`. In a nullable or broader production schema, use an explicit `CASE` that preserves or rejects unsupported values.

**Statement-level behavior.** The challenge asks for one update statement so the swap is expressed as one set-based operation. Database transaction logging, locks, and isolation are engine concerns, but the logical operation does not expose an intermediate table in which only half the values have been swapped.

## Complexity detail

Let $R$ be the number of rows in `Salary`. Every row must be examined and its `sex` value rewritten, so time complexity is $O(R)$. No algorithm can asymptotically avoid touching rows whose stored value must change.

The expression uses constant local state per row, so its algorithmic auxiliary space is $O(1)$, matching the manifest. A real database may generate $O(R)$ undo, redo, transaction-log, or multi-version records while updating $R$ rows. That durable engine storage is normally excluded from challenge-level auxiliary-space analysis; it should not be confused with a temporary table created by the solution.

There is no sort, join, grouping, or index lookup requirement in the statement. Updating an indexed `sex` column could create additional index-maintenance work, but the provided schema identifies only `id` as the primary key.

## Alternatives and edge cases

- **`CASE` expression:** `CASE sex WHEN 'm' THEN 'f' ELSE 'm' END` is the editorial form. It is equally set-based and may read more clearly when branches multiply.
- **Explicit two-value `CASE`:** Handle `'f'` and `'m'` separately and use `ELSE sex`. This safely preserves unexpected or null values in a broader schema.
- **Two update statements:** Updating female and male rows separately violates the contract and can undo the first change if the second statement sees newly written values.
- **Temporary mapping table:** Joining a two-row mapping table is unnecessary and explicitly outside the requested form.
- **Empty table:** The statement affects zero rows and still completes correctly.
- **All rows have the same sex:** Every row independently changes to the opposite value.
- **Valid ENUM domain:** The compact false branch is correct because every non-`'f'` value must be `'m'`.
- **Null value:** Outside the intended domain, it would become `'f'` rather than remain null; use explicit handling if nullability is possible.
- **Other columns:** They are untouched because only `sex` appears on the left side of `SET`.
- **Repeated execution:** Two executions restore the original values, confirming the mapping is a true swap.
- **Missing `WHERE`:** Here it is required behavior, not an accidental full-table update, because every employee must be changed.
