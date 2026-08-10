## General

**Identify one permanent keeper for every email**

The task is destructive: it must delete rows, not merely display a deduplicated
result. Before deleting anything, the query defines which rows must survive.
For each email group, the primary key's minimum value is the unique required
keeper ID.

Because `id` is a primary key, no two rows share that value. Even if many rows
have the same email, `MIN(id)` therefore identifies exactly one original row in
that group.

**Build the keeper-ID set with grouping**

The innermost `SELECT * FROM Person` reads a snapshot-like derived relation
named `p`. The surrounding query groups those rows by `email` and computes
`MIN(id)` once for every group. Conceptually, its result is a one-column set of
IDs that are protected from deletion.

For the sample, the `john@example.com` group contains IDs 1 and 3, so its keeper
is 1. The `bob@example.com` group contains only ID 2, so its keeper is 2. The
subquery thus produces IDs 1 and 2.

Grouping by email text is the correct identity rule. The lowercase guarantee
means the application does not need to normalize letter case before grouping,
although actual SQL string comparison still follows the column's collation.

**Why there is an extra derived-table layer**

MySQL restricts some updates and deletes that read directly from the same target
table in a nested subquery, producing the familiar “can't specify target table”
error. Wrapping `SELECT * FROM Person` in another derived table gives the
aggregate query a named intermediate source and is a conventional workaround.

The layer is not part of the mathematical deduplication idea. Logically, it
still contains the same Person rows. Its purpose is to make the read-before-
delete structure acceptable to the target SQL engine.

**Delete every ID outside the keeper set**

The outer statement scans `Person` and applies `id NOT IN (keeper IDs)`. A row
whose ID is one of the group minima fails the predicate and remains. Every
other row belongs to some email group but is not that group's minimum, so its
ID is absent and the row is deleted.

This use of `NOT IN` avoids joining the target row to every smaller duplicate.
The aggregate computes each group's threshold once, after which deletion is a
membership decision.

**Why `NOT IN` is safe for these subquery values**

`NOT IN` is dangerous when its subquery can emit `NULL`, because SQL's
three-valued logic may turn every comparison into unknown. Here the subquery
emits `MIN(id)`, and `id` is a primary key. Primary-key values are non-null, and
every emitted group contains at least one row, so every keeper ID is non-null.
The usual null-poisoning issue therefore does not occur.

The local description does not explicitly say whether `email` itself can be
null. If null emails existed, `GROUP BY email` would place them in one group and
keep the smallest ID among them. Whether multiple missing emails should count
as duplicates would be a business-rule question, but the query's behavior is
well-defined.

**Trace the mutation, not just a result set**

With keeper set `{1, 2}`, row 1 remains because its ID is in the set, row 2
remains for the same reason, and row 3 is deleted. After the statement commits,
the underlying `Person` table itself contains only the two keeper rows.

There is no output `SELECT` in the solution. The platform displays the table
after executing the mutation. Omitting an `ORDER BY` is correct because final
row order does not matter and table storage order is not a relational
guarantee anyway.

**Why every surviving row is necessary**

Take any surviving row. Its ID occurs in the grouped minimum set, so it is the
smallest ID for its email. Exactly one such ID exists because the primary key is
unique. Thus every survivor is the required representative of one email group.

Now take any nonminimum duplicate row. Its email group emits a strictly smaller
keeper ID, while its own ID is not emitted by any other group because IDs are
globally unique. The `NOT IN` condition is true and deletes it. Therefore every
duplicate beyond the required representative is removed.

**Transaction and concurrency context**

The reasoning treats the statement's source rows consistently for one database
operation. Real applications with concurrent inserts may need an appropriate
transaction isolation level or lock policy to ensure the table does not change
between logical selection and deletion. That operational concern lies outside
the single-statement challenge but explains why deduplication is normally run
within controlled database semantics.

## Complexity detail

Let $n$ be the number of Person rows and $u$ the number of distinct emails. The
derived read uses $O(n)$ data, grouping can take expected $O(n)$ with hashing or
$O(n\log n)$ with sorting, and deleting by an efficiently materialized keeper
set can be linear or index-assisted.

The manifest records conservative $O(n^2)$ time and $O(n)$ space. Quadratic
time is possible if membership against the derived result is executed as
repeated scans rather than an indexed or hashed anti-join. Materializing source
rows and keeper IDs requires up to $O(n)$ working storage. SQL query text does
not force one physical plan, so actual behavior depends on MySQL's optimizer
and indexes.

## Alternatives and edge cases

- **Self-join delete:** Delete a row whenever another row has the same email and smaller ID; concise MySQL syntax but can generate many matching pairs.
- **Window function:** Rank rows by `id` within each email and delete ranks above one through an engine-supported writable relation.
- **Pandas grouping:** The local editorial broadcasts each email's minimum ID and drops nonminimum DataFrame rows in place.
- **Single row per email:** Its ID is the group minimum and it remains.
- **Many duplicates:** Exactly the smallest-ID row survives, regardless of group size.
- **Primary-key non-nullness:** Guarantees the keeper subquery cannot poison `NOT IN` with null.
- **Nullable email:** The query treats all null emails as one group; confirm that semantic if the domain expands.
- **Duplicate letter case:** Input is lowercase, while database collation still defines equality.
- **Empty table:** The keeper set and deletion target are empty, so nothing changes.
- **Final ordering:** Not specified and not controlled by `DELETE`.
