## Examples

**Example 1**

- **Input:** `Customers = [[1,"Daniel"],[2,"Diana"],[3,"Elizabeth"],[4,"Jhon"]], Orders = [[10,1,"A"],[20,1,"B"],[30,1,"D"],[40,1,"C"],[50,2,"A"],[60,3,"A"],[70,3,"B"],[80,3,"D"],[90,4,"C"]]`

`Customers`:

| customer_id | customer_name |
|---:|---|
| 1 | Daniel |
| 2 | Diana |
| 3 | Elizabeth |
| 4 | Jhon |

`Orders`:

| order_id | customer_id | product_name |
|---:|---:|---|
| 10 | 1 | A |
| 20 | 1 | B |
| 30 | 1 | D |
| 40 | 1 | C |
| 50 | 2 | A |
| 60 | 3 | A |
| 70 | 3 | B |
| 80 | 3 | D |
| 90 | 4 | C |

- **Output:** `[[3,"Elizabeth"]]`

| customer_id | customer_name |
|---:|---|
| 3 | Elizabeth |

- **Explanation:** Customer 3 is the only customer whose orders include both A and B while excluding C. Daniel also bought A and B but is disqualified by his C order; Diana bought only A, and Jhon bought C.
