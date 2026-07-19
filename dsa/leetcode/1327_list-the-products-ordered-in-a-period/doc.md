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
