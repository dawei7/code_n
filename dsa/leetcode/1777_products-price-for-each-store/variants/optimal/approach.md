## General

**Pivot store rows into store columns**

`Products` is in long form: each row describes one product at one store. The requested result is wide form: one row per `product_id` with separate `store1`, `store2`, and `store3` price columns.

The exact SQL query uses conditional aggregation. It groups all rows of one product, conditionally exposes the price for each store, and aggregates that exposed value into its output column.

**Create one conditional value per store**

For store one, the expression is:

`IF(store = 'store1', price, NULL)`.

On the product's `store1` row, it returns that row's price. On rows for other stores, it returns null. The query repeats the same structure for `store2` and `store3`.

Using null rather than zero matters. Zero would assert a price of zero for nonmatching rows and could make a missing store look present. Null represents the absence of a matching store row.

**Why SUM acts as a pivot selector**

Each conditional expression is wrapped in `SUM`. The primary key `(product_id, store)` guarantees at most one row for a particular product-store pair.

Within one product group, the conditional values for a store are therefore either:

- one real price plus nulls from other store rows, or
- only nulls when that product is unavailable at the store.

SQL aggregate `SUM` ignores null inputs. In the first case, the sum equals the single real price. In the second case, summing an all-null set returns null, exactly the desired missing-store output.

Because uniqueness guarantees only one price, `MAX` or `MIN` would behave equivalently. `SUM` is correct here as a selector, not because multiple store prices need addition.

**Group by the selected product identifier**

`GROUP BY 1` uses the ordinal position of the first `SELECT` expression, which is `product_id`.

All rows sharing one product identifier enter the same group, yielding one output row per product. Rows of different products remain separate even when their store or price values match.

Writing `GROUP BY product_id` would be more explicit but would produce the same result for this select list.

**Trace the sample product**

Product zero has one row for each store. In its group:

- the store-one conditional exposes 95 only,
- the store-two conditional exposes 100 only,
- the store-three conditional exposes 105 only.

The sums become 95, 100, and 105.

Product one has no store-two row. Its store-two conditional is null on both existing group rows, so `SUM` returns null. Store one and store three return 70 and 80.

**Why no join is necessary**

All store observations are already in one table. A self-join per store could pivot the data, but it would require carefully preserving products missing a store and would be more verbose.

Conditional aggregation performs the transformation in one grouped scan and naturally retains any product that has at least one row.

**Any-order output**

The problem accepts any row order, so no `ORDER BY` is included. The database may return product groups in an implementation-dependent order without affecting correctness.

Column order is fixed by the `SELECT` list: product identifier, then stores one, two, and three.

**Why the result is correct**

For each product, grouping collects exactly its available store rows. Each conditional aggregate returns the unique price for its named store when present and null when absent.

Thus every product produces one row containing precisely its per-store prices. Primary-key uniqueness prevents accidental addition of multiple prices within one cell.

## Complexity detail

Let $R$ be the number of input rows and $P$ the number of distinct products. With hash aggregation, the database scans each row once, evaluates three constant-time conditions, and updates one product group, for expected $O(R)$ time.

The aggregation state and output hold one fixed-width record per product, using $O(P)$ space, matching the manifest. A sort-based grouping plan may use $O(R\log R)$ time physically if no helpful ordering or hash plan is chosen; SQL does not force one execution strategy.

The three store categories are fixed, so per-row and per-group column work is constant.

## Alternatives and edge cases

- **MAX with CASE:** `MAX(CASE WHEN store = 'store1' THEN price END)` is the conventional portable equivalent.
- **Self-join per store:** It can pivot columns but requires outer joins to preserve products missing a store.
- **Native PIVOT operator:** Some database systems support it, but MySQL conditional aggregation is broadly applicable.
- **Missing store:** All conditional inputs are null and `SUM` returns null.
- **All stores present:** Each output store column receives its unique price.
- **Only one store present:** The product row remains, with two null columns.
- **Primary-key uniqueness:** It makes sum equal selection rather than addition of multiple observations.
- **Price zero:** If allowed, it would remain distinguishable from null; the query does not substitute zero for missing.
- **Ordinal grouping:** `GROUP BY 1` depends on `product_id` remaining the first selected expression.
- **Any result order:** No ordering clause is required.
- **Different products at same store:** Product grouping keeps their prices separate.
- **Null aggregate semantics:** `SUM` ignores nulls but returns null when there is no non-null value.
- **Fixed enum domain:** Exactly three conditional columns cover every possible store.
- **No input mutation:** The query reads and reshapes rows without updating `Products`.
