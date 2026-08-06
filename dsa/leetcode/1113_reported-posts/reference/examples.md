## Examples

**Example 1**

- **Input:** `Actions = [[1,1,"2019-07-01","view",null],[1,1,"2019-07-01","like",null],[1,1,"2019-07-01","share",null],[2,4,"2019-07-04","view",null],[2,4,"2019-07-04","report","spam"],[3,4,"2019-07-04","view",null],[3,4,"2019-07-04","report","spam"],[4,3,"2019-07-02","view",null],[4,3,"2019-07-02","report","spam"],[5,2,"2019-07-04","view",null],[5,2,"2019-07-04","report","racism"],[5,5,"2019-07-04","view",null],[5,5,"2019-07-04","report","racism"]]`

| user_id | post_id | action_date | action | extra |
|---:|---:|---|---|---|
| 1 | 1 | 2019-07-01 | view | null |
| 1 | 1 | 2019-07-01 | like | null |
| 1 | 1 | 2019-07-01 | share | null |
| 2 | 4 | 2019-07-04 | view | null |
| 2 | 4 | 2019-07-04 | report | spam |
| 3 | 4 | 2019-07-04 | view | null |
| 3 | 4 | 2019-07-04 | report | spam |
| 4 | 3 | 2019-07-02 | view | null |
| 4 | 3 | 2019-07-02 | report | spam |
| 5 | 2 | 2019-07-04 | view | null |
| 5 | 2 | 2019-07-04 | report | racism |
| 5 | 5 | 2019-07-04 | view | null |
| 5 | 5 | 2019-07-04 | report | racism |

- **Output:** `[["spam",1],["racism",2]]`

| report_reason | report_count |
|---|---:|
| spam | 1 |
| racism | 2 |

- **Explanation:** Only report reasons with a nonzero number of reported posts matter.
