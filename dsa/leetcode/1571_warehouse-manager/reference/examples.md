## Examples

**Example 1**

- **Input:** `Warehouse = [["LCHouse1", 1, 1], ["LCHouse1", 2, 10], ["LCHouse1", 3, 5], ["LCHouse2", 1, 2], ["LCHouse2", 2, 2], ["LCHouse3", 4, 1]], Products = [[1, "LC-TV", 5, 50, 40], [2, "LC-KeyChain", 5, 5, 5], [3, "LC-Phone", 2, 10, 10], [4, "LC-T-Shirt", 4, 10, 20]]`

`Warehouse` table:

| name | product_id | units |
|---|---:|---:|
| LCHouse1 | 1 | 1 |
| LCHouse1 | 2 | 10 |
| LCHouse1 | 3 | 5 |
| LCHouse2 | 1 | 2 |
| LCHouse2 | 2 | 2 |
| LCHouse3 | 4 | 1 |

`Products` table:

| product_id | product_name | Width | Length | Height |
|---:|---|---:|---:|---:|
| 1 | LC-TV | 5 | 50 | 40 |
| 2 | LC-KeyChain | 5 | 5 | 5 |
| 3 | LC-Phone | 2 | 10 | 10 |
| 4 | LC-T-Shirt | 4 | 10 | 20 |

- **Output:** `[["LCHouse1", 12250], ["LCHouse2", 20250], ["LCHouse3", 800]]`

| warehouse_name | volume |
|---|---:|
| LCHouse1 | 12250 |
| LCHouse2 | 20250 |
| LCHouse3 | 800 |

- **Explanation:**
  - `LCHouse1`: $1 \times (5 \times 50 \times 40) + 10 \times (5 \times 5 \times 5) + 5 \times (2 \times 10 \times 10) = 10000 + 1250 + 1000 = 12250$.
  - `LCHouse2`: $2 \times 10000 + 2 \times 125 = 20000 + 250 = 20250$.
  - `LCHouse3`: $1 \times (4 \times 10 \times 20) = 800$.

**Example 2**

- **Input:** `Warehouse = [["A", 1, 3]], Products = [[1, "ProductA", 2, 3, 4]]`
- **Output:** `[["A", 72]]`

- **Explanation:** Unit volume is $2 \times 3 \times 4 = 24$. For 3 units, total volume is $3 \times 24 = 72$.

**Example 3**

- **Input:** `two warehouses storing different quantities of the same product`
- **Output:** `one independently calculated volume row for each warehouse`

- **Explanation:** Volumes are calculated and grouped independently per warehouse.
