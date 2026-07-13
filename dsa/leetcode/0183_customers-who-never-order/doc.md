# Customers Who Never Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 183 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/customers-who-never-order/) |

## Problem Description
### Goal
The `Customers` table lists registered customer identifiers and names, while the `Orders` table records purchases and links each order to a customer through `customerId`. A customer may have no orders, one order, or several orders.

Return one column named `Customers` containing the names of all customers for whom no matching order row exists. Customers with any order must be excluded even when other joined fields are absent, and multiple orders must not duplicate or otherwise affect the result. An empty order table therefore returns every customer, while order rows cannot create output for a customer missing from the customer table.

### Function Contract
**Inputs**

- `Customers(id, name)`: registered customers
- `Orders(id, customerId)`: orders linked to customers

**Return value**

One column named `Customers` containing the names of customers with no matching order.

### Examples
**Example 1**

- Customers: `Joe, Henry, Sam, Max`
- Orders belong to: `Joe, Sam`
- Output: `Henry, Max`

**Example 2**

- Customers: `Ada`
- Orders: none
- Output: `Ada`

**Example 3**

- Every customer has an order
- Output: no rows

### Required Complexity

- **Time:** $O(c + o)$
- **Space:** $O(c + o)$

<details>
<summary>Approach</summary>

#### General

This is an **anti-join**: retain a customer only when no related order exists. One formulation starts from `Customers`, left-joins `Orders` on `Orders.customerId = Customers.id`, and keeps only null-extended rows.

Test a right-side column that is guaranteed non-null for real orders, such as `Orders.id`. If it is `NULL` after the join, no order row matched. Testing a nullable business column would be unsafe because a real matched row could itself contain null.

Multiple orders may expand one customer into several joined rows, but all of those rows have non-null order ids and are filtered out. A customer with no orders produces exactly one null-extended row and survives.

An equally direct formulation is `WHERE NOT EXISTS (SELECT 1 FROM Orders ... )`. Most optimizers recognize both forms as an anti-join. `NOT EXISTS` often communicates intent most clearly and avoids dependence on a chosen non-null right-side column.

For a customer with at least one matching order, the left join produces only matched rows whose non-null order id fails the null filter, so the customer is excluded. For a customer with no matching order, left-join semantics produce one row with all order columns null; that row passes the filter and returns the customer's name. These are exhaustive cases, so the result contains exactly customers who never ordered.

#### Complexity detail

A hash anti-join can scan `c` customers and `o` orders in $O(c + o)$ time while using $O(o)$ auxiliary storage. With an index on `Orders.customerId`, the engine may perform indexed existence checks instead. Physical complexity depends on the selected plan and indexes.

#### Alternatives and edge cases

- `NOT EXISTS` expresses the absence test directly and is null-safe.
- `NOT IN (SELECT customerId ...)` can evaluate to unknown for every candidate if the subquery contains a null, unless nullability is guaranteed or filtered.
- Grouping and counting orders per customer works but computes more information than the boolean existence condition needs.
- An empty `Orders` table returns every customer; an empty `Customers` table returns nothing.
- One or many orders both exclude the customer exactly once.

</details>
