## Sales Table

| Column Name | Type |
|---|---|
| `product_id` | int |
| `period_start` | date |
| `period_end` | date |
| `average_daily_sales` | int |

`product_id` is the table's primary key, so a product has at most one row in `Sales`. The dates `period_start` and `period_end` are both included in the sales period. Throughout that interval, `average_daily_sales` is the product's daily sales amount. Every sales date lies in calendar years 2018 through 2020.
