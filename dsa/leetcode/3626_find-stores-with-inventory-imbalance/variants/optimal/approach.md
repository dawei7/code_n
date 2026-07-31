## General

**Rank both price extremes in one inventory pass.** For every `store_id`, assign one row number in descending price order and another in ascending price order. The first ranking identifies the most expensive product; the second identifies the cheapest. `inventory_id` is a deterministic secondary key without changing which price is extreme.

**Enforce the distinct-product threshold separately.** Aggregate `inventory` by store and compute `COUNT(DISTINCT product_name)`. Joining that result to `stores` prevents a store with fewer than three different products from entering the answer, even if multiple inventory rows exist.

Join each store to rank 1 from both price directions. The strict predicate on the two quantities implements the imbalance definition. Dividing the cheapest quantity by the most-expensive quantity and rounding to two decimal places produces the requested ratio. Finally, descending ratio order puts the strongest imbalance first, and ascending store name resolves equal ratios.

## Complexity detail

Let $R$ be the number of inventory rows and $S$ the number of stores. The two window rankings sort inventory partitions and take $O(R\log R)$ time in the general case. Distinct-product aggregation is bounded by the same order, and sorting at most $S$ result rows takes $O(S\log S)$ time. Total time is $O(R\log R+S\log S)$. Window and aggregate state use $O(R+S)$ auxiliary space.

The benchmark sets its workload size $N$ to the store count and gives every store three products, so the inventory relation has $3N$ rows. The ranked query processes and sorts that relation once in $O(N\log N)$ time, while a correct formulation that uses correlated scans to rediscover each store's price extremes takes $O(N^2)$ time.

## Alternatives and edge cases

- **Correlated minimum and maximum subqueries:** They can express the result compactly, but without suitable indexes they repeatedly scan `inventory` and scale quadratically.
- **Conditional aggregation after joining extrema:** This is valid when ties and row identity are handled deliberately, but window ranks make the selected product row explicit.
- **Fewer than three products:** Exclude the store even when its two products otherwise satisfy the quantity comparison.
- **Strict quantity comparison:** Equal extreme quantities do not constitute an imbalance.
- **Middle-priced products:** Their quantities do not affect the comparison; they matter only to the distinct-product threshold.
- **Ratio ordering:** Sort by the numeric rounded ratio descending, then by `store_name` ascending.
