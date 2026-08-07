<!-- Don't delete this -->
[TOC]

# Solution

---

## pandas

<!-- h3 for approaches -->
### Approach 1: Merge (cross) & Conditional Index

<!-- h4 for sections -->
#### Overview

<!-- Describe your approach to solving the problem. -->
In this problem, we are tasked with finding the $\text{account}_{id}$s that should be banned from Leetflex. An account should be banned if an account was logged in at the same moment from two different IP addresses.

Given the $\text{log}_{info}$ table:

| account_id | ip_address | login               | logout              |
|------------|------------|---------------------|---------------------|
| 1          | 1          | 2021-02-01 09:00:00 | 2021-02-01 09:30:00 |
| 1          | 2          | 2021-02-01 08:00:00 | 2021-02-01 11:30:00 |
| 2          | 6          | 2021-02-01 20:30:00 | 2021-02-01 22:00:00 |
| 2          | 7          | 2021-02-02 20:30:00 | 2021-02-02 22:00:00 |
| 3          | 9          | 2021-02-01 16:00:00 | 2021-02-01 16:59:59 |
| 3          | 13         | 2021-02-01 17:00:00 | 2021-02-01 17:59:59 |
| 4          | 10         | 2021-02-01 16:00:00 | 2021-02-01 17:00:00 |
| 4          | 11         | 2021-02-01 17:00:00 | 2021-02-01 17:59:59 |

<br>

1. **Cross join $\text{log}_{info}$ onto $\text{log}_{info}$**

```python
df = log_info.merge(log_info, how="cross")
```
We merge $\text{log}_{info}$ onto itself to create the cartesian product of rows from the first dataframe to the second dataframe. In other words, it will combine each row of the first dataframe with each row from the second dataframe.

| account_id_x | ip_address_x | login_x            | logout_x           | account_id_y | ip_address_y | login_y             | logout_y          |
|--------------|--------------|--------------------|--------------------|--------------|--------------|---------------------|-------------------|
|1             |1             |2021-02-01 09:00:00 |2021-02-01 09:30:00 |1             |1             |2021-02-01 09:00:00  |2021-02-01 09:30:00|
|1             |1             |2021-02-01 09:00:00 |2021-02-01 09:30:00 |1             |2             |2021-02-01 08:00:00  |2021-02-01 11:30:00|
|1             |1             |2021-02-01 09:00:00 |2021-02-01 09:30:00 |2             |6             |2021-02-01 20:30:00  |2021-02-01 22:00:00|
|1             |1             |2021-02-01 09:00:00 |2021-02-01 09:30:00 |2             |7             |2021-02-02 20:30:00  |2021-02-02 22:00:00|
|1             |1             |2021-02-01 09:00:00 |2021-02-01 09:30:00 |3             |9             |2021-02-01 16:00:00  |2021-02-01 16:59:59|
`59 more rows`
<br>

2. **Conditional filtering**
```python
# Filter on account_id, ip_address and login/logout
df = df[df['account_id_x'] == df['account_id_y']]
df = df[df['ip_address_x'] != df['ip_address_y']]
df = df[(df['login_x'] <= df['logout_y']) & (df['login_y'] <= df['logout_x'])]
```

We filter the rows and select accounts that meet the given filtering conditions:
- `account_id_x` and `account_id_y` are the same.
- `ip_address_x` and `ip_address_y` are different.
- The account is logged in at the same time, which is similar to determining whether two intervals overlap. There are several ways to implement this, and we provide one approach: $\text{login}_{x}$ is less than or equal to $\text{logout}_{y}$, and $\text{login}_{y}$ is less than or equal to $\text{logout}_{x}$. If this condition is met, it indicates the presence of overlapping login sessions for this account.

| account_id_x | ip_address_x | login_x            | logout_x           | account_id_y | ip_address_y | login_y             | logout_y          |
|--------------|--------------|--------------------|--------------------|--------------|--------------|---------------------|-------------------|
|1             |1             |2021-02-01 09:00:00 | 2021-02-01 09:30:00|1             |2             |2021-02-01 08:00:00  |2021-02-01 11:30:00|
|1             |2             |2021-02-01 08:00:00 | 2021-02-01 11:30:00|1             |1             |2021-02-01 09:00:00  |2021-02-01 09:30:00|
|4             |10            |2021-02-01 16:00:00 | 2021-02-01 17:00:00|4             |11            |2021-02-01 17:00:00  |2021-02-01 17:59:59|
|4             |11            |2021-02-01 17:00:00 | 2021-02-01 17:59:59|4             |10            |2021-02-01 16:00:00  |2021-02-01 17:00:00|
<br>

3. **Cleaning dataframe and renaming columns**
```python
# Drop duplicates on account_id
df = df.drop_duplicates('account_id_x')

# Rename output column
df = df.rename(columns={'account_id_x': 'account_id'})
```

After the conditional filter on `df`, we utilize the $\text{drop}_{duplicates}()$ method, passing in `account_id_x`, which will remove like `account_id_x`s resulting in unique values only. Finally, we will rename `account_id_x` to $\text{account}_{id}$ to conform to the resulting dataframe.

| account_id |
|------------|
| 1          |
| 4          |

<br>

<!-- h4 for sections -->
#### Implementation

```python
import pandas as pd

def leetflex_banned_accnts(log_info: pd.DataFrame) -> pd.DataFrame:
    # Approach: .merge(cross) and filter
    df = log_info.merge(log_info, how="cross")

    # Filter rows that have same account_id, different ip_address, and overlapped logged in times.
    df = df[df['account_id_x'] == df['account_id_y']]
    df = df[df['ip_address_x'] != df['ip_address_y']]
    df = df[(df['login_x'] <= df['logout_y']) & (df['login_y'] <= df['logout_x'])]

    # Drop duplicates on account_id
    df = df.drop_duplicates('account_id_x')

    # Rename output column
    df = df.rename(columns={'account_id_x': 'account_id'})

    return df[['account_id']]
```

<!-- an empty line to separate approaches -->
<br>

---

## Database

<!-- h3 for approaches -->
### Approach 1: Using `CROSS JOIN` and `DISTINCT`

<!-- h4 for sections -->
#### Algorithm

<!-- Describe your approach to solving the problem. -->
In SQL, we can utilize `CROSS JOIN` to create the cartesian product of `LogInfo` joined onto `LogInfo`, resulting in a table that contains all pairs of rows between both tables. Following this join, we need to find which accounts will be banned and to achieve this, we will utilize the `WHERE` clause to filter the rows and select accounts that meet the given filtering conditions:
- $l1.\text{account}_{id}$ and $l2.\text{account}_{id}$ are the same.
- $l1.\text{ip}_{address}$ and $l2.\text{ip}_{address}$ are different.
- The account is logged in at the same time, which is similar to determining whether two intervals overlap. There are several ways to implement this, and we provide one approach: `l1.login` is less than or equal to `l2.logout`, and `l2.login` is less than or equal to `11.logout`. If this condition is met, it indicates the presence of overlapping login sessions for this account.

Given we utilized a `CROSS JOIN` to join the table onto itself, there may be duplicate accounts in the resulting table. To resolve this, we will use `DISTINCT` with the $\text{account}_{id}$ column to retrieve unique values.

<!-- h4 for sections -->
#### Implementation

```sql
SELECT
  DISTINCT l1.account_id
FROM
  LogInfo l1
CROSS JOIN
  LogInfo l2
WHERE
  l1.account_id = l2.account_id AND
  l1.ip_address != l2.ip_address AND
  l1.login <= l2.logout AND l2.login <= l1.logout
```

<!-- an empty line to separate approaches -->
<br>