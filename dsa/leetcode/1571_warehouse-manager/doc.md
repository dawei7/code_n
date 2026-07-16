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

### Required Complexity

- **Time:** $O(W \log W)$
- **Space:** $O(W)$

<details>
<summary>Approach</summary>

#### General

**Attach dimensions to every inventory row**

Join `Warehouse` to `Products` through `product_id`. The product identifier is the product table's key, so each inventory row receives exactly one width, length, and height. Products without stored units do not enter the result because the inventory table drives the inner join.

**Convert units into occupied volume**

For each joined row, multiply `units * Width * Length * Height`. This accounts for both the volume of one product unit and the number of units stored. Product names do not affect the calculation.

Group these row volumes by `warehouse.name` and sum them. Every inventory row for the same warehouse enters exactly one group, so the sum includes all of that warehouse's stored products once and only once. Alias the grouping key as `warehouse_name` and the aggregate as `volume` to match the required output schema.

#### Complexity detail

With the primary-key lookup on `Products.product_id`, attaching product dimensions is linear in the $W$ inventory rows. A portable sort-based grouping costs $O(W \log W)$ time; a database may instead use hash aggregation and approach $O(W)$.

The join and grouping workspace can contain $O(W)$ rows or group state, giving an $O(W)$ auxiliary-space upper bound.

#### Alternatives and edge cases

- **Precompute unit product volumes:** a CTE can calculate `Width * Length * Height` once per product before joining. It is equivalent and may improve readability when the value is reused.
- **Correlated warehouse subquery:** select each warehouse name and rescan all inventory rows to compute its volume. This is correct but can require $O(W^2)$ work when many warehouses exist.
- **Join after grouping units:** first sum units by warehouse and product, then join dimensions. The uniqueness of `(name, product_id)` makes that extra grouping unnecessary here.
- **Shared product:** the same dimensions are used independently with each warehouse's own unit count.
- **Multiple products:** their occupied volumes are added, not their raw dimensions or unit counts.
- **Unused product:** a catalog product with no inventory row contributes to no warehouse.
- **Single inventory row:** its warehouse volume is exactly the four-factor product.
- **Product name:** it is descriptive data and is intentionally absent from both calculation and output.
- **Output order:** no ordering is required by the contract.

</details>
