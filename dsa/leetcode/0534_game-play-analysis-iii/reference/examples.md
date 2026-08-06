## Examples

**Example 1**

- Input: `Activity = [[1,2,"2016-03-01",5],[1,2,"2016-05-02",6],[1,3,"2017-06-25",1],[3,1,"2016-03-02",0],[3,4,"2018-07-03",5]]`

| player_id | device_id | event_date | games_played |
|---:|---:|---|---:|
| 1 | 2 | 2016-03-01 | 5 |
| 1 | 2 | 2016-05-02 | 6 |
| 1 | 3 | 2017-06-25 | 1 |
| 3 | 1 | 2016-03-02 | 0 |
| 3 | 4 | 2018-07-03 | 5 |

- Output: `[[1,"2016-03-01",5],[1,"2016-05-02",11],[1,"2017-06-25",12],[3,"2016-03-02",0],[3,"2018-07-03",5]]`

| player_id | event_date | games_played_so_far |
|---:|---|---:|
| 1 | 2016-03-01 | 5 |
| 1 | 2016-05-02 | 11 |
| 1 | 2017-06-25 | 12 |
| 3 | 2016-03-02 | 0 |
| 3 | 2018-07-03 | 5 |

- **Explanation:** Player `1` has played `5 + 6 = 11` games through `2016-05-02` and `5 + 6 + 1 = 12` through
  `2017-06-25`. Player `3` has played `0 + 5 = 5` games through `2018-07-03`. Only dates on which a player logged in
  produce result rows.
