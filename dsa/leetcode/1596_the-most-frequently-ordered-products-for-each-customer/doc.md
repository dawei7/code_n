# The Most Frequently Ordered Products for Each Customer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1596 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer/) |

## Problem Description
### Goal
The database contains `Customers`, `Orders`, and `Products`. `Customers` identifies each customer and stores a name. Every row in `Orders` records one order, including its date, customer, and product. `Products` maps each product identifier to its name and price.

For every customer who has placed at least one order, find the product or products appearing most often in that customer's order rows. If several products share the same maximum frequency for one customer, include all of them. Return each qualifying `customer_id` and `product_id` together with the matching `product_name`; customers without orders do not produce a row.

### Function Contract
**Inputs**

- `Customers(customer_id, name)`, where `customer_id` identifies a customer.
- `Orders(order_id, order_date, customer_id, product_id)`, with one row per order.
- `Products(product_id, product_name, price)`, where `product_id` identifies a product.

**Return value**

Return a relation with columns `customer_id`, `product_id`, and `product_name` containing every product tied for the greatest order count within its customer. Row order is not part of the contract.

### Examples
**Example 1**

- Input: Alice orders the mouse three times and the keyboard once; Bob orders the keyboard, mouse, and screen once each.
- Output: Alice's mouse plus all three tied products for Bob.

**Example 2**

- Input: One customer orders two different products twice each.
- Output: Two rows for that customer, one for each tied product.

**Example 3**

- Input: A customer exists in `Customers` but has no row in `Orders`.
- Output: No row for that customer.
