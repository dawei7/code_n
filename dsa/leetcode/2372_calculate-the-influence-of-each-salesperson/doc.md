# Calculate the Influence of Each Salesperson

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2372 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/calculate-the-influence-of-each-salesperson/) |

## Problem Description

### Goal

The `Salesperson` table identifies salespeople, `Customer` assigns each customer to a salesperson, and `Sales` records the price of each sale made by a customer. Calculate each salesperson's influence as the sum of all prices paid by every customer assigned to that salesperson.

Report every salesperson, including those without customers and those whose customers have no recorded sales. Their total must be `0` rather than `NULL`. Return the salesperson identifier, name, and computed total; the problem permits the result rows in any order.

### Function Contract

**Inputs**

- `Salesperson(salesperson_id, name)`: One row per salesperson; `salesperson_id` is unique.
- `Customer(customer_id, salesperson_id)`: One row per customer; `customer_id` is unique and `salesperson_id` references `Salesperson`.
- `Sales(sale_id, customer_id, price)`: One row per sale; `sale_id` is unique and `customer_id` references `Customer`.

Let $S$, $C$, and $R$ denote the numbers of rows in `Salesperson`, `Customer`, and `Sales`, respectively.

**Return value**

- Return columns `salesperson_id`, `name`, and `total`, with one row for every salesperson.
- `total` is the sum of `price` over sales made by that salesperson's customers, or `0` when no such sale exists.
- Result rows may be returned in any order.

### Examples

**Example 1**

- Input: `Salesperson = [[1,"Alice"],[2,"Bob"],[3,"Jerry"]]`, `Customer = [[1,1],[2,1],[3,2]]`, `Sales = [[1,2,892],[2,1,354],[3,3,988],[4,3,856]]`
- Output: `[[1,"Alice",1246],[2,"Bob",1844],[3,"Jerry",0]]`
- Explanation: Alice's two customers paid $892 + 354 = 1246$, Bob's customer paid $988 + 856 = 1844$, and Jerry has no customers.
