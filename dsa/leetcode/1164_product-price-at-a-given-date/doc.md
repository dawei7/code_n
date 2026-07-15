# Product Price at a Given Date

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1164 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/product-price-at-a-given-date/) |

## Problem Description

### Goal

The `Products` table records changes to product prices. Each row says that one product's price became `new_price` on `change_date`, and the combination `(product_id, change_date)` is unique. Before its first recorded change, every product has an initial price of `10`.

Find the price of every product on `2019-08-16`. For a product with one or more changes on or before that date, use the price from its latest such change, including a change made exactly on the target date. If all of a product's changes occur later, report its initial price. The result may be returned in any order.

### Function Contract

**Input table**

- `Products(product_id, new_price, change_date)`: Each row records a price change; `(product_id, change_date)` is the primary key.
- Let $r$ be the number of rows in `Products`.

**Return value**

A relation containing one row per distinct product with:

- `product_id`: The product identifier.
- `price`: Its effective price on `2019-08-16`.

### Examples

**Example 1**

`Products`

| product_id | new_price | change_date |
|---:|---:|---|
| 1 | 20 | 2019-08-14 |
| 2 | 50 | 2019-08-14 |
| 1 | 30 | 2019-08-15 |
| 1 | 35 | 2019-08-16 |
| 2 | 65 | 2019-08-17 |
| 3 | 20 | 2019-08-18 |

Output:

| product_id | price |
|---:|---:|
| 1 | 35 |
| 2 | 50 |
| 3 | 10 |

### Required Complexity

- **Time:** $O(r \log r)$
- **Space:** $O(r)$

<details>
<summary>Approach</summary>

#### General

**Preserve the complete product set.** Start with the distinct `product_id` values from all rows. Filtering the table to dates on or before `2019-08-16` too early would erase products whose first change is later, even though those products must appear with price `10`.

**Locate the effective change date.** Among eligible rows, group by `product_id` and take `MAX(change_date)`. Because `(product_id, change_date)` is the primary key, this date identifies exactly one price-change row for each product that had changed by the target date.

**Restore prices and defaults.** Left join every product to its latest eligible date, then join that pair back to `Products` to obtain `new_price`. When no eligible date exists, the joins yield null, so `COALESCE(new_price, 10)` supplies the initial price. A change on `2019-08-16` is eligible because the comparison is inclusive. An `ORDER BY product_id` may stabilize local fixtures even though the source accepts any output order.

#### Complexity detail

Grouping and joining $r$ rows take $O(r \log r)$ time under a comparison-based plan; indexed or hash-based execution may be faster in practice. The distinct product set, grouped latest dates, and join state require $O(r)$ working space in the worst case.

#### Alternatives and edge cases

- **Window ranking:** Rank eligible changes per product by `change_date` descending and retain rank one; this is equally expressive but still needs a separate complete product set for unchanged products.
- **Correlated latest-price lookup:** A subquery ordered by date for every product is concise, but without a suitable index it can rescan `Products` for each product and become quadratic.
- **Union changed and unchanged products:** Two branches can return latest prices and default prices separately, but the exclusion logic is easier to get wrong than a left join.
- **Only future changes:** The product remains present and receives the initial price `10`.
- **Change on the target date:** The `change_date <= '2019-08-16'` condition includes it.
- **Several earlier changes:** Only the row at the maximum eligible date determines the reported price.

</details>
