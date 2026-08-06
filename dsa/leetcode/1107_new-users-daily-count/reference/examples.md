## Examples

**Example 1**

- **Input:** `Traffic = [[1,"login","2019-05-01"],[1,"homepage","2019-05-01"],[1,"logout","2019-05-01"],[2,"login","2019-06-21"],[2,"logout","2019-06-21"],[3,"login","2019-01-01"],[3,"jobs","2019-01-01"],[3,"logout","2019-01-01"],[4,"login","2019-06-21"],[4,"groups","2019-06-21"],[4,"logout","2019-06-21"],[5,"login","2019-03-01"],[5,"logout","2019-03-01"],[5,"login","2019-06-21"],[5,"logout","2019-06-21"]]`

| user_id | activity | activity_date |
|---:|---|---|
| 1 | login | 2019-05-01 |
| 1 | homepage | 2019-05-01 |
| 1 | logout | 2019-05-01 |
| 2 | login | 2019-06-21 |
| 2 | logout | 2019-06-21 |
| 3 | login | 2019-01-01 |
| 3 | jobs | 2019-01-01 |
| 3 | logout | 2019-01-01 |
| 4 | login | 2019-06-21 |
| 4 | groups | 2019-06-21 |
| 4 | logout | 2019-06-21 |
| 5 | login | 2019-03-01 |
| 5 | logout | 2019-03-01 |
| 5 | login | 2019-06-21 |
| 5 | logout | 2019-06-21 |

- **Output:** `[["2019-05-01",1],["2019-06-21",2]]`

| login_date | user_count |
|---|---:|
| 2019-05-01 | 1 |
| 2019-06-21 | 2 |

- **Explanation:** Only dates with a nonzero user count appear. User `5` is not counted on `2019-06-21` because that user's first login was on `2019-03-01`.
