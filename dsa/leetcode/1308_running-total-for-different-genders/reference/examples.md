## Examples

**Example 1**

- **Input:** `Scores = [["Aron","F","2020-01-01",17],["Alice","F","2020-01-07",23],["Bajrang","M","2020-01-07",7],["Khali","M","2019-12-25",11],["Slaman","M","2019-12-30",13],["Joe","M","2019-12-31",3],["Jose","M","2019-12-18",2],["Priya","F","2019-12-31",23],["Priyanka","F","2019-12-30",17]]`

`Scores`:

| player_name | gender | day | score_points |
|---|:---:|:---:|---:|
| Aron | F | 2020-01-01 | 17 |
| Alice | F | 2020-01-07 | 23 |
| Bajrang | M | 2020-01-07 | 7 |
| Khali | M | 2019-12-25 | 11 |
| Slaman | M | 2019-12-30 | 13 |
| Joe | M | 2019-12-31 | 3 |
| Jose | M | 2019-12-18 | 2 |
| Priya | F | 2019-12-31 | 23 |
| Priyanka | F | 2019-12-30 | 17 |

- **Output:** `[["F","2019-12-30",17],["F","2019-12-31",40],["F","2020-01-01",57],["F","2020-01-07",80],["M","2019-12-18",2],["M","2019-12-25",13],["M","2019-12-30",26],["M","2019-12-31",29],["M","2020-01-07",36]]`

Result:

| gender | day | total |
|:---:|:---:|---:|
| F | 2019-12-30 | 17 |
| F | 2019-12-31 | 40 |
| F | 2020-01-01 | 57 |
| F | 2020-01-07 | 80 |
| M | 2019-12-18 | 2 |
| M | 2019-12-25 | 13 |
| M | 2019-12-30 | 26 |
| M | 2019-12-31 | 29 |
| M | 2020-01-07 | 36 |

- **Explanation:** For team `F`, Priyanka's 17 points on `2019-12-30` begin the total. Priya adds 23 for a total of 40, Aron adds 17 for 57, and Alice adds 23 for 80. Team `M` starts independently with Jose's 2 points on `2019-12-18`; Khali raises the total to 13, Slaman to 26, Joe to 29, and Bajrang to 36.
