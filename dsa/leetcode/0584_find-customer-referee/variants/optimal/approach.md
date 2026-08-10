## General

The required customers fall into two categories:

- their `referee_id` is a real value other than 2;
- their `referee_id` is `NULL`, meaning nobody referred them.

The apparent predicate `referee_id != 2` handles the first category but not the second. Understanding why requires SQL’s treatment of missing values.

**Why `NULL != 2` is not true**

SQL uses three-valued logic. A comparison can evaluate to true, false, or unknown. `NULL` represents an absent or unknown value, so comparing it with an ordinary value does not produce true or false:

```sql
NULL != 2
```

evaluates to unknown. A `WHERE` clause retains only rows whose condition is true; it discards both false and unknown results. Therefore, a plain inequality would accidentally remove customers with no referee even though the problem explicitly wants them.

**How `COALESCE` combines the two cases**

The exact query uses:

```sql
WHERE COALESCE(referee_id, 0) != 2
```

`COALESCE` returns its first non-`NULL` argument.

- If `referee_id` is present, `COALESCE(referee_id, 0)` returns the actual ID. The row passes exactly when that ID is not 2.
- If `referee_id` is `NULL`, `COALESCE` returns 0. Since 0 is not 2, the row passes.

Zero is used only as a comparison substitute. It is not selected, written back to the table, or presented as the customer’s actual referee. Even if zero were itself an allowed stored ID, a real zero should qualify because it is not 2, so the substitution has the same truth outcome required for this particular predicate.

The more literal equivalent is:

```sql
WHERE referee_id != 2
   OR referee_id IS NULL
```

That form explicitly names both categories. The `COALESCE` form compresses them into one two-valued comparison.

**Why the query needs no join**

The problem does not ask for the referee’s name or any other referee details. It asks only whether the stored referee ID equals 2. Every required value—customer name and referee ID—is already in the `Customer` row. A self-join would add work without supplying information needed by the condition.

The query projects only `name` because that is the requested output column:

```sql
SELECT name
FROM Customer
```

Result order is unrestricted, so `ORDER BY` is intentionally absent.

**Tracing the sample**

Will, Jane, and Bill have `NULL` referee IDs. `COALESCE` maps each missing value to zero for the comparison, so all three pass. Zack has referee ID 1, which is not 2, so he passes. Alex and Mark each have referee ID 2, so `COALESCE` leaves 2 unchanged and the inequality is false; both are excluded.

It is important that customer ID 2 is not automatically excluded. Jane’s own `id` is 2, but her `referee_id` is `NULL`. The rule concerns *who referred the customer*, not the customer’s own ID. Jane therefore qualifies. Mixing up `id` and `referee_id` would answer a different question.

**Why the query is correct**

Take any customer row. If `referee_id = 2`, the value is non-`NULL`, `COALESCE` returns 2, and `2 != 2` is false, so the row is excluded exactly as required.

If `referee_id` is a non-`NULL` value other than 2, `COALESCE` returns that value and the inequality is true, so the row is included under the first category.

If `referee_id` is `NULL`, `COALESCE` returns zero and the inequality is true, so the row is included under the second category. These cases are exhaustive and mutually exclusive. Thus, the filter keeps exactly customers not referred by ID 2, including customers with no referee.

Selecting `name` then returns precisely the requested data. No grouping is necessary because each input row represents one customer and `id` is a primary key. Duplicate names, if allowed, correspond to different customer rows and should not be silently collapsed with `DISTINCT`.

**A broader lesson about nulls**

Replacing `NULL` with a sentinel is safe only when the sentinel produces the intended truth value. Here, every missing referee must behave like “not 2,” and zero satisfies that single comparison. For a different task—such as finding referees greater than zero or distinguishing missing from an actual zero—`COALESCE(..., 0)` could change semantics. The explicit `IS NULL` form is often clearer when the domain or predicate is more complicated.

Also, `referee_id = NULL` would not fix the issue. Equality with `NULL` is unknown for the same reason inequality is. SQL requires `IS NULL` or a null-handling function.

## Complexity detail

Let $n$ be the number of rows in `Customer`. Without a selective usable index for this predicate, the database scans all rows, evaluates one constant-time expression per row, and takes $O(n)$ time. It can stream qualifying names, requiring $O(1)$ auxiliary working memory outside the output.

The result itself can contain $O(n)$ names, and database execution buffers may materialize rows. If output storage is included, total result space is $O(n)$. There is no grouping, join, or ordering in the query, so the exact SQL does not inherently require $O(n\log n)$ work.

This differs from the manifest’s conservative $O(n\log n)$ time and $O(n)$ space declaration. The space bound safely includes output/materialization, but the query’s logical operation is a linear filter. SQL remains declarative, and a particular engine’s physical behavior depends on storage and indexes, yet no sort is requested.

## Alternatives and edge cases

- **Explicit disjunction:** `referee_id <> 2 OR referee_id IS NULL` most directly mirrors the two requirements and avoids choosing a sentinel.
- **Null-safe comparison:** In MySQL, `NOT (referee_id <=> 2)` uses the null-safe equality operator and negates it. It is compact but less portable and less familiar.
- **Plain inequality:** `referee_id != 2` is incorrect because rows with `NULL` evaluate to unknown and are filtered out.
- **Equality to `NULL`:** `referee_id = NULL` is also unknown, never the proper null test. Use `IS NULL`.
- **`NOT IN (2)`:** This has the same null problem as ordinary inequality; `NULL NOT IN (2)` is unknown.
- **Self-join to referees:** Unnecessary because only the numeric referee ID is tested, not any referring customer attribute.
- **Customer whose own ID is 2:** The customer still qualifies unless their `referee_id` is 2. The two columns have different meanings.
- **No referee:** A `NULL` value must be included and remains unmodified in the table; zero is only a temporary predicate value.
- **Referee ID exactly 2:** The row is the only category excluded.
- **Any other referee ID:** Negative, zero, positive, or large values all satisfy “not 2” if the schema permits them.
- **Duplicate customer names:** The output can contain repeated names from distinct customer rows. Adding `DISTINCT` would change the row semantics without a requirement.
- **Any result order:** No `ORDER BY` is needed, avoiding unnecessary sorting.
- **Sentinel caution:** `COALESCE(referee_id, 0)` is valid because both missing and actual zero should pass `!= 2`. A sentinel must be reconsidered whenever the comparison changes.
