## Function Contract

**Inputs**

- `operations`: A list that begins with `"OrderManagementSystem"` and then contains method names from `"addOrder"`, `"modifyOrder"`, `"cancelOrder"`, and `"getOrdersAtPrice"`.
- `arguments`: A parallel list containing the arguments for each construction or method call.

The app adapter constructs one stateful system and applies the operations in order. Each `modifyOrder` and `cancelOrder` call refers to an order that currently exists and is active. Modification changes the price but preserves the order's original type.

Let $Q$ be the number of method calls after construction, $A$ the maximum number of simultaneously active orders, and $T$ the total number of IDs contained in all lookup results.

**Return value**

Return one result for every entry in `operations`: `null` for construction and every mutating operation, and a list of matching active IDs for each `getOrdersAtPrice` call. A lookup with no matches contributes an empty list.
