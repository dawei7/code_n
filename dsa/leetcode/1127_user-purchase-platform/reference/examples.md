## Examples

**Example 1**

- **Input:** `Spending = [[1,"2019-07-01","mobile",100],[1,"2019-07-01","desktop",100],[2,"2019-07-01","mobile",100],[2,"2019-07-02","mobile",100],[3,"2019-07-01","desktop",100],[3,"2019-07-02","desktop",100]]`

| user_id | spend_date | platform | amount |
|---:|---|---|---:|
| 1 | 2019-07-01 | mobile | 100 |
| 1 | 2019-07-01 | desktop | 100 |
| 2 | 2019-07-01 | mobile | 100 |
| 2 | 2019-07-02 | mobile | 100 |
| 3 | 2019-07-01 | desktop | 100 |
| 3 | 2019-07-02 | desktop | 100 |

- **Output:** `[["2019-07-01","desktop",100,1],["2019-07-01","mobile",100,1],["2019-07-01","both",200,1],["2019-07-02","desktop",100,1],["2019-07-02","mobile",100,1],["2019-07-02","both",0,0]]`

| spend_date | platform | total_amount | total_users |
|---|---|---:|---:|
| 2019-07-01 | desktop | 100 | 1 |
| 2019-07-01 | mobile | 100 | 1 |
| 2019-07-01 | both | 200 | 1 |
| 2019-07-02 | desktop | 100 | 1 |
| 2019-07-02 | mobile | 100 | 1 |
| 2019-07-02 | both | 0 | 0 |

- **Explanation:** On `2019-07-01`, user `1` purchased through both desktop and mobile, user `2` used only mobile, and user `3` used only desktop. On `2019-07-02`, user `2` used only mobile, user `3` used only desktop, and no user purchased through both platforms.
