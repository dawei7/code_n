## Description

Table: `Delivery`

| Column Name | Type |
| :--- | :--- |
| `delivery_id` | `int` |
| `customer_id` | `int` |
| `order_date` | `date` |
| `customer_pref_delivery_date` | `date` |

`delivery_id` is the primary key (column with unique values) of this table.
The table holds information about food delivery to customers who make orders on a certain date and specify a preferred delivery date (which can be the same as the order date or after it).

If the customer's preferred delivery date is the same as the order date, then the order is called **immediate**; otherwise, it is called **scheduled**.

Write a solution to find the percentage of immediate orders in the table, rounded to 2 decimal places.
