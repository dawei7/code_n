# Sales Person

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 607 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/sales-person/) |

## Problem Description
### Goal
Given tables of salespeople, companies, and orders linking a salesperson to a company, find every salesperson who did not have any orders related to the company whose name is `RED`.

Return the qualifying salesperson names in any order. A salesperson is excluded when even one of their orders is associated with a `RED` company, regardless of other orders they handled. Salespeople with no orders at all have no order for `RED` and therefore must be included.

### Function Contract
**Inputs**

- `SalesPerson(sales_id, name, salary, commission_rate, hire_date)`: salesperson records
- `Company(com_id, name, city)`: customer companies
- `Orders(order_id, order_date, com_id, sales_id, amount)`: orders linking companies and salespeople

**Return value**

- One column, `name`, containing every salesperson with no order associated with a `RED` company
- Salespeople with no orders qualify

### Examples
**Example 1**

- Input: Alice has an order for `RED`; Bob has only an order for `BLUE`
- Output: `Bob`

**Example 2**

- Input: Cara has no orders
- Output: `Cara`

**Example 3**

- Input: Dan has both `RED` and non-`RED` orders
- Output: no row for Dan
