# Products With Three or More Orders in Two Consecutive Years

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2292 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/products-with-three-or-more-orders-in-two-consecutive-years/) |

## Problem Description

### Goal

The `Orders` table records purchases. Each row has a unique `order_id`, the
ordered `product_id`, a `quantity`, and the order's `purchase_date`. An order
counts once for this task regardless of its quantity.

Report the IDs of products that have at least three orders in one calendar
year and at least three orders again in the immediately following calendar
year. A product may qualify through any pair of consecutive years, and it must
appear only once in the result. The rows may be returned in any order.

### Function Contract

**Inputs**

- `Orders`: Rows with integer `order_id`, integer `product_id`, integer `quantity`, and date-valued `purchase_date`; `order_id` is unique.

Let $r$ be the number of order rows and $g$ the number of distinct
product-year groups.

**Return value**

A one-column table named `product_id` containing every qualifying product
exactly once, in any order.

### Examples

#### Example 1

- **Input:** product `1` has three orders in 2020 and three in 2021; product `2` has one order in 2022
- **Output:** product `1`

#### Example 2

- **Input:** a product has three orders in 2020 and three in 2022, but none in 2021
- **Output:** no rows

#### Example 3

- **Input:** a product has four orders in 2023 and five in 2024
- **Output:** that product once
