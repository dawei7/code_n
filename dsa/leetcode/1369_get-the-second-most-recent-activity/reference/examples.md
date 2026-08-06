## Examples

**Example 1**

- **Input:** `UserActivity = [["Alice","Travel","2020-02-12","2020-02-20"],["Alice","Dancing","2020-02-21","2020-02-23"],["Alice","Travel","2020-02-24","2020-02-28"],["Bob","Travel","2020-02-11","2020-02-18"]]`

`UserActivity`:

| username | activity | startDate | endDate |
|---|---|:---:|:---:|
| Alice | Travel | 2020-02-12 | 2020-02-20 |
| Alice | Dancing | 2020-02-21 | 2020-02-23 |
| Alice | Travel | 2020-02-24 | 2020-02-28 |
| Bob | Travel | 2020-02-11 | 2020-02-18 |

- **Output:** `[["Alice","Dancing","2020-02-21","2020-02-23"],["Bob","Travel","2020-02-11","2020-02-18"]]`

| username | activity | startDate | endDate |
|---|---|:---:|:---:|
| Alice | Dancing | 2020-02-21 | 2020-02-23 |
| Bob | Travel | 2020-02-11 | 2020-02-18 |

- **Explanation:** Alice's newest activity is Travel from `2020-02-24` through `2020-02-28`; immediately before it, she was Dancing from `2020-02-21` through `2020-02-23`, so Dancing is selected. Bob has only one recorded activity, so that Travel row is returned.
