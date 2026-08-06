## Description

Table: `restaurant_orders`

```

+------------------+----------+
| Column Name      | Type     | 
+------------------+----------+
| order_id         | int      |
| customer_id      | int      |
| order_timestamp  | datetime |
| order_amount     | decimal  |
| payment_method   | varchar  |
| order_rating     | int      |
+------------------+----------+
order_id is the unique identifier for this table.
payment_method can be cash, card, or app.
order_rating is between 1 and 5, where 5 is the best (NULL if not rated).
order_timestamp contains both date and time information.

```

Write a solution to find **golden hour customers** - customers who consistently order during peak hours and provide high satisfaction. A customer is a **golden hour customer** if they meet ALL the following criteria:

<ul>
	<li>Made **at least** `3` orders.</li>
	<li>**At least** `60%` of their orders are during **peak hours **(`11:00`-`14:00` or `18:00`-`21:00`).</li>
	<li>Their **average rating** for rated orders is at least `4.0,` round it to` 2 `decimal places.</li>
	<li>Have rated **at least** `50%` of their orders.</li>
</ul>

Return *the result table ordered by* `average_rating` *in **descending** order, then by* `customer_id`​​​​​​​ *in **descending** order*.

The result format is in the following example.
