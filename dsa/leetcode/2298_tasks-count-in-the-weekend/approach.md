## General

**Convert each date to MySQL's weekday number**

MySQL's `WEEKDAY(date)` returns zero for Monday, one for Tuesday, through five for Saturday and six for Sunday.

The weekend is therefore represented exactly by the set `(5,6)`. No textual day names, locale settings, or manual date arithmetic are needed.

**Turn each classification into a zero-or-one value**

For one task row,

`WEEKDAY(submit_date) IN (5, 6)`

evaluates to one when the date is Saturday or Sunday and zero otherwise in MySQL's numeric Boolean context.

The complementary expression with `NOT IN` produces one for Monday through Friday and zero for weekend dates.

Because the two conditions are complements for every non-null valid date, each task contributes exactly one to one output count and zero to the other.

**Aggregate the weekend count**

`SUM(WEEKDAY(submit_date) IN (5, 6)) AS weekend_cnt` adds the weekend indicator across all rows.

Each Saturday or Sunday task contributes one regardless of its assignee or task ID. The result is the number of task rows submitted during the weekend, not the number of distinct dates or assignees.

**Aggregate the working-day count**

The second `SUM` adds the complementary weekday indicator and names it `working_cnt`.

Monday through Friday all count equally. A date shared by several tasks contributes once for every task row, as required.

**Why one query row is returned**

The query contains aggregate functions and no `GROUP BY`. SQL therefore treats the whole `Tasks` table as one group and returns one result row with both totals.

The “any order” requirement is automatically satisfied because there is only one row. Column aliases give the exact requested output names.

**Trace the sample**

June 13, 14, and 15 of 2022 are Monday, Tuesday, and Wednesday, so their weekend indicators are zero and working indicators are one.

June 18 is Saturday and both June 19 rows are Sunday. Those three rows contribute one each to `weekend_cnt`. Both totals become three.

**Why task and assignee IDs are unused**

The classification depends only on `submit_date`. `task_id` establishes row identity, and `assignee_id` provides context, but neither affects whether that row belongs to the weekend or working-day category.

Counting the Boolean expressions directly avoids unnecessary grouping by either identifier.

**Why the two sums are correct**

For every non-null date, `WEEKDAY` returns exactly one integer from zero through six. It belongs either to `(5,6)` or to its complement, never both.

Summing the first indicator counts precisely all weekend task rows, while summing the second counts precisely all remaining task rows. The returned aliases therefore match the requested values.

**Understand empty and null behavior of the exact SQL**

The schema presents ordinary dates and does not describe nulls. Under that contract, every row is classified.

If the table were empty, MySQL `SUM` over no rows would return `NULL` rather than zero. If explicit zeroes were required for an empty-table extension, `COALESCE(SUM(...),0)` would be needed. That behavior is not added by the exact source.

## Complexity detail

Let `r` be the number of task rows. The database scans each row, evaluates `WEEKDAY` and two membership predicates, and updates constant-size aggregate state. Conceptual time is `O(r)`.

The two running sums require `O(1)` aggregation space. No grouping table, sort, or result-sized intermediate structure is necessary. Actual database execution details can depend on the engine, but a full scan is sufficient.

## Alternatives and edge cases

- **CASE expressions:** `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` is more portable and has the same meaning as MySQL Boolean summation.
- **DAYOFWEEK:** It uses a different numbering convention, so weekend constants must be adjusted carefully.
- **Count total minus weekend:** Working count can be `COUNT(*)-weekend_cnt`, but the exact query states both classifications independently.
- **Group by weekday:** It would produce up to seven rows and require another pivot or aggregation to reach the requested two columns.
- **Saturday:** `WEEKDAY` returns five and the row counts as weekend.
- **Sunday:** It returns six and also counts as weekend.
- **Monday through Friday:** Their values zero through four count as working days.
- **Several tasks on one date:** Every task row contributes separately.
- **Assignee repetition:** It has no effect because the requested count is not distinct by assignee.
- **Empty table extension:** Exact `SUM` returns null; `COALESCE` would be required for zero.
- **Null date extension:** `IN` and `NOT IN` on null produce null, so such a row contributes to neither sum; the stated schema semantics avoid this case.
- **Single output row:** No ordering clause is useful.
- **Primary key:** `task_id` uniqueness ensures each stored task is one row, although the aggregation does not need to reference the key explicitly.
- **Boundary between Friday and Saturday:** `WEEKDAY` changes from four to five, exactly where the weekend predicate becomes true.
- **Boolean arithmetic:** This compact syntax is MySQL-specific behavior; databases without numeric Booleans should use `CASE`.
- **No double counting:** `IN` and `NOT IN` are complementary for non-null weekday values, so the two totals sum to the task-row count.
- **Date rather than timestamp:** The schema's date type avoids timezone-dependent day changes during classification.
