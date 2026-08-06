## General

**Use the source guarantee to count directly from `Friends`.** Every catalog activity has at least one participating friend, so grouping `Friends` by `activity` produces exactly one count for every activity that can affect the answer. Joining `Activities` back into this calculation cannot add a zero-participant activity and is unnecessary for the requested output.

**Separate counting from the global comparison.** The `activity_counts` CTE stores one row per activity with `COUNT(*)` friend rows. The outer query compares each count with the minimum and maximum over that compact relation. Both comparisons are strict, so every tie at the least-popular or most-popular count is excluded.

The grouping assigns each friend to exactly one named activity and therefore computes every participant count correctly. The two scalar aggregates are taken over all and only those counts. An activity survives precisely when its count is greater than the global minimum and less than the global maximum, which is the required neither-extreme condition.

## Complexity detail

Let $F$ be the number of friend rows, $A$ the number of activities, and $N=F+A$. Grouping the friend rows costs $O(F \log F)$ in the general sort/group model, while the constant number of scans over the $A$ grouped rows costs $O(A)$. This is within $O(N \log N)$ time. The grouped relation stores $A$ counts, giving $O(A)$ auxiliary space. Hash aggregation can make the expected grouping time linear.

## Alternatives and edge cases

- **Catalog left join:** Beginning with `Activities` and counting matched friend IDs is correct, but the guaranteed positive participation makes the join and null-preservation work unnecessary.
- **Window extrema:** `MIN` and `MAX` window functions over the grouped counts avoid scalar subqueries and have the same asymptotic cost, but require another projection layer before filtering.
- **Correlated count per activity:** Recounting `Friends` independently for every catalog row is correct but can take $O(AF)$ time without a usable index.
- **All counts equal:** The minimum equals the maximum, so no activity satisfies both strict inequalities.
- **One or two popularity levels:** Every activity lies at an extreme, leaving an empty result.
- **Ties at either extreme:** All activities sharing the minimum or maximum are excluded; ties at an intermediate count are all returned.
- **Repeated friend names:** Participant counts come from friend rows, not distinct names, so different IDs with the same name still count separately.
- **Result order:** The contract allows any order, so no `ORDER BY` is required.
