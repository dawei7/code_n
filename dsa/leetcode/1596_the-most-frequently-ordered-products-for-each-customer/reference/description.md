## Description

The database contains `Customers`, `Orders`, and `Products`. `Customers` identifies each customer and stores a name. Every row in `Orders` records one order, including its date, customer, and product. `Products` maps each product identifier to its name and price.

For every customer who has placed at least one order, find the product or products appearing most often in that customer's order rows. If several products share the same maximum frequency for one customer, include all of them. Return each qualifying `customer_id` and `product_id` together with the matching `product_name`; customers without orders do not produce a row. Result rows may appear in any order.
