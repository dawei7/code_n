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
