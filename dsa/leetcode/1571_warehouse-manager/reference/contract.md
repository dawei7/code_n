## Function Contract

**Database Schemas**

**`Warehouse`**

| Column | Type | Meaning |
|---|---|---|
| `name` | varchar | Warehouse name; composite key with `product_id`. |
| `product_id` | int | Product identifier. |
| `units` | int | Quantity of product stored at the warehouse. |

**`Products`**

| Column | Type | Meaning |
|---|---|---|
| `product_id` | int | Unique product identifier. |
| `product_name` | varchar | Display name of the product. |
| `Width` | int | Width of one unit of the product. |
| `Length` | int | Length of one unit of the product. |
| `Height` | int | Height of one unit of the product. |

**Return value**

Return columns `warehouse_name` and `volume`. For each warehouse, `volume` is the sum of `units * Width * Length * Height` over all its inventory rows. Row order is unrestricted.
