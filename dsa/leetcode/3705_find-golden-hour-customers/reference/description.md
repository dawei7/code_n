## Description

The `restaurant_orders` table records restaurant purchases and optional customer ratings:

| Column | Type | Meaning |
|---|---|---|
| `order_id` | `int` | Unique row identifier |
| `customer_id` | `int` | Customer placing the order |
| `order_timestamp` | `datetime` | Date and time of the order |
| `order_amount` | `decimal` | Order amount |
| `payment_method` | `varchar` | One of `cash`, `card`, or `app` |
| `order_rating` | `int` | Rating from 1 through 5, or `NULL` when unrated |

Find every **golden hour customer**. A customer qualifies only when all of these conditions hold:

- they placed at least three orders;
- at least 60% of their orders occurred during either inclusive peak interval, `11:00:00`–`14:00:00` or `18:00:00`–`21:00:00`;
- the average over rated orders is at least 4.0; and
- at least 50% of their orders have a non-`NULL` rating.

For each qualifying customer, return their identifier, order count, whole-number peak-hour percentage, and average rating rounded to two decimal places. Sort by `average_rating` descending and then by `customer_id` descending.
