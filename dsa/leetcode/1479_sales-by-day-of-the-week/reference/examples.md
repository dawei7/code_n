## Examples

**Example 1**

- **Input:** `Orders = [[1,1,"2020-06-01","1",10],[2,1,"2020-06-08","2",10],[3,2,"2020-06-02","1",5],[4,3,"2020-06-03","3",5],[5,4,"2020-06-04","4",1],[6,4,"2020-06-05","5",5],[7,5,"2020-06-05","1",10],[8,5,"2020-06-14","4",5],[9,5,"2020-06-21","3",5]], Items = [["1","LC Alg. Book","Book"],["2","LC DB. Book","Book"],["3","LC SmarthPhone","Phone"],["4","LC Phone 2020","Phone"],["5","LC SmartGlass","Glasses"],["6","LC T-Shirt XL","T-Shirt"]]`

| order_id | customer_id | order_date | item_id | quantity |
|---:|---:|---|---|---:|
| 1 | 1 | `2020-06-01` | `1` | 10 |
| 2 | 1 | `2020-06-08` | `2` | 10 |
| 3 | 2 | `2020-06-02` | `1` | 5 |
| 4 | 3 | `2020-06-03` | `3` | 5 |
| 5 | 4 | `2020-06-04` | `4` | 1 |
| 6 | 4 | `2020-06-05` | `5` | 5 |
| 7 | 5 | `2020-06-05` | `1` | 10 |
| 8 | 5 | `2020-06-14` | `4` | 5 |
| 9 | 5 | `2020-06-21` | `3` | 5 |

| item_id | item_name | item_category |
|---|---|---|
| `1` | `LC Alg. Book` | `Book` |
| `2` | `LC DB. Book` | `Book` |
| `3` | `LC SmarthPhone` | `Phone` |
| `4` | `LC Phone 2020` | `Phone` |
| `5` | `LC SmartGlass` | `Glasses` |
| `6` | `LC T-Shirt XL` | `T-Shirt` |

- **Output:** `[["Book",20,5,0,0,10,0,0],["Glasses",0,0,0,0,5,0,0],["Phone",0,0,5,1,0,0,10],["T-Shirt",0,0,0,0,0,0,0]]`

| Category | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|---|---:|---:|---:|---:|---:|---:|---:|
| `Book` | 20 | 5 | 0 | 0 | 10 | 0 | 0 |
| `Glasses` | 0 | 0 | 0 | 0 | 5 | 0 | 0 |
| `Phone` | 0 | 0 | 5 | 1 | 0 | 0 | 10 |
| `T-Shirt` | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- **Explanation:** On Monday, `2020-06-01` and `2020-06-08` contribute
  $10+10=20$ Book units from item IDs `1` and `2`. Tuesday contributes `5`
  Book units on `2020-06-02`. Wednesday contributes `5` Phone units on
  `2020-06-03`, and Thursday contributes `1` Phone unit on `2020-06-04`.
  Friday contributes `10` Book units and `5` Glasses units on `2020-06-05`.
  No items were sold on Saturday. On Sunday, `2020-06-14` and `2020-06-21`
  contribute $5+5=10$ Phone units from item IDs `4` and `3`. There are no
  T-shirt sales.
