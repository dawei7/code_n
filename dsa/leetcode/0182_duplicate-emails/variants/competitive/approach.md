## General

**Group by the value whose repetition matters**

The competitive query groups `Person` rows by `Email`. Each group contains all
people whose stored email values compare equal under the database collation.

The unique `id` column is not involved. Duplication means one email associated
with more than one row, regardless of the employees' identifiers.

After grouping, selecting `Email` returns one representative value for each
email group, so duplicates in the source do not appear repeatedly in the
result.

**Count every row in each group**

`COUNT(*)` counts all rows, including rows containing null in individual
columns. The predicate:

`HAVING COUNT(*) > 1`

retains only groups of size at least two.

The email field is guaranteed non-null, so `COUNT(Email)` would give the same
count. `COUNT(*)` more directly states that group membership rows are being
counted.

**Why `HAVING` is the correct phase**

SQL logically forms groups after reading and filtering input rows. Aggregate
values such as `COUNT(*)` do not exist at the ordinary `WHERE` phase.

`HAVING` filters the completed groups. A condition such as
`WHERE COUNT(*) > 1` is invalid because `WHERE` operates before aggregation.

No separate outer subquery is needed: grouping, aggregate filtering, and final
projection can all be expressed in one select block.

**Trace the sample**

The two `a@b.com` rows form one group with count two. It passes and returns
`a@b.com`.

The single `c@d.com` row forms a group with count one. It fails the predicate
and is omitted.

If an email appeared five times, its count would be five but the group would
still yield one output row. If all emails were unique, the result would be
empty.

**Why no `DISTINCT` is required**

`GROUP BY Email` already produces at most one result row per distinct group
key. Adding `SELECT DISTINCT Email` would repeat work without changing the
logical result.

The required output itself is one row per duplicated address, which matches
the natural grouped cardinality.

**Soundness and completeness**

A returned email belongs to a group whose row count exceeds one, so it appears
more than once and is genuinely duplicate.

Any duplicate email contributes at least two rows to its group. That group
passes `HAVING` and its key is selected. Therefore every duplicate is returned.

These two directions establish the exact result set independently of physical
row order.

Notice that the threshold is strictly greater than one, rather than greater
than or equal to one. Every existing email has a group of size at least one,
so the latter test would incorrectly return unique addresses as well. The
strict threshold is the small condition that turns ordinary grouping into
duplicate detection.

The query also does not need `MIN(id)`, `MAX(id)`, or a pair of IDs as evidence.
Those values could identify members of a duplicate group, but the required
answer contains only the shared email. Avoiding unrelated selected columns
keeps the grouping contract unambiguous and prevents MySQL mode-dependent
behavior for nonaggregated columns.

**Case and collation**

The schema says emails contain no uppercase letters, avoiding questions about
whether `A@b.com` and `a@b.com` should be normalized by the application.

SQL string equality still follows the column's collation. With all-lowercase
valid input, the intended exact duplicates group naturally. A production email
policy could require binary collation or broader normalization, but that lies
outside the Reference.

**NULL and output order**

Emails are guaranteed not null. Without that guarantee, all nulls would form
one group under `GROUP BY`, and `COUNT(*)` could report a null duplicate. This
query correctly relies on the stated input contract.

No `ORDER BY` is present because any result order is accepted. Grouping does
not itself promise an ordering.

**Source comment accuracy**

The file comments claim $O(n^2)$ time. Normal SQL grouping does not compare
every row with every other row. Engines usually sort by the key or build a hash
table, yielding far better standard bounds.

The actual query is a single valid statement in MySQL; its leading hash
comments are dialect-specific but do not affect the relational logic.

## Complexity detail

For $n$ rows, a sort-based aggregate takes $O(n\log n)$ time and can use
$O(n)$ working space. This matches the manifest.

A hash aggregate can be expected $O(n)$ time with $O(u)$ memory for $u$
distinct emails. An email index can change the plan again. The source's
$O(n^2)$ comment is overly pessimistic for conventional implementations.

## Alternatives and edge cases

- **Count subquery:** Produce `(Email, count)` groups in a derived table and filter outside; correct but unnecessary.
- **Pandas groupby:** Group by email, compute sizes, and retain counts above one.
- **Self-join:** Match equal emails with different IDs, then deduplicate; potentially creates a large intermediate.
- **Exactly one duplicate pair:** Returns the email once.
- **Several duplicate groups:** Returns one row for each group.
- **All unique:** Returns an empty result.
- **Empty table:** Also returns an empty result.
- **Non-null contract:** Prevents a null group from being reported.
- **Lowercase guarantee:** Avoids application-level case normalization.
- **Any order:** No `ORDER BY` is needed.
