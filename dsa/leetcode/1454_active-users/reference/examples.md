## Examples

**Example 1**

- **Input:** `Accounts = [[1,"Winston"],[7,"Jonathan"]], Logins = [[7,"2020-05-30"],[1,"2020-05-30"],[7,"2020-05-31"],[7,"2020-06-01"],[7,"2020-06-02"],[7,"2020-06-02"],[7,"2020-06-03"],[1,"2020-06-07"],[7,"2020-06-10"]]`

| id | name |
|---:|---|
| 1 | `Winston` |
| 7 | `Jonathan` |

| id | login_date |
|---:|---|
| 7 | `2020-05-30` |
| 1 | `2020-05-30` |
| 7 | `2020-05-31` |
| 7 | `2020-06-01` |
| 7 | `2020-06-02` |
| 7 | `2020-06-02` |
| 7 | `2020-06-03` |
| 1 | `2020-06-07` |
| 7 | `2020-06-10` |

- **Output:** `[[7,"Jonathan"]]`

| id | name |
|---:|---|
| 7 | `Jonathan` |

- **Explanation:** Winston, whose ID is `1`, logged in twice on only two
  different dates, so he is not active. Jonathan, whose ID is `7`, logged in
  seven times across six distinct dates. Five of those dates are consecutive,
  so Jonathan is an active user.
