## Examples

**Example 1**

- **Input:** `Countries = [[2,"USA"],[3,"Australia"],[7,"Peru"],[5,"China"],[8,"Morocco"],[9,"Spain"]], Weather = [[2,15,"2019-11-01"],[2,12,"2019-10-28"],[2,12,"2019-10-27"],[3,-2,"2019-11-10"],[3,0,"2019-11-11"],[3,3,"2019-11-12"],[5,16,"2019-11-07"],[5,18,"2019-11-09"],[5,21,"2019-11-23"],[7,25,"2019-11-28"],[7,22,"2019-12-01"],[7,20,"2019-12-02"],[8,25,"2019-11-05"],[8,27,"2019-11-15"],[8,31,"2019-11-25"],[9,7,"2019-10-23"],[9,3,"2019-12-23"]]`

`Countries`:

| country_id | country_name |
|---:|---|
| 2 | USA |
| 3 | Australia |
| 7 | Peru |
| 5 | China |
| 8 | Morocco |
| 9 | Spain |

`Weather`:

| country_id | weather_state | day |
|---:|---:|---|
| 2 | 15 | 2019-11-01 |
| 2 | 12 | 2019-10-28 |
| 2 | 12 | 2019-10-27 |
| 3 | -2 | 2019-11-10 |
| 3 | 0 | 2019-11-11 |
| 3 | 3 | 2019-11-12 |
| 5 | 16 | 2019-11-07 |
| 5 | 18 | 2019-11-09 |
| 5 | 21 | 2019-11-23 |
| 7 | 25 | 2019-11-28 |
| 7 | 22 | 2019-12-01 |
| 7 | 20 | 2019-12-02 |
| 8 | 25 | 2019-11-05 |
| 8 | 27 | 2019-11-15 |
| 8 | 31 | 2019-11-25 |
| 9 | 7 | 2019-10-23 |
| 9 | 3 | 2019-12-23 |

- **Output:** `[["USA","Cold"],["Australia","Cold"],["Peru","Hot"],["Morocco","Hot"],["China","Warm"]]`

| country_name | weather_type |
|---|---|
| USA | Cold |
| Australia | Cold |
| Peru | Hot |
| Morocco | Hot |
| China | Warm |

- **Explanation:** USA's sole November value is $15$, so its type is `Cold`. Australia's average is $(-2 + 0 + 3) / 3 = 0.333$, which is also `Cold`. Peru's only qualifying value is $25$, making it `Hot`. China's average is $(16 + 18 + 21) / 3 = 18.333$, so it is `Warm`. Morocco's average is $(25 + 27 + 31) / 3 = 27.667$, making it `Hot`. Spain has no November observation and is therefore absent from the result.
