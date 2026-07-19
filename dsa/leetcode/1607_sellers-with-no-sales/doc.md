# Sellers With No Sales

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1607 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/sellers-with-no-sales/) |

## Problem Description
### Goal
The database records customers, sellers, and orders. Each order identifies its customer and seller, its cost, and the date on which the sale occurred.

Find every seller who made no sale from January 1, 2020 through December 31, 2020, including both boundary dates. A seller still qualifies when they have orders outside 2020 or have never appeared in `Orders` at all. Return the qualifying seller names in ascending lexicographic order.

### Function Contract
**Inputs**

- `Customer(customer_id, customer_name)`, containing customer identifiers and names.
- `Seller(seller_id, seller_name)`, containing seller identifiers and names.
- `Orders(order_id, sale_date, order_cost, customer_id, seller_id)`, with one row per sale and foreign identifiers for its customer and seller.

**Return value**

Return a relation with the single column `seller_name`. Include sellers for whom no matching order has `sale_date` between `2020-01-01` and `2020-12-31`, and order the rows by `seller_name` ascending.

### Examples
**Example 1**

- Input: Daniel and Elizabeth have sales during 2020, while Frank's only sale is in 2019.
- Output: `Frank`

**Example 2**

- Input: A seller has orders on `2020-01-01` and `2020-12-31`.
- Output: That seller is excluded because both endpoints belong to the target interval.

**Example 3**

- Input: A seller has no rows in `Orders`.
- Output: That seller is included.
