## General

**Turn duplication into the existence of a smaller twin**

The competitive statement reads the target table twice through aliases `p1`
and `p2`. Alias `p1` represents a candidate row to delete. Alias `p2` represents
evidence that the candidate is not the keeper.

A candidate should be deleted exactly when another row has the same email and
a smaller ID. The two `WHERE` conditions express those two facts directly:
`p1.Email = p2.Email` establishes the same group, and `p1.Id > p2.Id`
establishes that `p1` is not the minimum.

**Understand MySQL's multi-table delete syntax**

`DELETE p1 FROM Person p1, Person p2` is a MySQL multi-table delete form. The
name after `DELETE` identifies which alias's physical rows are removed. Although
both aliases participate in matching, only rows represented by `p1` are
deleted; `p2` rows serve as witnesses.

The comma between table aliases forms a Cartesian product before filtering in
relational terms. The `WHERE` predicates retain only meaningful same-email,
ordered pairs. An explicit `JOIN Person p2 ON ...` could state the relationship
more visibly, but the result is equivalent.

**Why the smallest ID survives**

Fix one email group and let its smallest ID be $m$. For the row with ID $m$,
there cannot be another same-email row with an ID smaller than $m$. It produces
no qualifying `(p1, p2)` pair, so it is never selected as a deletion target.

Every other row in that group has ID greater than $m$. Pairing that row as
`p1` with the minimum row as `p2` satisfies both predicates, so the larger row
is selected for deletion. This establishes that exactly the minimum survives.

**Multiple witnesses do not cause multiple deletions**

Suppose one email has IDs 1, 3, and 8. Candidate ID 8 matches both ID 1 and ID 3
as smaller witnesses, producing more than one join pair. A physical table row
is still deleted once. Duplicate qualifying join combinations do not require a
`DISTINCT` clause and do not attempt to remove some extra row.

ID 3 matches ID 1 and is deleted. ID 1 matches no smaller witness and remains.
Thus group size does not change the final rule.

**Trace the sample**

Rows 1 and 3 share `john@example.com`. Pair `(p1.id = 3, p2.id = 1)` passes
the greater-ID condition, so row 3 is deleted. The reverse pair fails because
1 is not greater than 3.

`bob@example.com` appears only at ID 2. There is no different same-email row
with a smaller ID, so row 2 is never targeted. The final table contains IDs 1
and 2.

**Why all and only nonminimum duplicates are removed**

Any deleted `p1` has a same-email `p2` with smaller ID, proving `p1` cannot be
the required smallest representative. Therefore no necessary keeper is
deleted.

Conversely, every row that is not the minimum of its email group can use that
group's minimum row as `p2`. The join predicates succeed, so that nonminimum row
is deleted. This covers every unwanted duplicate and leaves one row per email.

**Email equality and null behavior**

The lowercase guarantee avoids application-side case normalization, but SQL
equality follows the email column's collation. Under a case-insensitive
collation, values differing only by case would match even though such uppercase
input is outside the stated domain.

If `Email` were null, SQL evaluates `NULL = NULL` as unknown rather than true.
Multiple null-email rows would not match each other and would all survive. The
Reference describes rows as containing lowercase emails but does not explicitly
spell out `NOT NULL`; the intended challenge data uses actual email values. A
null-supporting generalization should use a null-safe equality operator or an
explicit policy.

**Mutation and result order**

This is a `DELETE`, as explicitly required for SQL users. It modifies `Person`
and does not return a selected result table. The challenge driver displays the
remaining rows after execution.

No ordering clause is relevant to deletion, and relational tables have no
inherent row order. The Reference accepts the final table in any order.

## Complexity detail

Let $n$ be the number of rows. A naive self-join considers $n^2$ alias pairs,
then filters them, giving the source and manifest time bound $O(n^2)$. An index
on `(Email, Id)` or optimizer transformation can make witness lookup much more
efficient.

The manifest records $O(n)$ space, which can describe bookkeeping or an
optimized execution. A literal materialized self-join could produce up to
$O(n^2)$ matching pairs for one large duplicate group, though a database need
not materialize them all before deleting targets. SQL resource use is therefore
physical-plan dependent.

## Alternatives and edge cases

- **Grouped keeper set:** Compute `MIN(id)` per email once and delete IDs outside it, as the optimal variant does.
- **Explicit self join:** Move both predicates into an `ON` clause for clearer modern SQL without changing semantics.
- **Pandas in-place drop:** Compute group minima and remove rows whose IDs differ from them.
- **One occurrence:** No smaller same-email witness exists, so the row survives.
- **Several smaller witnesses:** A target may join multiple times but its physical row is deleted once.
- **Smallest ID:** Never satisfies `p1.Id > p2.Id` within its group.
- **Nullable email:** Ordinary equality does not group nulls; use null-safe comparison if null duplicates must collapse.
- **Empty table:** The self-join yields no targets and nothing changes.
- **Concurrent writes:** Production cleanup may require suitable transaction isolation.
- **Any final order:** Deletion does not and need not arrange survivors.
