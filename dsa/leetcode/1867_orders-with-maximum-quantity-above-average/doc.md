# Orders With Maximum Quantity Above Average

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/orders-with-maximum-quantity-above-average/) |
| Frontend ID | 1867 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |

## Problem Description

### Goal

The `OrdersDetails` table stores the products included in customer orders. An order may contain several products, and each row gives one product's `quantity` within its `order_id`. The pair `(order_id, product_id)` uniquely identifies a row.

For every order, consider both its average product quantity and its largest product quantity. Return the identifiers of the orders whose largest quantity is strictly greater than the average quantity of every order in the table. Equivalently, an order qualifies only when its maximum exceeds the greatest of all per-order averages. The result may be returned in any order.

### Function Contract

**Inputs**

- `OrdersDetails(order_id, product_id, quantity)`: one row for each product appearing in an order. `(order_id, product_id)` is unique, and every `quantity` is positive.
- Let $R$ be the number of rows and $G$ the number of distinct orders.

**Return value**

- Return one column named `order_id`.
- Include an order exactly when its maximum `quantity` is strictly greater than every order's average `quantity`.
- Do not include equality, and do not return duplicate order identifiers.
- Result order is unrestricted.

### Examples

**Example 1**

- Input: order `1` has quantities `[12,10,15]`, order `2` has `[8,4,6,4]`, order `3` has `[5,18,20]`, order `4` has `[2,8]`, and order `5` has `[9,9]`
- Output: `[[1],[3]]`

The largest per-order average is order `3`'s $43/3$. The maxima of orders `1` and `3`, respectively $15$ and $20$, exceed that threshold.

**Example 2**

- Input: order `1` has quantities `[4,4]` and order `2` has `[1,7]`
- Output: `[[2]]`

Both averages are $4$, while only order `2` has a maximum above $4$.

**Example 3**

- Input: order `1` has `[9]` and order `2` has `[9,9]`
- Output: `[]`

The greatest average is $9$, and the comparison is strict, so a maximum of $9$ does not qualify.
