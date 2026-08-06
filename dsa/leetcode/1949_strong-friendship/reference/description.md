## Description

Table: `Friendship`

```text
+-------------+------+
| Column Name | Type |
+-------------+------+
| user1_id    | int  |
| user2_id    | int  |
+-------------+------+
(user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the users user1_id and user2_id are friends.
Note that user1_id < user2_id.
```

A friendship between a pair of friends `x` and `y` is strong if `x` and `y` have at least three common friends.

Write a solution to find all the strong friendships.

Note that the result table should not contain duplicates with `user1_id < user2_id`.

Return the result table in **any order**.

