## Description

Table: `UserActivity`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| username      | varchar |
| activity      | varchar |
| startDate     | Date    |
| endDate       | Date    |
+---------------+---------+
This table may contain duplicates rows.
This table contains information about the activity performed by each user in a period of time.
A person with username performed an activity from startDate to endDate.
```

Write a solution to show the **second most recent activity** of each user.

If the user only has one activity, return that one. A user cannot perform more than one activity at the same time.

Return the result table in **any** order.

The result format is in the following example.
### Function Contract

**Input**

- `UserActivity`: the possibly duplicate activity-history rows described above.

Let $A$ be the number of stored rows and $U$ the number of distinct users.

**Return value**

Return one row per user with these columns:

- `username`: the activity owner.
- `activity`: the selected activity name.
- `startDate`: the selected period's start date.
- `endDate`: the selected period's end date.

For a user with at least two distinct activity periods, select the second period in descending chronological order. For a user with one distinct period, select that period. Identical stored rows describe one logical period, and the result order is unrestricted.

### Examples
#### Example 1

```
**Input:**
UserActivity table:
+------------+--------------+-------------+-------------+
| username   | activity     | startDate   | endDate     |
+------------+--------------+-------------+-------------+
| Alice      | Travel       | 2020-02-12  | 2020-02-20  |
| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
| Alice      | Travel       | 2020-02-24  | 2020-02-28  |
| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
+------------+--------------+-------------+-------------+
**Output:**
+------------+--------------+-------------+-------------+
| username   | activity     | startDate   | endDate     |
+------------+--------------+-------------+-------------+
| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
+------------+--------------+-------------+-------------+
**Explanation:**
The most recent activity of Alice is Travel from 2020-02-24 to 2020-02-28, before that she was dancing from 2020-02-21 to 2020-02-23.
Bob only has one record, we just take that one.
```