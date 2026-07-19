## General
**Filter the date range before aggregation**

Join `Orders` to `Products` by `product_id`, retaining order dates greater than or equal to `2020-02-01` and strictly less than `2020-03-01`. The half-open range includes all dates in leap-year February without depending on day extraction or string formatting.

Group the retained rows by the product identifier and name, sum `unit`, and use `HAVING SUM(unit) >= 100`. Duplicate order rows remain separate inputs to the sum, as required by the table contract. Select the name and aggregate with alias `unit`; a final name ordering makes local results deterministic although the source permits any order.

## Complexity detail
In the hash-join and hash-aggregation model, reading the two relations costs $O(p+o)$ and stores product and aggregate state in $O(p+k)$ space. Deterministically ordering the $k$ result rows adds $O(k\log k)$ time.

## Alternatives and edge cases
- **Correlated sum per product:** Summing matching February orders separately for each product is correct but may rescan all $o$ order rows for each of $p$ products.
- **Month and year extraction:** Testing extracted components works but can prevent index range use; the half-open date interval is clearer.
- **Exactly 100 units:** Include the product because the threshold is at least 100.
- **Duplicate orders:** Count every row; the table explicitly permits duplicates.
- **Boundary dates:** Include `2020-02-01` and `2020-02-29`, but exclude `2020-01-31` and `2020-03-01`.
- **No February orders:** Such a product has no qualifying group and is absent.
