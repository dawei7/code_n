## General

**Preserve every person with a left outer join**

The competitive query begins with `Person` and uses:

`LEFT JOIN Address`.

That ordering encodes the business rule. Every row in the left table survives
whether or not a compatible row exists on the right. An unmatched right side
is represented with `NULL` values.

The explicit match condition is:

`Person.PersonId = Address.PersonId`.

Only address rows belonging to the same identifier may be combined with a
person.

**Distinguish outer join from inner join**

An ordinary `JOIN`, usually meaning inner join, emits only matched pairs. In the
sample, Allen Wang has no address, so an inner join would remove Allen entirely.

The left join instead creates a null-extended joined row. Selecting `City` and
`State` from that nonexistent right row yields database `NULL`, exactly as the
contract requests.

An address for `PersonId = 3` has no matching person. It is not returned,
because the task is driven by persons and the right side is not preserved.

**Project names and location in the requested order**

The `SELECT` clause returns `FirstName`, `LastName`, `City`, and `State`.
MySQL identifiers are commonly case-insensitive in this context, so the
capitalization corresponds to the locally declared `firstName`, `lastName`,
`city`, and `state` columns.

Selecting named columns prevents `PersonId` and `AddressId` from appearing in
the result. The order of expressions in `SELECT` determines the order of
result columns, independently of table storage order.

Each projected name is unique across the two table schemas. If both tables
contained a column with the same projected name, it would need a table
qualifier to avoid ambiguity.

**Trace the two sample people**

For person ID one, the join probe finds no address. The engine emits Allen,
Wang, `NULL`, `NULL`.

For person ID two, it finds the address row with New York City and New York,
so those values accompany Bob and Alice.

The unmatched California address belongs to ID three and is ignored. This
shows why the preserved side must be `Person`; reversing the tables without
changing the join direction would answer a different question.

**Understand duplicate match semantics**

`Person.PersonId` is a primary key and therefore unique. `Address.AddressId`
is also a primary key, but the provided schema text does not explicitly say
that `Address.PersonId` is unique.

If several address rows share one person ID, a relational join emits one result
row for each match. The query does not arbitrarily choose an address or merge
them. Under the expected data, this produces the intended row set; under
duplicate right-side matches, the multiplicity follows standard SQL behavior.

**Keep filtering out of `WHERE`**

The query places identifier equality in `ON`, where it controls which right
rows match each left row. It has no `WHERE` condition.

If one wrote `WHERE Person.PersonId = Address.PersonId` after an insufficient
outer join, null-extended rows would fail the comparison because SQL's
three-valued logic treats comparison with `NULL` as unknown. The apparent outer
join would then behave like an inner join. This source avoids that trap.

**Return actual nulls and unspecified order**

The query does not replace missing fields with a display string. SQL `NULL` is
the required marker for absent city and state.

It also omits `ORDER BY`, which is correct because any row order is accepted.
Without `ORDER BY`, SQL does not promise a stable or particular order even if
one run looks sorted.

**Why each output association is valid**

For every person, left-join semantics either pair all matching addresses or
create one null-extended row. Therefore every person is represented.

The `ON` equality ensures every non-null address belongs to the person shown.
Projection returns exactly the four requested columns. Together, those facts
prove completeness and prevent cross-person address assignment.

**Source comment syntax**

The leading `#` lines are accepted as comments by MySQL. In SQL dialects that
do not support hash comments, they must be removed or changed to `--` comments;
the actual `SELECT` statement itself is standard left-join syntax.

## Complexity detail

Let $P$ and $A$ be input row counts. A hash-join execution can process both
tables in expected $O(P+A)$ time with linear working memory, aligning with the
manifest.

The SQL statement specifies relational results, not a fixed algorithm. An
optimizer may choose indexed nested loops, a hash join, or another plan based
on available indexes and statistics. Output cardinality must also be counted;
repeated address matches can create more than $P$ result rows. The manifest is
a plausible plan-level summary rather than a universal engine guarantee.

## Alternatives and edge cases

- **`USING (PersonId)`:** Shorter equivalent syntax because both tables use the same join-key name.
- **Pandas left merge:** `merge(..., how="left", on="personId")` expresses the same relational operation for DataFrames.
- **Inner join:** Loses people with no address and is incorrect.
- **Right join:** Could work with tables reversed but makes the preservation intent less obvious.
- **Unmatched person:** Produces one row with null location fields.
- **Unmatched address:** Is excluded from the person-centered result.
- **Duplicate address matches:** Produce multiple result rows under ordinary join semantics.
- **NULL filtering:** A right-table `WHERE` predicate can accidentally discard unmatched people.
- **Any row order:** No sorting clause should be inferred.
- **Dialect comments:** Hash-prefixed comments are MySQL-specific even though the query body is broadly portable.
