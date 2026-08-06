## Description

Table: `app_events`

```

+------------------+----------+
| Column Name      | Type     | 
+------------------+----------+
| event_id         | int      |
| user_id          | int      |
| event_timestamp  | datetime |
| event_type       | varchar  |
| session_id       | varchar  |
| event_value      | int      |
+------------------+----------+
event_id is the unique identifier for this table.
event_type can be app_open, click, scroll, purchase, or app_close.
session_id groups events within the same user session.
event_value represents: for purchase - amount in dollars, for scroll - pixels scrolled, for others - NULL.

```

Write a solution to identify **zombie sessions, **sessions where users appear active but show abnormal behavior patterns. A session is considered a **zombie session** if it meets ALL the following criteria:

<ul>
	<li>The session duration is **more than** `30` minutes.</li>
	<li>Has **at least** `5` scroll events.</li>
	<li>The **click-to-scroll ratio** is less than `0.20` .</li>
	<li>**No purchases** were made during the session.</li>
</ul>

Return *the result table ordered by* `scroll_count` *in **descending** order, then by* `session_id` *in **ascending** order*.

The result format is in the following example.
