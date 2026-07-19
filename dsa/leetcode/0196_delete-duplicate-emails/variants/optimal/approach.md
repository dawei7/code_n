## General
For each email group, the survivor is defined uniquely: the row with minimum `id`. A row is therefore deletable exactly when another row has the same email and a smaller id.

The native MySQL form expresses that predicate with a multi-table self-join deletion. Alias one copy as the deletion target and one as a possible keeper; join on equal email and require `duplicate.id > keeper.id`. The target alias is the only table named after `DELETE`, so matching keeper rows are never deleted merely because they participate in the join.

For `(1,a), (2,b), (3,a), (4,a)`, rows 3 and 4 each match row 1 and are deleted. Row 1 has no same-email row with a smaller id, and row 2 has no duplicate at all, so both survive. It does not matter that row 4 may match multiple smaller rows; deletion remains idempotent for that target row.

The local SQLite adapter uses a different mutation-safe shape because SQLite does not support MySQL's joined-delete syntax: compute minimum ids per email in a nested relation, then delete ids not in that keeper set. The extra nesting also avoids engines' restrictions on reading directly from the table currently being modified.

Every deleted row matches a same-email row with smaller id, so it cannot be the required representative. Conversely, every nonminimum row has the group's minimum-id row as a smaller same-email match and is deleted. The minimum row has no smaller match and survives, while a unique-email row also has no match. Hence exactly the minimum-id row remains for each distinct email.

## Complexity detail
A sort/group or indexed self-join plan generally costs $O(n \log n)$ logical work and up to $O(n)$ temporary or index state. An index on `(email, id)` can make duplicate and minimum lookup substantially more efficient. Mutation cost and exact planning are database-dependent.

## Alternatives and edge cases
- Grouping by email to compute `MIN(id)` and deleting every other id is explicit and portable with dialect-specific mutation wrapping.
- `ROW_NUMBER() OVER (PARTITION BY email ORDER BY id)` clearly labels duplicates, but deleting through the ranked result requires dialect-specific CTE support.
- Deleting an arbitrary row from each duplicate group violates the minimum-id requirement.
- Already-distinct data is unchanged. Groups of any size retain one row, independent of physical row order.
- The schema's id uniqueness ensures each group has one unambiguous minimum.
