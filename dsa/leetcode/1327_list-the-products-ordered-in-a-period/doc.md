# List the Products Ordered in a Period

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1327 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/list-the-products-ordered-in-a-period/) |

## Problem Description
### Goal
The `Products` table identifies each product and stores its name and category. The `Orders` table records a product, an order date, and the number of units ordered; duplicate order rows may occur.

Find products whose orders dated in February 2020 total at least 100 units. Return each qualifying `product_name` together with its February total under the column name `unit`. Orders before `2020-02-01` or on or after `2020-03-01` do not contribute.

The result may be returned in any order. Products without February orders and products whose February total is below 100 must be omitted.

### Function Contract
**Inputs**

- `Products(product_id, product_name, product_category)`: one row per product, keyed by `product_id`.
- `Orders(product_id, order_date, unit)`: order rows referencing `Products`; duplicate rows are allowed.

Let $p$ be the number of product rows, $o$ the number of order rows, and $k$ the number of qualifying products.

**Return value**

The `product_name` and summed February 2020 `unit` for every product with a total of at least 100 units.

### Examples
**Example 1**

- Input: `Leetcode Solutions` has February orders of 60 and 70 units
- Output: `("Leetcode Solutions", 130)`

**Example 2**

- Input: `Leetcode Kit` has February orders of 50 and 50 units plus a March order
- Output: `("Leetcode Kit", 100)`
- Explanation: The March units are excluded, and equality with the threshold qualifies.

**Example 3**

- Input: a product has 80 February units and 30 January units
- Output: no row for that product
- Explanation: Units outside February cannot raise its qualifying total.

### Required Complexity
- **Time:** $O(p+o+k\log k)$
- **Space:** $O(p+k)$

<details>
<summary>Approach</summary>

#### General

**Filter the date range before aggregation**

Join `Orders` to `Products` by `product_id`, retaining order dates greater than or equal to `2020-02-01` and strictly less than `2020-03-01`. The half-open range includes all dates in leap-year February without depending on day extraction or string formatting.

Group the retained rows by the product identifier and name, sum `unit`, and use `HAVING SUM(unit) >= 100`. Duplicate order rows remain separate inputs to the sum, as required by the table contract. Select the name and aggregate with alias `unit`; a final name ordering makes local results deterministic although the source permits any order.

#### Complexity detail

In the hash-join and hash-aggregation model, reading the two relations costs $O(p+o)$ and stores product and aggregate state in $O(p+k)$ space. Deterministically ordering the $k$ result rows adds $O(k\log k)$ time.

#### Alternatives and edge cases

- **Correlated sum per product:** Summing matching February orders separately for each product is correct but may rescan all $o$ order rows for each of $p$ products.
- **Month and year extraction:** Testing extracted components works but can prevent index range use; the half-open date interval is clearer.
- **Exactly 100 units:** Include the product because the threshold is at least 100.
- **Duplicate orders:** Count every row; the table explicitly permits duplicates.
- **Boundary dates:** Include `2020-02-01` and `2020-02-29`, but exclude `2020-01-31` and `2020-03-01`.
- **No February orders:** Such a product has no qualifying group and is absent.

</details>
