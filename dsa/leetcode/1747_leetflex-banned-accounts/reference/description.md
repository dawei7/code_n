## Description

Table: `LogInfo`

```
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| account_id  | int      |
| ip_address  | int      |
| login       | datetime |
| logout      | datetime |
+-------------+----------+
This table may contain duplicate rows.
The table contains information about the login and logout dates of Leetflex accounts. It also contains the IP address from which the account was logged in and out.
It is guaranteed that the logout time is after the login time.
```

Write a solution to find the $\text{account}_{id}$ of the accounts that should be banned from Leetflex. An account should be banned if it was logged in at some moment from two different IP addresses.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Database Schema**

**`LogInfo`**

| Column | Type | Meaning |
|---|---|---|
| $\text{account}_{id}$ | int | User account identifier. |
| $\text{ip}_{address}$ | int | IP address used for the login session. |
| `login` | datetime | Timestamp when session started. |
| `logout` | datetime | Timestamp when session ended. |

- $(\text{account}_{id}, \text{ip}_{address}, login)$ is unique.

**Return value**

Return a table with the single column $\text{account}_{id}$. Include each $\text{account}_{id}$ at most once for which at least two sessions from different IP addresses have overlapping time intervals ($login1 \le logout2 AND login2 \le logout1$).

### Examples

#### Example 1

```
**Input:**
LogInfo table:
+------------+------------+---------------------+---------------------+
| account_id | ip_address | login               | logout              |
+------------+------------+---------------------+---------------------+
| 1          | 1          | 2021-02-01 09:00:00 | 2021-02-01 09:30:00 |
| 1          | 2          | 2021-02-01 08:00:00 | 2021-02-01 11:30:00 |
| 2          | 6          | 2021-02-01 20:30:00 | 2021-02-01 22:00:00 |
| 2          | 7          | 2021-02-02 20:30:00 | 2021-02-02 22:00:00 |
| 3          | 9          | 2021-02-01 16:00:00 | 2021-02-01 16:59:59 |
| 3          | 13         | 2021-02-01 17:00:00 | 2021-02-01 17:59:59 |
| 4          | 10         | 2021-02-01 16:00:00 | 2021-02-01 17:00:00 |
| 4          | 11         | 2021-02-01 17:00:00 | 2021-02-01 17:59:59 |
+------------+------------+---------------------+---------------------+
**Output:**
+------------+
| account_id |
+------------+
| 1          |
| 4          |
+------------+
**Explanation:**
Account ID 1 --> The account was active from "2021-02-01 09:00:00" to "2021-02-01 09:30:00" with two different IP addresses (1 and 2). It should be banned.
Account ID 2 --> The account was active from two different addresses (6, 7) but in **two different times**.
Account ID 3 --> The account was active from two different addresses (9, 13) on the same day but **they do not intersect at any moment**.
Account ID 4 --> The account was active from "2021-02-01 17:00:00" to "2021-02-01 17:00:00" with two different IP addresses (10 and 11). It should be banned.
```