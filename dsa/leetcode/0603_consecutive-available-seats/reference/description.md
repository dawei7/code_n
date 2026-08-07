## Description

Table: `Cinema`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| seat_id     | int  |
| free        | bool |
+-------------+------+
seat_id is an auto-increment column for this table.
Each row of this table indicates whether the i^th seat is free or not. 1 means free while 0 means occupied.
```

Find all the consecutive available seats in the cinema.

Return the result table **ordered** by $\text{seat}_{id}$ **in ascending order**.

The test cases are generated so that more than two seats are consecutively available.

The result format is in the following example.
### Function Contract

**Input**

`Cinema(seat_id, free)` contains the seat availability rows. Let $n$ be its row count.

**Return value**

Return a one-column table containing each free `seat_id` that has a free seat at `seat_id - 1` or `seat_id + 1`. Sort the result by `seat_id` in ascending order.

### Examples
#### Example 1

```
**Input:**
Cinema table:
+---------+------+
| seat_id | free |
+---------+------+
| 1       | 1    |
| 2       | 0    |
| 3       | 1    |
| 4       | 1    |
| 5       | 1    |
+---------+------+
**Output:**
+---------+
| seat_id |
+---------+
| 3       |
| 4       |
| 5       |
+---------+
```