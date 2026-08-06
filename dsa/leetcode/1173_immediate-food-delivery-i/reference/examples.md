## Examples

**Example 1**

- Input: `Delivery = [[1,1,"2019-08-01","2019-08-02"],[2,5,"2019-08-02","2019-08-02"],[3,1,"2019-08-11","2019-08-11"],[4,3,"2019-08-24","2019-08-26"],[5,4,"2019-08-21","2019-08-22"],[6,2,"2019-08-11","2019-08-13"]]`
- Output: `[[33.33]]`

`Delivery`

| delivery_id | customer_id | order_date | customer_pref_delivery_date |
|---:|---:|---|---|
| 1 | 1 | 2019-08-01 | 2019-08-02 |
| 2 | 5 | 2019-08-02 | 2019-08-02 |
| 3 | 1 | 2019-08-11 | 2019-08-11 |
| 4 | 3 | 2019-08-24 | 2019-08-26 |
| 5 | 4 | 2019-08-21 | 2019-08-22 |
| 6 | 2 | 2019-08-11 | 2019-08-13 |

Output:

| immediate_percentage |
|---:|
| 33.33 |

- Explanation: Deliveries `2` and `3` are immediate because their two dates match. The other four are scheduled, so the immediate percentage is $100 \times 2/6$, which rounds to `33.33`.
