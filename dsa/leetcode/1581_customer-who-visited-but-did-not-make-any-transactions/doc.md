# Customer Who Visited but Did Not Make Any Transactions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1581 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) |

## Problem Description
### Goal

The `Visits` table records each store visit and the customer who made it. The `Transactions` table records purchases, with every transaction linked to the visit during which it occurred.

Identify visits for which no transaction was made. A visit with several transactions is still a transactional visit and must contribute nothing, while multiple transaction-free visits by the same customer must all be counted.

Return each customer who has at least one transaction-free visit together with the number of such visits. Result rows may appear in any order.

### Function Contract
**Inputs**

- `Visits(visit_id, customer_id)`: visit records keyed by `visit_id`.
- `Transactions(transaction_id, visit_id, amount)`: transaction records keyed by `transaction_id`; `visit_id` identifies the associated visit.

**Return value**

Return columns `customer_id` and `count_no_trans`, with one row per customer and the count of that customer's visits having no matching transaction.

### Examples
**Example 1**

- Input: visits by customers 23, 9, 30, 54, and 96, with transactions attached only to visit IDs 1, 2, and 5
- Output: customer 30 has one transaction-free visit, customer 54 has two, and customer 96 has one

**Example 2**

- Input: one visit with no transaction
- Output: that customer with `count_no_trans = 1`

**Example 3**

- Input: every visit has at least one transaction
- Output: an empty result
