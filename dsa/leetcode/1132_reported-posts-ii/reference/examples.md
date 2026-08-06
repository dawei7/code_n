## Examples

**Example 1**

- **Input:** `Actions = [[1,1,"2019-07-01","view",null],[1,1,"2019-07-01","like",null],[1,1,"2019-07-01","share",null],[2,2,"2019-07-04","view",null],[2,2,"2019-07-04","report","spam"],[3,4,"2019-07-04","view",null],[3,4,"2019-07-04","report","spam"],[4,3,"2019-07-02","view",null],[4,3,"2019-07-02","report","spam"],[5,2,"2019-07-03","view",null],[5,2,"2019-07-03","report","racism"],[5,5,"2019-07-03","view",null],[5,5,"2019-07-03","report","racism"]], Removals = [[2,"2019-07-20"],[3,"2019-07-18"]]`

Actions:

| user_id | post_id | action_date | action | extra |
|---:|---:|---|---|---|
| 1 | 1 | 2019-07-01 | view | `null` |
| 1 | 1 | 2019-07-01 | like | `null` |
| 1 | 1 | 2019-07-01 | share | `null` |
| 2 | 2 | 2019-07-04 | view | `null` |
| 2 | 2 | 2019-07-04 | report | spam |
| 3 | 4 | 2019-07-04 | view | `null` |
| 3 | 4 | 2019-07-04 | report | spam |
| 4 | 3 | 2019-07-02 | view | `null` |
| 4 | 3 | 2019-07-02 | report | spam |
| 5 | 2 | 2019-07-03 | view | `null` |
| 5 | 2 | 2019-07-03 | report | racism |
| 5 | 5 | 2019-07-03 | view | `null` |
| 5 | 5 | 2019-07-03 | report | racism |

Removals:

| post_id | remove_date |
|---:|---|
| 2 | 2019-07-20 |
| 3 | 2019-07-18 |

- **Output:** `[[75.00]]`

| average_daily_percent |
|---:|
| 75.00 |

- **Explanation:** On `2019-07-04`, one of the two posts reported as spam was removed, so the daily percentage is $50\%$. On `2019-07-02`, the only spam-reported post was removed, producing $100\%$. The other dates contain no spam reports and are excluded, so the average is $(50 + 100) / 2 = 75\%$. The output is one number, and the removal dates themselves do not matter.
