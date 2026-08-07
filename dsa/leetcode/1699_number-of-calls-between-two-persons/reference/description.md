## Description

Table: `Calls`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| from_id     | int     |
| to_id       | int     |
| duration    | int     |
+-------------+---------+
This table does not have a primary key (column with unique values), it may contain duplicates.
This table contains the duration of a phone call between from_id and to_id.
from_id != to_id
```

Write a solution to report the number of calls and the total call duration between each pair of distinct persons `(person1, person2)` where `person1 < person2`.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Database Schema**

**`Calls`**

| Column | Type | Meaning |
|---|---|---|
| `from_id` | int | User ID of caller. |
| `to_id` | int | User ID of recipient. |
| `duration` | int | Duration of call in seconds. |

- `from_id != to_id`. Duplicate rows represent separate calls.

**Return value**

Return a table with columns `person1`, `person2`, `call_count`, and `total_duration`. `person1 < person2` for every row. Include one row per distinct unordered pair of users who have called each other. Row order is unrestricted.

### Examples
#### Example 1

```
**Input:**
Calls table:
+---------+-------+----------+
| from_id | to_id | duration |
+---------+-------+----------+
| 1       | 2     | 59       |
| 2       | 1     | 11       |
| 1       | 3     | 20       |
| 3       | 4     | 100      |
| 3       | 4     | 200      |
| 3       | 4     | 200      |
| 4       | 3     | 499      |
+---------+-------+----------+
**Output:**
+---------+---------+------------+----------------+
| person1 | person2 | call_count | total_duration |
+---------+---------+------------+----------------+
| 1       | 2       | 2          | 70             |
| 1       | 3       | 1          | 20             |
| 3       | 4       | 4          | 999            |
+---------+---------+------------+----------------+
**Explanation:**
Users 1 and 2 had 2 calls and the total duration is 70 (59 + 11).
Users 1 and 3 had 1 call and the total duration is 20.
Users 3 and 4 had 4 calls and the total duration is 999 (100 + 200 + 200 + 499).
```