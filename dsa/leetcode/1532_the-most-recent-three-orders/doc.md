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

### Required Complexity

- **Time:** $O(m\log m + c)$
- **Space:** $O(m)$

<details>
<summary>Approach</summary>

#### General

**Rank orders independently within each customer**

Use `ROW_NUMBER()` partitioned by `customer_id` and ordered by `order_date DESC`. Because a customer has at most one order per day, every order receives an unambiguous rank: 1 is newest, 2 is next, and so on.

Filtering to ranks at most 3 keeps exactly the requested prefix for each customer. A group containing one or two orders has no larger rank and therefore retains all its rows; a group with no orders contributes nothing because the final relation joins from ranked orders to customers.

**Attach names and enforce the specified presentation order**

Join the ranked orders to `Customers` by `customer_id`, select only the four requested columns, and sort by customer name ascending, customer ID ascending, and order date descending. The customer-ID key matters even though IDs are unique because different customers may share a name.

Every returned order is among its customer's top three by construction. Conversely, every top-three order receives a rank from 1 through 3 and survives the filter, proving that the result neither omits nor adds an order.

#### Complexity detail

Partitioned ranking may sort the $m$ order rows, for a conservative $O(m\log m)$ cost. Joining customer data contributes $O(c+m)$ expected work with indexed or hashed IDs, and the required final ordering is also bounded by $O(m\log m)$. The combined bound is $O(m\log m+c)$.

The rank and sort stages can retain $O(m)$ rows. The returned relation itself is excluded from the auxiliary-space statement.

#### Alternatives and edge cases

- **Correlated count of newer orders:** retain an order when fewer than three same-customer orders have a later date. It is correct but can compare $O(m^2)$ order pairs.
- **User variables in MySQL:** session-variable ranking is version-sensitive and less declarative than a window function.
- **Aggregate maximum dates:** three separate maximum-date queries can work but become cumbersome and duplicate logic.
- **Fewer than three orders:** all available orders must be returned.
- **Exactly three orders:** every order is returned, already sorted newest first.
- **More than three orders:** only ranks 1 through 3 survive.
- **No orders:** the customer contributes no row because there is no order to report.
- **Duplicate names:** customer ID ascending breaks the name tie before dates are considered.
- **Unique daily order:** no additional order-ID tie-breaker is needed within one customer.

</details>
