## General

Each student row records a `department_id`. A student is invalid for this report when that identifier is absent from the primary-key `id` column of `Departments`. The query expresses this set-membership test directly:

`department_id NOT IN (SELECT id FROM Departments)`.

**Build the set of current identifiers**

The subquery `SELECT id FROM Departments` produces every department identifier that currently exists. Because `id` is a primary key, these values are unique and non-null under ordinary SQL primary-key semantics. Duplicate removal is unnecessary.

For each row of `Students`, `NOT IN` asks whether its recorded `department_id` differs from every value returned by that subquery. A true result means no matching current department exists, so the student is enrolled under an obsolete identifier.

The outer `SELECT id, name` returns the student’s own primary-key identifier and name, not the missing department identifier. These are exactly the two requested output columns.

The result order is unrestricted, so there is no `ORDER BY`. Omitting an unnecessary sort avoids work and still satisfies the contract.

In the example, department identifiers one, seven, and thirteen appear in `Departments`. Students whose values are fourteen, seventy-seven, seventy-four, or thirty-three pass `NOT IN` and are returned. Students referring to one, seven, or thirteen are filtered out.

**Why every selected row is correct**

If a student passes the predicate, its `department_id` is unequal to every current department `id`, so its department no longer exists and the row belongs in the answer. If a student’s department exists, the subquery contains an equal identifier, making `NOT IN` false and excluding that row. Thus the predicate is both necessary and sufficient for non-null department identifiers.

The use of primary keys also means a matching department appears at most once. Multiplicity would not change membership truth, but uniqueness helps the database build or use an efficient lookup structure.

**SQL null semantics**

`NOT IN` needs care in generalized schemas because SQL uses three-valued logic. If the subquery contained `NULL`, comparisons against that value could make the predicate unknown for otherwise absent identifiers. Here, `Departments.id` is a primary key and therefore cannot be null, so that classic trap does not arise on the right side.

If `Students.department_id` itself is null, `NULL NOT IN (...)` is unknown and the row is not returned. The task describes students as enrolled in a recorded department identifier, so the intended rows use actual identifiers. If a generalized requirement considered a null department invalid, `NOT EXISTS` or an explicit null condition would be safer.

## Complexity detail

Let $D$ be the number of department rows and $S$ the number of student rows.

A typical database plan materializes or indexes the department identifiers in $O(D)$ time and space, then scans students and performs expected $O(1)$ membership checks, for $O(D + S)$ time. With $N = D + S$, this is $O(N)$ expected time and $O(D)$ working space, matching the manifest model.

If a suitable index on `Departments.id` is used directly, each student lookup may be $O(\log D)$, giving $O(S\log D)$ lookup time with little additional materialization. SQL complexity is plan-dependent, but the primary key gives the optimizer an efficient access path.

The output can contain up to $S$ rows; output storage is separate from the query’s auxiliary working space.

## Alternatives and edge cases

- **`NOT EXISTS`:** A correlated anti-membership test using matching IDs is robust to nulls and often optimized into an anti-join.
- **Left anti-join:** Left-join departments on the identifier and keep rows where the joined department ID is null. It makes the missing-match interpretation visually explicit.
- **Application-side filtering:** Loading both tables and comparing identifiers outside SQL duplicates database work and moves unnecessary data.
- **Empty department table:** Every student with a non-null `department_id` passes because the right-hand set is empty.
- **No invalid students:** The predicate rejects every row and the result is an empty table.
- **Repeated student names:** Selection is based on department membership and returns student IDs, so equal names would not merge rows.
- **Non-null primary key:** The right-side `id` cannot contain null, preventing the most dangerous `NOT IN` behavior.
- **Null student department:** The exact query omits it because the predicate becomes unknown. Add explicit handling if null should mean invalid.
- **Any output order:** No sort is required, and consumers must not infer a stable order from the execution plan.
- **Return columns:** The query returns the student’s `id` and `name` only; the obsolete department value is used solely for filtering.
- **No `DISTINCT` needed:** `Students.id` is a primary key, and the subquery is used as a membership set rather than joined multiplicatively. Each qualifying student row can appear only once in the output.
- **Missing foreign-key enforcement:** The very existence of invalid department identifiers means this dataset is not relying on an active foreign-key constraint that rejects them. The query intentionally detects those orphan references.
- **Department renamed but ID retained:** Validity depends only on the identifier. Changing a department’s name does not make its students invalid as long as the same `Departments.id` remains present.
