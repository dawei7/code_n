## Description

Table: `Spending`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| spend_date  | date    |
| platform    | enum    |
| amount      | int     |
+-------------+---------+
The table logs the history of the spending of users that make purchases from an online shopping website that has a desktop and a mobile application.
(user_id, spend_date, platform) is the primary key (combination of columns with unique values) of this table.
The platform column is an ENUM (category) type of ('desktop', 'mobile').
```

Write a solution to find the total number of users and the total amount spent using the mobile only, the desktop only, and both mobile and desktop together for each date.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Inputs**

$Spending(\text{user}_{id}, \text{spend}_{date}, platform, amount)$ contains $R$ purchase rows at the unique user-date-platform grain. The only platform values are `desktop` and `mobile`.

**Return value**

- Return exactly $\text{spend}_{date}$, `platform`, $\text{total}_{amount}$, and $\text{total}_{users}$.
- For every represented date, return one row for each of `desktop`, `mobile`, and `both`.
- Classify a user separately on each date. A user with both platform rows contributes the sum of both amounts and one user to `both`, not to either single-platform category.
- Use `0` for both measures when a date-category pair has no users.
- Result row order is unrestricted.

### Examples

#### Example 1

```
**Input:**
Spending table:
+---------+------------+----------+--------+
| user_id | spend_date | platform | amount |
+---------+------------+----------+--------+
| 1       | 2019-07-01 | mobile   | 100    |
| 1       | 2019-07-01 | desktop  | 100    |
| 2       | 2019-07-01 | mobile   | 100    |
| 2       | 2019-07-02 | mobile   | 100    |
| 3       | 2019-07-01 | desktop  | 100    |
| 3       | 2019-07-02 | desktop  | 100    |
+---------+------------+----------+--------+
**Output:**
+------------+----------+--------------+-------------+
| spend_date | platform | total_amount | total_users |
+------------+----------+--------------+-------------+
| 2019-07-01 | desktop  | 100          | 1           |
| 2019-07-01 | mobile   | 100          | 1           |
| 2019-07-01 | both     | 200          | 1           |
| 2019-07-02 | desktop  | 100          | 1           |
| 2019-07-02 | mobile   | 100          | 1           |
| 2019-07-02 | both     | 0            | 0           |
+------------+----------+--------------+-------------+
**Explanation:**
On 2019-07-01, user 1 purchased using **both** desktop and mobile, user 2 purchased using mobile **only** and user 3 purchased using desktop **only**.
On 2019-07-02, user 2 purchased using mobile **only**, user 3 purchased using desktop **only** and no one purchased using **both** platforms.
```