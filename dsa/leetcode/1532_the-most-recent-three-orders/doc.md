# The Most Recent Three Orders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1532 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/the-most-recent-three-orders/) |

## Problem Description
### Goal

The `Customers` table identifies customers by ID and name. The `Orders` table records an order ID, date, customer ID, and cost, with at most one order for a given customer on any one day.

For each customer who has placed orders, return their three most recent orders. If that customer has fewer than three orders, return every one of them. The result contains the customer name and ID together with the order ID and order date; cost is not returned.

Order the result first by `customer_name` in ascending order, then by `customer_id` in ascending order when names tie, and finally by `order_date` in descending order for the same customer.

### Function Contract
**Inputs**

Let $c$ be the number of customer rows and $m$ the number of order rows.

- `Customers.customer_id`: A unique integer customer identifier.
- `Customers.name`: The customer's name.
- `Orders.order_id`: A unique integer order identifier.
- `Orders.order_date`: The order date; each customer has at most one order per date.
- `Orders.customer_id`: The customer who placed the order.
- `Orders.cost`: The order cost, which does not appear in the result.

**Return value**

Return `customer_name`, `customer_id`, `order_id`, and `order_date` for at most the three newest orders of every customer with orders, using the required name/ID/date ordering.

### Examples
**Example 1**

- Input: Winston has four orders dated June 10, July 15, July 31, and August 3 of 2020.
- Output: Winston's August 3, July 31, and July 15 orders.
- Explanation: The June 10 order is the fourth newest and is excluded.

**Example 2**

- Input: Annabelle has two orders and Marwan has one.
- Output: Both Annabelle orders and the single Marwan order.
- Explanation: A customer with fewer than three orders keeps every order.

**Example 3**

- Input: Two customers share a name but have different IDs and multiple orders.
- Output: The lower customer ID's rows appear first; each customer's dates descend within its group.
