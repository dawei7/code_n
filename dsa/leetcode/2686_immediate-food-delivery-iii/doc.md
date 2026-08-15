# Immediate Food Delivery III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2686 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/immediate-food-delivery-iii/) |

## Problem Description

### Goal

The `Delivery` table records food orders. Each row has a unique delivery identifier, a customer, the date on which the order was placed, and the customer's preferred delivery date. The preferred date is never earlier than the order date.

An order is **immediate** when `customer_pref_delivery_date` equals `order_date`; otherwise it is **scheduled**. For every distinct order date, compute the percentage of that date's orders that were immediate. Round each percentage to two decimal places and return the rows in ascending `order_date` order.

### Function Contract

**Input table**

- `Delivery(delivery_id, customer_id, order_date, customer_pref_delivery_date)`: `delivery_id` is unique. Each row represents one order and its requested delivery date.

**Return value**

Return columns `order_date` and `immediate_percentage`, with one row per distinct order date. Express the percentage on the $0$ to $100$ scale, rounded to two decimal places, and order the result by `order_date` ascending.

### Examples

#### Example 1

- **Input:** On `2019-08-01`, two of three orders are immediate; on `2019-08-02`, two of three are immediate; on `2019-08-03`, both orders are immediate; and on `2019-08-04`, neither order is immediate.
- **Output:** `[["2019-08-01",66.67],["2019-08-02",66.67],["2019-08-03",100.00],["2019-08-04",0.00]]`

#### Example 2

- **Input:** `Delivery = [[1,10,"2024-01-05","2024-01-05"]]`
- **Output:** `[["2024-01-05",100.00]]`

#### Example 3

- **Input:** `Delivery = [[1,10,"2024-02-01","2024-02-03"],[2,11,"2024-02-01","2024-02-02"]]`
- **Output:** `[["2024-02-01",0.00]]`
