## General

**Separate the two intended solutions**

The competitive file contains two independent `SELECT` statements. The first
tries to compute run lengths with MySQL user variables. The second uses three
self-joined aliases.

There is no semicolon between them. As one script, SQL encounters a second
`SELECT` where the first statement has not been terminated, causing a syntax
error. Even with a separator, a single-query judge generally expects only one
result set.

One alternative must be selected and the other removed from executable source.

**Intended user-variable run counting**

The first query initializes `@counter` and `@prev`. For each row, it intends to
compare the current `Num` with `@prev`. An equal value increments the run
counter; a change resets it to one. It then assigns the current value to
`@prev`.

The outer query keeps derived rows whose count is at least three and applies
`DISTINCT(Num)` so a longer run emits the value once.

Conceptually, this is a one-pass run-length scan. It would correctly detect the
third and later positions within each equal-value run if rows were processed
in increasing ID order and assignments occurred in the written expression
order.

**Missing order makes the first alternative incorrect**

The inner variable query has no `ORDER BY id`. SQL tables are unordered
relations, and the engine may read `Logs` in any physical or optimized order.
The row stored in `@prev` is therefore not guaranteed to be the preceding log
event.

Adding an outer `ORDER BY` after counts would be too late; the run counter must
be evaluated in sequence order. The ordering belongs in the row stream used by
the variable assignments.

Even with an inner order, MySQL user-variable assignment order inside a select
list has historically been unsafe and optimizer-dependent. Modern window
functions are the reliable choice.

**Second intended solution uses three aliases**

The second query aliases `Logs` as `l1`, `l2`, and `l3` and requires:

- `l2.Id = l1.Id + 1`;
- `l3.Id = l2.Id + 1`;
- all three `Num` values equal.

Every resulting joined row is a three-ID consecutive window holding one value.
`SELECT DISTINCT l1.Num` collapses overlapping windows and separate qualifying
runs of the same value.

This relational logic is sound under the challenge's consecutive-ID model and
does not rely on row evaluation order.

**Trace both concepts**

For IDs one through three containing one, a correctly ordered counter would
produce counts one, two, and three; the third row passes the outer filter.
The self-join produces triple `(1,2,3)`.

For a four-row run, the counter produces qualifying counts three and four,
while the join produces two overlapping triples. In both cases, `DISTINCT`
returns the value once.

For the two twos at IDs six and seven in the sample, the counter reaches only
two and the join cannot find a third alias row, so two is excluded.

**Why the self-join is complete**

Any run of at least three has some first three IDs satisfying the adjacency and
equality predicates. Therefore its value is emitted. Any emitted value came
from such a triple, so it genuinely qualifies.

The self-join's comma syntax is an older form equivalent to a cross join
filtered by `WHERE`. Explicit `JOIN ... ON` syntax is clearer and helps keep
relationship predicates next to their joins.

**Material exact-file status**

As stored, the missing statement separator makes the file invalid. If only one
query is retained, the second self-join alternative is the safer choice.

The first alternative would still need a guaranteed increasing-ID input order
and a replacement for user-variable side effects. Merely inserting a semicolon
does not repair those semantic risks.

**Consecutive rows versus ID arithmetic**

The self-join interprets consecutive events as IDs differing by one. This
matches the standard autoincrement challenge data. If deletions could leave
gaps and adjacency meant neighboring surviving rows, use `LAG` ordered by ID
instead.

## Complexity detail

The intended user-variable scan could be $O(n)$ time plus distinct processing,
but its ordering is not validly specified.

The three-way self-join can be efficient with the primary-key index: candidate
next IDs are directly probed, followed by deduplication. A sort-based distinct
plan can fit the manifest's $O(n\log n)$ time and $O(n)$ space. Without useful
indexes, naive join work can be much larger. Exact-file syntax failure prevents
either plan from running as written.

## Alternatives and edge cases

- **Keep only the explicit self-join:** It is the safer of the two bundled alternatives.
- **`LAG(num, 1)` and `LAG(num, 2)`:** Compare the current value with the preceding two values under `ORDER BY id`.
- **Run identifiers with window functions:** Mark changes, cumulatively number runs, and group counts.
- **Long runs:** `DISTINCT` removes duplicate qualifying windows.
- **Multiple runs of one value:** Still return one row for that number.
- **Two-row run:** Must not qualify.
- **Unordered SQL input:** User-variable state has no sequence meaning without a guaranteed order.
- **ID gaps:** Decide whether exact numeric adjacency or row-order adjacency is intended.
- **Two statements:** A semicolon alone may yield two result sets; submit one query.
- **User-variable deprecation:** Prefer deterministic window or join logic in modern MySQL.
