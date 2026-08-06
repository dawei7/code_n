## Examples

**Example 1**

- **Input:** `Activity = [[1,2,"2016-03-01",5],[1,2,"2016-03-02",6],[2,3,"2017-06-25",1],[3,1,"2016-03-01",0],[3,4,"2016-07-03",5]]`

`Activity`:

| player_id | device_id | event_date | games_played |
|---:|---:|---|---:|
| 1 | 2 | 2016-03-01 | 5 |
| 1 | 2 | 2016-03-02 | 6 |
| 2 | 3 | 2017-06-25 | 1 |
| 3 | 1 | 2016-03-01 | 0 |
| 3 | 4 | 2016-07-03 | 5 |

- **Output:** `[["2016-03-01",2,0.50],["2017-06-25",1,0.00]]`

| install_dt | installs | Day1_retention |
|---|---:|---:|
| 2016-03-01 | 2 | 0.50 |
| 2017-06-25 | 1 | 0.00 |

- **Explanation:** Players 1 and 3 both installed on `2016-03-01`, but only player 1 returned on `2016-03-02`; that cohort's retention is therefore $1 / 2 = 0.50$. Player 2 installed on `2017-06-25` and did not return on `2017-06-26`, so that cohort's retention is $0 / 1 = 0.00$.
