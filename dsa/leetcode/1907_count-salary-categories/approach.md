## General

**Separate the required labels from observed data.** A normal `GROUP BY` returns only categories that occur. This problem requires all three rows even when one count is zero. CTE `S` explicitly constructs the three category labels using constant `SELECT` statements combined by `UNION`. It is the guaranteed output skeleton.

**Classify every account exactly once.** CTE `T` uses a `CASE` expression. Income below 20000 maps to `"Low Salary"`. Income above 50000 maps to `'High Salary'`. Every remaining income falls in the inclusive interval 20000 through 50000 and maps to `'Average Salary'`.

The order of branches makes the boundaries precise. Exactly 20000 fails the low test and reaches the else branch. Exactly 50000 fails the high test and also reaches else. Values cannot belong to two categories, and every ordinary integer income belongs to one.

**Aggregate observed counts.** `GROUP BY 1` groups by the first selected expression, the computed category. `COUNT(1)` counts account rows in each group. Since `account_id` is unique, every input row represents one account and contributes exactly one to its category. `T` contains at most three rows, but it omits any category with no accounts.

**Restore missing categories with a left join.** The final query starts from `S` and uses `LEFT JOIN T USING (category)`. Every skeleton category remains even if `T` has no matching row. `USING` matches the identically named category columns and emits one shared category field.

For a missing match, `accounts_count` is SQL `NULL`. `COALESCE(accounts_count, 0)` replaces that null with numeric zero. Observed counts are non-null and pass through unchanged.

**Trace the example.** Three incomes exceed 50000, one lies below 20000, and none lies between the inclusive boundaries. `T` therefore has low count one and high count three but no average row. Joining from `S` retains all labels; the average match is null and becomes zero.

**Why the skeleton is more reliable than three scans.** One could run a separate aggregate for each category and union them. The exact query scans/classifies `Accounts` conceptually once, groups the result, then attaches it to three constant labels. It centralizes boundary logic and guarantees a category cannot be forgotten.

The classification is a true partition of the integer number line. A value cannot be simultaneously below 20000 and above 50000, and the closed interval between those strict regions is exactly the average category. Consequently, the three grouped counts sum to the total number of account rows; this is a useful mental consistency check for both boundaries and missing categories.

**Why `UNION` is harmless here.** The three literal labels are distinct, so `UNION`'s duplicate elimination does not remove any intended row. `UNION ALL` would produce the same skeleton with potentially less deduplication work, but the relation has only three rows, making the difference constant.

**Empty input behavior.** If `Accounts` contains no rows, `T` is empty. The left join still returns the three `S` rows, and all counts become zero. This is exactly why the query must not use an inner join.

**Any output order is valid.** There is no `ORDER BY` because the statement permits any order. The order in which the literal union or join happens to return rows is not guaranteed.

## Complexity detail

Let $A$ be the number of account rows. Classification and aggregation inspect each account once, giving expected $O(A)$ time with hash grouping. Sorting-based grouping may use $O(A\log A)$ physically, but only three possible group keys exist, so engines can maintain constant-sized aggregate state efficiently.

The skeleton and grouped result each contain at most three rows. Logical auxiliary aggregation space is $O(1)$ with respect to $A$, matching the manifest. The final output is exactly three rows.

Database plans may scan the table and evaluate `CASE` row by row. Indexes are not required because all rows must contribute to some count.

## Alternatives and edge cases

- **Three conditional aggregates with `UNION ALL`:** Each branch can count one category and always returns a row, but may conceptually scan `Accounts` three times. It is correct and simple for three fixed labels.
- **Single-row conditional sums then unpivot:** Compute all three counts in columns and convert them to rows. This can ensure one scan but uses more SQL machinery.
- **Inner join from `S` to `T`:** Incorrect when a category is empty because that required row disappears.
- **Income exactly 20000:** It belongs to Average Salary through the `ELSE` branch.
- **Income exactly 50000:** It also belongs to Average Salary; high is strictly greater.
- **No accounts in a category:** Missing grouped row becomes zero through `COALESCE`.
- **No accounts at all:** All three skeleton rows survive and each count is zero.
- **Positional grouping:** `GROUP BY 1` refers to computed category because it is selected first. Naming it explicitly would be more maintainable but equivalent.
- **Double-quoted low label:** MySQL normally treats `"Low Salary"` as a string unless ANSI_QUOTES mode changes quoting semantics; single quotes are more portable, but the exact source uses both styles.
- **Count reconciliation:** Because each non-null income reaches exactly one `CASE` result, the three returned counts should add up to the number of accounts. A different total signals altered null or boundary assumptions.
