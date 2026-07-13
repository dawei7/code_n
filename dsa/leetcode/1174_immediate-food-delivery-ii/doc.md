# Immediate Food Delivery II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1174 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [immediate-food-delivery-ii](https://leetcode.com/problems/immediate-food-delivery-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/immediate-food-delivery-ii/).

### Goal
For each customer, consider only their first order by `order_date`. Return the percentage of those first orders that were immediate, rounded to two decimal places.

### Query Contract
**Input table**

- `Delivery(delivery_id, customer_id, order_date, customer_pref_delivery_date)`: Food delivery orders.

**Output column**

- `immediate_percentage`

### Examples
**Example 1**

`Delivery`

| delivery_id | customer_id | order_date | customer_pref_delivery_date |
|---:|---:|---|---|
| 1 | 1 | 2019-08-01 | 2019-08-02 |
| 2 | 2 | 2019-08-02 | 2019-08-02 |
| 3 | 1 | 2019-08-11 | 2019-08-12 |
| 4 | 3 | 2019-08-24 | 2019-08-24 |
| 5 | 3 | 2019-08-21 | 2019-08-22 |
| 6 | 2 | 2019-08-11 | 2019-08-13 |
| 7 | 4 | 2019-08-09 | 2019-08-09 |

Output:

| immediate_percentage |
|---:|
| 50.00 |

---

## Solution
### Approach
Find each customer's earliest `order_date`, then keep only deliveries matching that first date. Among those first orders, compute the percentage where `order_date` equals `customer_pref_delivery_date`.

A window function with `ROW_NUMBER()` or a grouped minimum date joined back to `Delivery` both express the same idea.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, deliveries are grouped by customer and then aggregated.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
