# Product Sales Analysis III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1070 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/product-sales-analysis-iii/) |

## Problem Description

### Goal

The `Sales` table stores product sales by `sale_id`, `product_id`, year, quantity, and per-unit price. Its composite primary key is `(sale_id, year)`. A product may have several sale entries in the same year.

For every product, identify the earliest year in which it appears in `Sales`, then return all of that product's sale entries from that year. Report `product_id`, the year under the name `first_year`, `quantity`, and `price`. Return the rows in any order.

### Function Contract

**Inputs**

- `Sales(sale_id, product_id, year, quantity, price)`: $R$ sale rows with composite key `(sale_id, year)`.

**Return value**

- Columns `product_id`, `first_year`, `quantity`, and `price`.
- Every sale row whose `year` equals the minimum year for its `product_id`, including multiple rows in that first year.
- Result order is unrestricted; the local reference orders by product and sale key for deterministic validation.

### Examples

**Example 1**

`Sales`

| sale_id | product_id | year | quantity | price |
|---:|---:|---:|---:|---:|
| 1 | 100 | 2008 | 10 | 5000 |
| 2 | 100 | 2009 | 12 | 5000 |
| 7 | 200 | 2011 | 15 | 9000 |

Output:

| product_id | first_year | quantity | price |
|---:|---:|---:|---:|
| 100 | 2008 | 10 | 5000 |
| 200 | 2011 | 15 | 9000 |

The 2009 sale for product 100 is omitted because that product already appeared in 2008.

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Find one first year per product:** Group `Sales` by `product_id` and compute `MIN(year)`. This relation contains the earliest year for every product represented in the table.

**Join the minimum back to sale rows:** Match the grouped relation to `Sales` on both `product_id` and `year`. Matching only the product would retain later years; matching both conditions selects exactly the required first-year entries.

**Preserve ties rather than rank one row:** The join returns every sale sharing the minimum year. Project the sale's year as `first_year` together with its quantity and price. Ordering by product and the composite sale key is included solely for deterministic fixtures.

Every joined row has a year equal to its product's grouped minimum, so it belongs in the result. Conversely, every sale in a product's first year satisfies both join conditions and is retained, including any additional row tied on that year.

#### Complexity detail

A sort-based grouped minimum over $R$ rows and deterministic result ordering take $O(R\log R)$ time and up to $O(R)$ execution space. A hash aggregate and hash join may run in expected $O(R)$ time before output ordering; indexes can produce other physical plans.

#### Alternatives and edge cases

- **Correlated minimum:** Compare each sale's year with a subquery computing its product's minimum. It is concise but can rescan all $R$ rows for each sale, taking $O(R^2)$ time without an index.
- **Dense rank:** `DENSE_RANK()` partitioned by product and ordered by year preserves all first-year ties, but may sort the full input and requires an outer filter.
- **Row number:** Keeping only `ROW_NUMBER() = 1` is incorrect when a product has several sales in its earliest year.
- **Single sale for a product:** It is necessarily a first-year row.
- **Several first-year sales:** Every tied row is returned with its own quantity and price.
- **Later price change:** Later-year rows are omitted even if their price or quantity differs.
- **Composite sale key:** Reusing a `sale_id` in a different year does not merge the rows.

</details>
