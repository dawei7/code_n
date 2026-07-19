## General
The inclusion requirement determines the join direction: every row from `Person` must survive even when no matching row exists in `Address`. Make `Person` the left relation and apply a `LEFT JOIN` to `Address` on the shared `personId`.

Conceptually, the query is:

```sql
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a
  ON a.personId = p.personId;
```

For a matched person, the joined address supplies `city` and `state`. For an unmatched person, outer-join semantics synthesize `NULL` for those right-side columns rather than dropping the person. Address rows with no corresponding person do not appear because the result is driven by `Person`.

The join condition belongs in `ON`. Moving a right-table filter into `WHERE` can accidentally reject the null-extended rows and turn the intended outer join into inner-join behavior.

A left outer join emits at least one result row for every row in its left relation. Here that guarantees every person appears. When `a.personId = p.personId` has a match, the selected address fields come from that related row; when no match exists, SQL supplies nulls for exactly those fields. Thus every output row has the required person data and precisely the available address data, with no unrelated address able to create a person row.

## Complexity detail
With a hash join or suitable index, the database can process `P` person rows and `A` address rows in $O(P + A)$ logical work, plus result production. A hash join may use $O(A)$ auxiliary space; an indexed nested-loop plan has different costs. SQL complexity depends on indexes, statistics, and the chosen execution plan, so the notation describes the intended efficient plan rather than a guaranteed physical implementation.

## Alternatives and edge cases
- An `INNER JOIN` removes people without addresses and violates the central requirement.
- A `RIGHT JOIN` can express the same relationship after reversing table roles, but it is less direct and is unsupported by some engines.
- Separate correlated subqueries for city and state repeat the same lookup and can lead to inconsistent or inefficient plans.
- An empty `Address` table still yields every person with null location fields.
- If the schema allowed multiple addresses per person, the join would return multiple rows for that person; the stated schema/contract determines whether that multiplicity is possible.
