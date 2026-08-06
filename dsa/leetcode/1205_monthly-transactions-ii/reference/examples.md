## Examples

**Example 1**

- Input: `Transactions = [[101,"US","approved",1000,"2019-05-18"],[102,"US","declined",2000,"2019-05-19"],[103,"US","approved",3000,"2019-06-10"],[104,"US","declined",4000,"2019-06-13"],[105,"US","approved",5000,"2019-06-15"]], Chargebacks = [[102,"2019-05-29"],[101,"2019-06-30"],[105,"2019-09-18"]]`
- Output: `[["2019-05","US",1,1000,1,2000],["2019-06","US",2,8000,1,1000],["2019-09","US",0,0,1,5000]]`

`Transactions`

| id | country | state | amount | trans_date |
|---:|---|---|---:|---|
| 101 | US | approved | 1000 | 2019-05-18 |
| 102 | US | declined | 2000 | 2019-05-19 |
| 103 | US | approved | 3000 | 2019-06-10 |
| 104 | US | declined | 4000 | 2019-06-13 |
| 105 | US | approved | 5000 | 2019-06-15 |

`Chargebacks`

| trans_id | trans_date |
|---:|---|
| 102 | 2019-05-29 |
| 101 | 2019-06-30 |
| 105 | 2019-09-18 |

Result:

| month | country | approved_count | approved_amount | chargeback_count | chargeback_amount |
|---|---|---:|---:|---:|---:|
| 2019-05 | US | 1 | 1000 | 1 | 2000 |
| 2019-06 | US | 2 | 8000 | 1 | 1000 |
| 2019-09 | US | 0 | 0 | 1 | 5000 |
