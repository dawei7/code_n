# Immediate Food Delivery I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1173 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [immediate-food-delivery-i](https://leetcode.com/problems/immediate-food-delivery-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/immediate-food-delivery-i/).

### Goal
Calculate the percentage of deliveries where the order date equals the customer's preferred delivery date. Round the percentage to two decimal places.

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
| 2 | 5 | 2019-08-02 | 2019-08-02 |
| 3 | 1 | 2019-08-11 | 2019-08-11 |
| 4 | 3 | 2019-08-24 | 2019-08-26 |
| 5 | 4 | 2019-08-21 | 2019-08-22 |
| 6 | 2 | 2019-08-11 | 2019-08-13 |

Output:

| immediate_percentage |
|---:|
| 33.33 |

---

## Solution
### Approach
Use a conditional aggregate: count rows where `order_date = customer_pref_delivery_date`, divide by the total number of rows, multiply by `100`, and round to two decimals.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, all delivery rows are scanned once.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
