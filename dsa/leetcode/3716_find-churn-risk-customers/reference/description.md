## Description

Table: `subscription_events`

```

+------------------+---------+
| Column Name      | Type    | 
+------------------+---------+
| event_id         | int     |
| user_id          | int     |
| event_date       | date    |
| event_type       | varchar |
| plan_name        | varchar |
| monthly_amount   | decimal |
+------------------+---------+
event_id is the unique identifier for this table.
event_type can be start, upgrade, downgrade, or cancel.
plan_name can be basic, standard, premium, or NULL (when event_type is cancel).
monthly_amount represents the monthly subscription cost after this event.
For cancel events, monthly_amount is 0.

```

Write a solution to **Find Churn Risk Customers** - users who show warning signs before churning. A user is considered **churn risk customer** if they meet ALL the following criteria:

<ul>
	<li>Currently have an **active subscription** (their last event is not cancel).</li>
	<li>Have performed **at least one** downgrade in their subscription history.</li>
	<li>Their **current plan revenue** is less than `50%` of their historical maximum plan revenue.</li>
	<li>Have been a subscriber for **at least** `60` days.</li>
</ul>

Return *the result table ordered by* `days_as_subscriber` *in **descending** order, then by* `user_id` *in **ascending** order*.

The result format is in the following example.
