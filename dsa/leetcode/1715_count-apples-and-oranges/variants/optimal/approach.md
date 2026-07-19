## General
**Preserve every box with a left join**

Left-join `Boxes` to `Chests` on `chest_id`. An inner join would discard boxes without a chest, losing their direct fruit. For an unmatched or `NULL` chest identifier, replace each joined chest count with zero using `COALESCE`.

**Aggregate direct and nested fruit together**

For each joined box row, add its direct apple count to the joined chest apple count, and do the same for oranges. Sum these per-box expressions across the entire join.

Each box produces exactly one joined row because a chest identifier uniquely identifies its `Chests` record. Therefore direct fruit is counted once per box. A referenced chest contributes once through every box occurrence, while an unreferenced chest creates no joined row and contributes nothing. These are exactly the required totals.

## Complexity detail
A hash join can build a lookup from the $C$ chest rows in $O(C)$ time and space, then scan and aggregate the $B$ boxes in $O(B)$ time. Total time is $O(B+C)=O(R)$ and auxiliary join space is $O(C)$.

## Alternatives and edge cases
- **Inner join:** boxes without a chest disappear, incorrectly removing their direct fruit.
- **Sum the tables independently:** adding every chest row includes unreferenced chests and fails to repeat a chest referenced by several boxes.
- **Correlated chest lookup:** searching `Chests` separately for every box can take $O(BC)$ time without an index.
- **No chest:** `NULL` must contribute zero rather than making the per-row addition `NULL`.
- **Repeated chest identifier:** include its fruit once for each referencing box row.
- **Unreferenced chest:** it contributes nothing because no box contains it.
- **Zero fruit counts:** zero remains a valid contribution and must not be confused with a missing row.
- **Output shape:** return one aggregate row with the two required column names.
