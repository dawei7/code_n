# Product Sales Analysis II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1069 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/product-sales-analysis-ii/) |

## Problem Description

### Goal

The `Sales` table records product sales by `sale_id`, `product_id`, year, quantity, and per-unit price. Its composite primary key is `(sale_id, year)`, so the same product may own several distinct sale rows across years or sale identifiers.

For every product identifier that occurs in `Sales`, report the total quantity sold across all of that product's sale rows. Return `product_id` and the summed quantity under the name `total_quantity`. Result rows may be returned in any order.

### Function Contract

**Inputs**

- `Sales(sale_id, product_id, year, quantity, price)`: $R$ sale rows with composite key `(sale_id, year)`.
- `Product(product_id, product_name)`: product metadata supplied by the schema but not needed for the requested identifiers and totals.

**Return value**

- Columns `product_id` and `total_quantity`.
- One row for every distinct `product_id` occurring in `Sales`, where `total_quantity` is the sum of its `quantity` values.
- Result order is unrestricted; the local reference orders by `product_id` for deterministic validation.

### Examples

**Example 1**

`Sales`

| sale_id | product_id | year | quantity | price |
|---:|---:|---:|---:|---:|
| 1 | 100 | 2008 | 10 | 5000 |
| 2 | 100 | 2009 | 12 | 5000 |
| 7 | 200 | 2011 | 15 | 9000 |

Output:

| product_id | total_quantity |
|---:|---:|
| 100 | 22 |
| 200 | 15 |

The two rows for product 100 contribute `10 + 12`, while product 200 has one quantity of 15.

### Required Complexity

- **Time:** $O(R\log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Form one group per product:** Group all `Sales` rows by `product_id`. Rows for different products remain separate even if they share a year, price, quantity, or sale identifier component.

**Aggregate the sold units:** Apply `SUM(quantity)` to each group and alias the result as `total_quantity`. The output grain is now one row per product represented in the sales data.

**Avoid an unnecessary join:** The requested columns and aggregate both come from `Sales`. Joining `Product` would add work without contributing a name or another requested field. An ascending product order is included only to stabilize local fixtures.

Every output total sums exactly the rows in its product group. Conversely, every sale belongs to one `product_id` group, so every sold product appears once and every quantity contributes once to the correct total.

#### Complexity detail

A sort-based grouping plan processes $R$ rows in $O(R\log R)$ time and may use $O(R)$ execution space. Hash aggregation can run in expected $O(R)$ time with space proportional to the number of distinct products. Indexes and the database optimizer may select a different physical plan.

#### Alternatives and edge cases

- **Correlated sum:** Compute a scalar sum for each source row and then deduplicate products. It is correct but can rescan all $R$ sales for every row, taking $O(R^2)$ time.
- **Join to Product:** It is unnecessary because neither `product_name` nor any other product-table column is requested.
- **Window sum plus distinct:** A partitioned `SUM` followed by deduplication works but retains row-level data longer than grouped aggregation.
- **Single sale:** Its quantity is the product's total.
- **Several years:** Quantities are summed across all years because `year` is not a grouping column.
- **Same sale identifier in different years:** The composite primary key permits both rows, and both quantities contribute.
- **Product without sales:** It has no `Sales` group and does not appear.
- **Price:** Per-unit price does not affect the requested quantity total.

</details>
