## Function Contract

**Inputs**

- `Customers`: Table with columns `customer_id` (int), `customer_name` (varchar).

**Return value**

Return a table with single column `ids` (int) containing all missing integers in $[1, \max(\text{customer\_id})]$ sorted ascending.
