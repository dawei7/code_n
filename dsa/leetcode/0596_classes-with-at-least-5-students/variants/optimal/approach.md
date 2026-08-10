## General

Each row represents one enrollment: one `student` in one `class`. The requested answer depends on how many enrollment rows belong to each class, so the natural relational operation is grouping by class and filtering groups by their size.

**Creating one group per class**

The query selects `class` and writes:

```sql
GROUP BY 1
```

The ordinal `1` refers to the first expression in the `SELECT` list, which is `class`. It is therefore equivalent to `GROUP BY class`. All Math enrollments become one group, all English enrollments another, and so on.

Ordinal grouping is concise, but spelling out the column can be easier to maintain: if the select-list order changes, `GROUP BY 1` may begin referring to a different expression. In this exact query, its meaning is unambiguous.

**Why counting rows counts students**

`COUNT(1)` counts every row in a group because the literal 1 is never `NULL`. The composite primary key `(student, class)` guarantees that the same student-class enrollment cannot appear twice. Therefore, the number of rows in a class group equals the number of distinct students enrolled in that class.

Without that uniqueness guarantee, repeated duplicate enrollment rows could inflate `COUNT(1)`, and `COUNT(DISTINCT student)` would be necessary. Here, ordinary row count is sufficient and simpler.

For the sample, Math’s group contains rows for A, C, E, G, H, and I, giving count six. Every other class group has count one.

**Why the condition belongs in `HAVING`**

The query uses:

```sql
HAVING COUNT(1) >= 5
```

`WHERE` filters individual rows before grouping; it cannot decide based on the final size of a group. `HAVING` filters after aggregation, so it can retain or discard an entire class according to `COUNT(1)`.

The comparison is `>= 5` because “at least five” includes exactly five. A strict `> 5` would incorrectly exclude a class with precisely five students.

The aggregate count guides filtering but is not selected. The output needs only the class names, so each surviving group contributes its `class` value and nothing else.

**Logical execution order**

Although SQL is written with `SELECT` first, a useful conceptual order is:

1. `FROM Courses` supplies enrollment rows.
2. `GROUP BY class` partitions them by class name.
3. `COUNT(1)` computes each group’s enrollment count.
4. `HAVING COUNT(1) >= 5` keeps qualifying groups.
5. `SELECT class` returns their names.

The result order is unrestricted, so no `ORDER BY` is needed.

**Why the query is correct**

For every class $c$, grouping creates exactly one group containing all and only rows whose `class` equals $c$. Composite-key uniqueness ensures each enrolled student contributes exactly one row to that group, so `COUNT(1)` equals the true number of students in $c$.

`HAVING` retains this group exactly when that number is at least five. Hence, every qualifying class is returned and every class with fewer than five students is excluded. Because one group yields one selected class value, the output contains no duplicate row for a class.

There is no need to inspect student names beyond counting their unique enrollment rows. There is also no need for a subquery: `HAVING` lets aggregation and group filtering happen in the same query block.

**What primary-key semantics contribute**

The primary key has two columns. A student may appear in several classes, because `student` alone is not unique. A class may contain many students, because `class` alone is not unique. Only the exact pair is unique. This is precisely the data model needed for enrollment counting.

Counting globally distinct students would answer a different question. The grouping boundary matters: each student is counted once *within each class* in which they appear.

## Complexity detail

Let $n$ be the number of enrollment rows and $c$ the number of distinct classes. A hash aggregation reads all $n$ rows and keeps one counter per class, taking expected $O(n)$ time and $O(c)$ state.

A sort-based aggregation may order rows by class in $O(n\log n)$ time, while an index on `class` may support streaming groups. The manifest’s $O(n\log c)$ time is a conservative grouping-oriented bound. Filtering the $c$ completed groups is $O(c)$.

Logical working space is $O(c)$ for hash counters, bounded by $O(n)$ as declared by the manifest. A database may materialize or sort more rows depending on its plan. The output contains at most $c$ class names.

## Alternatives and edge cases

- **Grouped subquery:** Compute `class, COUNT(*) AS total` in a subquery and filter `total >= 5` outside. Correct, but `HAVING` expresses the same operation more directly.
- **`COUNT(DISTINCT student)`:** Robust if duplicate enrollment rows are possible, but redundant under the composite primary key.
- **`WHERE COUNT(...)`:** Invalid logical placement because `WHERE` runs before aggregate groups exist.
- **Window count:** Annotate each row with `COUNT(*) OVER (PARTITION BY class)`, filter, then use `DISTINCT class`. It retains unnecessary row detail and needs deduplication.
- **Exactly five students:** Must be included; the boundary operator is `>=`.
- **Four students:** Must be excluded.
- **One student in several classes:** Counted once in each class group, which is correct.
- **Duplicate enrollment pair:** Forbidden by the primary key. If the schema changed, row counting could overcount.
- **Empty table:** No groups exist, so the result is empty.
- **Any output order:** No sorting is required.
- **Ordinal grouping:** `GROUP BY 1` means the selected `class` column here; explicit naming is clearer if columns may be reordered.
- **Counting a nullable column:** `COUNT(1)` avoids null-sensitive undercounting. Every row contributes exactly one.
- **Output schema:** The count is used only by `HAVING`; returning it would add an unrequested column.
