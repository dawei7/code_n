## Examples

**Example 1**

- **Input:** `Product = [[1,"LC Phone"],[2,"LC T-Shirt"],[3,"LC Keychain"]], Sales = [[1,"2019-01-25","2019-02-28",100],[2,"2018-12-01","2020-01-01",10],[3,"2019-12-01","2020-01-31",1]]`

`Product`:

| product_id | product_name |
|---:|---|
| 1 | LC Phone |
| 2 | LC T-Shirt |
| 3 | LC Keychain |

`Sales`:

| product_id | period_start | period_end | average_daily_sales |
|---:|---|---|---:|
| 1 | 2019-01-25 | 2019-02-28 | 100 |
| 2 | 2018-12-01 | 2020-01-01 | 10 |
| 3 | 2019-12-01 | 2020-01-31 | 1 |

- **Output:** `[[1,"LC Phone","2019",3500],[2,"LC T-Shirt","2018",310],[2,"LC T-Shirt","2019",3650],[2,"LC T-Shirt","2020",10],[3,"LC Keychain","2019",31],[3,"LC Keychain","2020",31]]`

| product_id | product_name | report_year | total_amount |
|---:|---|---:|---:|
| 1 | LC Phone | 2019 | 3500 |
| 2 | LC T-Shirt | 2018 | 310 |
| 2 | LC T-Shirt | 2019 | 3650 |
| 2 | LC T-Shirt | 2020 | 10 |
| 3 | LC Keychain | 2019 | 31 |
| 3 | LC Keychain | 2020 | 31 |

- **Explanation:** LC Phone is sold for 35 days in 2019, contributing `35 * 100 = 3500`. LC T-Shirt contributes 31 days in 2018, 365 days in 2019, and one day in 2020, for totals of `310`, `3650`, and `10`. LC Keychain contributes 31 days in December 2019 and 31 days in January 2020, producing `31` in each year.
