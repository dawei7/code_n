# Warehouse Manager

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1571 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/warehouse-manager/) |

## Problem Description
### Goal

The `Warehouse` table records how many units of each product are stored at each warehouse. The `Products` table supplies every product's width, length, and height. One unit occupies the rectangular volume obtained by multiplying those three dimensions.

For every warehouse represented in the inventory table, calculate the total volume occupied by all stored units. Return the warehouse name and its aggregated volume; result rows may appear in any order.

### Function Contract
**Inputs**

- `Warehouse(name, product_id, units)`: $W$ inventory rows. The pair `(name, product_id)` is unique, and `units` is the number of that product stored at the named warehouse.
- `Products(product_id, product_name, Width, Length, Height)`: product records keyed by `product_id`. The three dimensions describe one unit of the product.

**Return value**

Return a table with columns `warehouse_name` and `volume`. For each warehouse name, `volume` is the sum of `units * Width * Length * Height` over its inventory rows.

### Examples
**Example 1**

- Input: three warehouses containing TVs, keychains, phones, and T-shirts in different quantities
- Output: `LCHouse1` has volume `12250`, `LCHouse2` has `20250`, and `LCHouse3` has `800`

**Example 2**

- Input: warehouse `A` stores three units of a `2 × 3 × 4` product
- Output: `(A, 72)`

**Example 3**

- Input: two warehouses store different quantities of the same product
- Output: one independently calculated volume row for each warehouse
