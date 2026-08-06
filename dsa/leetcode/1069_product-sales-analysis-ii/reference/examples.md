## Examples

**Example 1**

- **Input:** `Sales = [[1,100,2008,10,5000],[2,100,2009,12,5000],[7,200,2011,15,9000]], Product = [[100,"Nokia"],[200,"Apple"],[300,"Samsung"]]`

`Sales`:

| sale_id | product_id | year | quantity | price |
|---:|---:|---:|---:|---:|
| 1 | 100 | 2008 | 10 | 5000 |
| 2 | 100 | 2009 | 12 | 5000 |
| 7 | 200 | 2011 | 15 | 9000 |

`Product`:

| product_id | product_name |
|---:|---|
| 100 | Nokia |
| 200 | Apple |
| 300 | Samsung |

- **Output:** `[[100,22],[200,15]]`

| product_id | total_quantity |
|---:|---:|
| 100 | 22 |
| 200 | 15 |
