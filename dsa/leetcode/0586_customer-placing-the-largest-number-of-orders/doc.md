# Customer Placing the Largest Number of Orders

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 586 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/) |

## Problem Description
### Goal
Given an `Orders` table in which every row has a unique `order_number` and the `customer_number` of the customer who placed it, count how many orders were placed by each customer.

Return the `customer_number` belonging to the customer who placed the largest number of orders. The test data guarantees that exactly one customer has more orders than every other customer, so the output contains one row and no tie-breaking rule is needed.

### Function Contract
**Inputs**

- `Orders(order_number, customer_number)`: orders and the customer that placed each one

**Return value**

- A one-row result grid with column `customer_number`
- The input guarantees that one customer has strictly more orders than every other customer

### Examples
**Example 1**

- Input: customer 1 has two orders and customer 2 has three
- Output: `2`

**Example 2**

- Input: one order from one customer
- Output: that customer's identifier

**Example 3**

- Input: order numbers are unsorted but customer 7 occurs most often
- Output: `7`
