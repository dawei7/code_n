## Examples

**Example 1**

- Input: `Users = [[1,"2019-01-01","Lenovo"],[2,"2019-02-09","Samsung"],[3,"2019-01-19","LG"],[4,"2019-05-21","HP"]], Orders = [[1,"2019-08-01",4,1,2],[2,"2019-08-02",2,1,3],[3,"2019-08-03",3,2,3],[4,"2019-08-04",1,4,2],[5,"2019-08-04",1,3,4],[6,"2019-08-05",2,2,4]], Items = [[1,"Samsung"],[2,"Lenovo"],[3,"LG"],[4,"HP"]]`
- Output: `[[1,"no"],[2,"yes"],[3,"yes"],[4,"no"]]`

`Users`

| user_id | join_date | favorite_brand |
|---:|---|---|
| 1 | 2019-01-01 | Lenovo |
| 2 | 2019-02-09 | Samsung |
| 3 | 2019-01-19 | LG |
| 4 | 2019-05-21 | HP |

`Orders`

| order_id | order_date | item_id | buyer_id | seller_id |
|---:|---|---:|---:|---:|
| 1 | 2019-08-01 | 4 | 1 | 2 |
| 2 | 2019-08-02 | 2 | 1 | 3 |
| 3 | 2019-08-03 | 3 | 2 | 3 |
| 4 | 2019-08-04 | 1 | 4 | 2 |
| 5 | 2019-08-04 | 1 | 3 | 4 |
| 6 | 2019-08-05 | 2 | 2 | 4 |

`Items`

| item_id | item_brand |
|---:|---|
| 1 | Samsung |
| 2 | Lenovo |
| 3 | LG |
| 4 | HP |

Output:

| seller_id | 2nd_item_fav_brand |
|---:|---|
| 1 | no |
| 2 | yes |
| 3 | yes |
| 4 | no |

- Explanation: User 1 receives `no` because that user sold no items. Users 2 and 3 receive `yes` because each user's second sold item has that user's favorite brand. User 4 receives `no` because the second sold item's brand differs from that user's favorite brand.
