## Examples

**Example 1**

- **Input:** `Failed = [["2018-12-28"],["2018-12-29"],["2019-01-04"],["2019-01-05"]], Succeeded = [["2018-12-30"],["2018-12-31"],["2019-01-01"],["2019-01-02"],["2019-01-03"],["2019-01-06"]]`

`Failed`

| fail_date |
|---|
| 2018-12-28 |
| 2018-12-29 |
| 2019-01-04 |
| 2019-01-05 |

`Succeeded`

| success_date |
|---|
| 2018-12-30 |
| 2018-12-31 |
| 2019-01-01 |
| 2019-01-02 |
| 2019-01-03 |
| 2019-01-06 |

- **Output:** `[["succeeded","2019-01-01","2019-01-03"],["failed","2019-01-04","2019-01-05"],["succeeded","2019-01-06","2019-01-06"]]`

| period_state | start_date | end_date |
|---|---|---|
| succeeded | 2019-01-01 | 2019-01-03 |
| failed | 2019-01-04 | 2019-01-05 |
| succeeded | 2019-01-06 | 2019-01-06 |

- **Explanation:** Dates from 2018 are omitted because the report covers only 2019. Tasks succeeded from January 1 through January 3, failed from January 4 through January 5, and succeeded again on January 6; these become the three displayed periods, with the final one having identical endpoints.
