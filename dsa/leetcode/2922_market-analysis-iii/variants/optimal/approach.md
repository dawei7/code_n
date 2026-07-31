## General

**Filter at the order level, then count distinct items.** Join each order to
its seller and item so that `item_brand` can be compared with
`favorite_brand`. Discard matching-brand rows before aggregation. Group the
remaining rows by `seller_id` and apply `COUNT(DISTINCT item_id)`; the
distinct modifier is essential because multiple orders for one item still
represent one unique item.

Store those per-seller counts in `seller_counts`. Its scalar maximum is the
global qualifying-item count to beat. Selecting every row equal to that
maximum preserves all ties, while sellers without any mismatched-brand order
remain absent rather than appearing with a zero count. Finally,
`ORDER BY seller_id` makes the required ascending output deterministic.

Every retained order is associated with exactly its referenced seller and
item, and the filter is exactly the required brand inequality. Thus each group
contains precisely the qualifying orders for one seller, and its distinct
count is correct. Comparing every group with the global maximum returns all
and only top sellers.

## Complexity detail

Let $U$, $I$, and $O$ be the input table row counts, and $W$ the number of
winning output rows. With hash joins and hash-based distinct aggregation, the
expected work is $O(U+I+O)$ before output ordering. Sorting the winners costs
$O(W\log W)$, for $O(U+I+O+W\log W)$ expected time. Join indexes or different
physical plans can change constants. Hash tables, distinct-item sets, and
grouped counts use $O(U+I+O)$ space in the worst case.

## Alternatives and edge cases

- **Correlated count per seller:** A distinct-count subquery for every user is correct, but can rescan `Orders` and `Items` once per seller instead of aggregating the joined rows once.
- **Window maximum:** A window over grouped counts can mark maximum rows, but the scalar maximum is simpler and avoids another exposed ranking column.
- **Count orders instead of items:** Plain `COUNT(*)` overcounts repeated orders for the same item; the contract requires unique item IDs.
- **Favorite-brand sales:** These rows must be removed before counting, even when the item is highly popular.
- **Maximum-count ties:** Every seller sharing the maximum belongs in the result.
- **No qualifying orders:** The grouped CTE is empty, its maximum is null, and the result correctly contains no rows.
- **Output order:** SQL does not guarantee row order without the explicit final `ORDER BY seller_id`.

