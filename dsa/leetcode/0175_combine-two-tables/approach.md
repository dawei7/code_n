## General

**Choose `Person` as the preserved relation**

The requested output must contain every row from `Person`, even when no
matching address exists. That requirement determines the join type and its
direction:

`Person LEFT JOIN Address`.

A left outer join preserves all rows from the table written on the left. For
each person, it searches for `Address` rows with the same `personId`. A match
combines the columns from both rows. If no match exists, the database still
emits the person's row and supplies SQL `NULL` for columns belonging to
`Address`.

An inner join would discard unmatched people and therefore fail the central
contract.

**Use the shared key explicitly through `USING`**

The optimal query writes:

`LEFT JOIN Address USING (personId)`.

`USING (personId)` is join syntax available when both input tables have a
column with that exact name. It means the equality condition:

`Person.personId = Address.personId`.

It also presents the shared join key as one coalesced column in the joined
relation rather than two separately named copies. The query does not project
that key, so the visible difference is minor here.

`Person.personId` is a primary key, ensuring at most one person row for a given
identifier. `Address.addressId` is its primary key. The local schema does not
explicitly declare `Address.personId` unique, so relationally, multiple address
rows with the same person ID would produce multiple joined output rows for that
person. The query correctly follows ordinary join semantics rather than
silently choosing one.

**Project only the required columns**

After joining, the intermediate relation includes identifiers and name and
address fields. The `SELECT` list narrows it to:

- `firstName`;
- `lastName`;
- `city`;
- `state`.

Their order exactly matches the requested result schema. Avoiding `SELECT *`
prevents extra `personId` and `addressId` columns from leaking into the result.

The columns named `city` and `state` come only from `Address`; `firstName` and
`lastName` come only from `Person`, so they are unambiguous without table
qualifiers. Qualifiers could still improve readability, but they are not
required for this schema.

**Trace the sample join**

Person one, Allen Wang, has no `Address` row with `personId = 1`. The left join
preserves Allen's person row and supplies `NULL` for `city` and `state`.

Person two, Bob Alice, matches the address row whose `personId` is two. The
joined row combines Bob's name with New York City and New York.

The address whose `personId` is three has no matching `Person` row. Because
`Address` is the non-preserved right side, that orphan address contributes no
output row. The task asks for each person, not each address.

**Why the join condition belongs in the join**

Writing the key equality in `USING` makes it part of the outer-join matching
operation. A common mistake is to use a Cartesian product or an outer join and
then put a right-table condition in `WHERE`.

A `WHERE` predicate that requires an `Address` value to be non-null can reject
the null-extended rows after the join, effectively turning the result into an
inner join. This query has no such filter, so unmatched people remain.

**NULL is a database value marker**

For an unmatched person, SQL produces `NULL`, not the string `"Null"`, an empty
string, or zero. The display table may render it as `Null`, but the underlying
result is the database null marker.

The query does not use `COALESCE`, because replacing missing locations with
custom text would violate the required output.

**Order is intentionally unspecified**

There is no `ORDER BY` clause. The Reference allows any result order, so this
is correct. Database engines may return rows in an order that happens to match
physical storage, but callers must not rely on it.

Adding an unnecessary order would introduce sorting work and promise behavior
the task does not request.

**Why the result is complete and sound**

For every `Person` row, left-join semantics emit at least one output row:
matched address data when present, or null address values otherwise. Thus no
person is omitted.

Every non-null location in the result comes from an `Address` row with equal
`personId`, so no person's name is paired with another person's address.
Projection then returns exactly the requested attributes.

## Complexity detail

Let $P$ and $A$ be the row counts in `Person` and `Address`. With a hash join,
the engine can build a hash structure for one input and scan the other in
$O(P+A)$ expected time and $O(P+A)$ worst-case working space, matching the
manifest's broad bounds.

SQL query text does not force that physical plan. With an index on the join key,
the optimizer may use indexed nested loops; without suitable indexes or hash
join support, worst-case work can differ substantially. Output size also grows
with the number of matches and can exceed $P$ if `Address.personId` repeats.

## Alternatives and edge cases

- **Explicit `ON` condition:** `LEFT JOIN Address ON Person.personId = Address.personId` is equivalent and works even when key names differ.
- **Right join with reversed tables:** Can preserve `Person`, but is less direct and less portable in style.
- **Inner join:** Incorrect because it drops people without addresses.
- **Correlated subqueries:** Could fetch each address column separately, but duplicate work and multirow semantics are awkward.
- **No matching address:** Produces SQL `NULL` for both location fields.
- **Orphan address:** Produces no row because `Address` is not the preserved side.
- **Multiple matches:** Emits one joined row per address match unless uniqueness is separately guaranteed.
- **Column projection:** Omitting identifiers is required by the output schema.
- **Any order:** No `ORDER BY` is necessary.
- **Physical complexity:** Actual runtime depends on indexes, statistics, optimizer choices, and output cardinality.
