## Examples

**Example 1**

- Input: `Weather = [[1,"2015-01-01",10],[2,"2015-01-02",25],[3,"2015-01-03",20],[4,"2015-01-04",30]]`

| id | recordDate | temperature |
|---:|---|---:|
| 1 | 2015-01-01 | 10 |
| 2 | 2015-01-02 | 25 |
| 3 | 2015-01-03 | 20 |
| 4 | 2015-01-04 | 30 |

- Output: `id = [2,4]`

| id |
|---:|
| 2 |
| 4 |

- Explanation: January 2 is warmer than January 1 (`10 -> 25`), and January 4 is warmer than January 3 (`20 -> 30`).
