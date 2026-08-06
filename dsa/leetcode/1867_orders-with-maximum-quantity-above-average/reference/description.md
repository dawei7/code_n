## Description

The `OrdersDetails` table stores the products included in customer orders. An order may contain several products, and each row gives one product's `quantity` within its `order_id`. The pair `(order_id, product_id)` uniquely identifies a row.

For every order, consider both its average product quantity and its largest product quantity. Return the identifiers of the orders whose largest quantity is strictly greater than the average quantity of every order in the table. Equivalently, an order qualifies only when its maximum exceeds the greatest of all per-order averages. The result may be returned in any order.
