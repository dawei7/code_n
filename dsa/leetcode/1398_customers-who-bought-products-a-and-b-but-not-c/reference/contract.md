## Function Contract

**Inputs**

- `Customers(customer_id, customer_name)` contains $C$ customer rows, with unique `customer_id` values.
- `Orders(order_id, customer_id, product_name)` contains $O$ purchase rows, with unique `order_id` values.

**Return value**

Return exactly the columns `customer_id` and `customer_name`. A customer qualifies if and only if all three conditions hold:

- at least one of that customer's orders has `product_name = "A"`;
- at least one has `product_name = "B"`;
- none has `product_name = "C"`.

Other product names and repeated purchases do not change those presence conditions. Customers without orders or without either required product do not qualify. Order the result rows by `customer_id`. Let $R$ be the number of qualifying customers.
