## General
**Preserve every student with a left join.** Join `Students` to `Departments` on the recorded department ID. A valid reference produces the matching department row, while an invalid reference still preserves the student but supplies `NULL` for every column from the department side.

**Keep only unmatched rows.** Filter for `d.id IS NULL`. Because `Departments.id` is a primary key and therefore cannot itself be null, this condition distinguishes an absent join partner without confusing it with stored data. Select the student-side `id` and `name`; ordering by student ID is optional for the problem contract but makes local results deterministic.

The left join examines every student. A row survives exactly when no department has the referenced ID, which is precisely the requested invalid-department condition.

## Complexity detail
With an index or hash table on the department primary key, constructing or reading the lookup structure costs $O(D)$ and checking all students costs $O(S)$, for $O(N)$ time and $O(D)$ lookup space in the general model. Database indexes may already provide that lookup storage.

## Alternatives and edge cases
- **`NOT EXISTS` anti-subquery:** A correlated existence test is semantically equivalent and often optimized to the same plan, but an unindexed nested scan can cost $O(DS)$.
- **`NOT IN` subquery:** This is concise, but nullable values in the subquery can make SQL's three-valued logic reject every row; the primary key is non-null here, though the anti-join remains clearer.
- **No invalid students:** The query correctly returns an empty result.
- **No departments:** Every student is unmatched and must be returned.
- **Repeated names:** Student identity comes from `id`; equal names remain separate output rows.
