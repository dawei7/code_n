## Description

Table: `Sessions`

```text
+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| user_id       | int      |
| session_id    | int      |
| session_type  | enum     |
| session_start | datetime |
| session_end   | datetime |
| sessions_count| int      |
+---------------+----------+
session_id is the column with unique values for this table.
session_type is an ENUM (category) of type ('Viewer', 'Streamer').
Each row of this table contains user_id, session_id, session_type, session_start, session_end, and sessions_count.
```

Write a solution to find the number of streaming sessions for users whose **first session** was as a **Viewer** and who later became a **Streamer**.

Return the result table ordered by `sessions_count` in **descending** order, and in case of a tie, by `user_id` in **descending** order.
