### 1. Description

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

### 2. Function Contract

**Input**

$Cinema(\text{seat}_{id}, free)$ contains the seat availability rows. Let $n$ be its row count.

**Return value**

Return a one-column table containing each free $\text{seat}_{id}$ that has a free seat at $\text{seat}_{id} - 1$ or $\text{seat}_{id} + 1$. Sort the result by $\text{seat}_{id}$ in ascending order.

### 3. Examples

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