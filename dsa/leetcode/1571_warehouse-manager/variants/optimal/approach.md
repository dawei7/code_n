## General
**Attach dimensions to every inventory row**

Join `Warehouse` to `Products` through `product_id`. The product identifier is the product table's key, so each inventory row receives exactly one width, length, and height. Products without stored units do not enter the result because the inventory table drives the inner join.

**Convert units into occupied volume**

For each joined row, multiply `units * Width * Length * Height`. This accounts for both the volume of one product unit and the number of units stored. Product names do not affect the calculation.

Group these row volumes by `warehouse.name` and sum them. Every inventory row for the same warehouse enters exactly one group, so the sum includes all of that warehouse's stored products once and only once. Alias the grouping key as `warehouse_name` and the aggregate as `volume` to match the required output schema.

## Complexity detail
With the primary-key lookup on `Products.product_id`, attaching product dimensions is linear in the $W$ inventory rows. A portable sort-based grouping costs $O(W \log W)$ time; a database may instead use hash aggregation and approach $O(W)$.

The join and grouping workspace can contain $O(W)$ rows or group state, giving an $O(W)$ auxiliary-space upper bound.

## Alternatives and edge cases
- **Precompute unit product volumes:** a CTE can calculate `Width * Length * Height` once per product before joining. It is equivalent and may improve readability when the value is reused.
- **Correlated warehouse subquery:** select each warehouse name and rescan all inventory rows to compute its volume. This is correct but can require $O(W^2)$ work when many warehouses exist.
- **Join after grouping units:** first sum units by warehouse and product, then join dimensions. The uniqueness of `(name, product_id)` makes that extra grouping unnecessary here.
- **Shared product:** the same dimensions are used independently with each warehouse's own unit count.
- **Multiple products:** their occupied volumes are added, not their raw dimensions or unit counts.
- **Unused product:** a catalog product with no inventory row contributes to no warehouse.
- **Single inventory row:** its warehouse volume is exactly the four-factor product.
- **Product name:** it is descriptive data and is intentionally absent from both calculation and output.
- **Output order:** no ordering is required by the contract.
