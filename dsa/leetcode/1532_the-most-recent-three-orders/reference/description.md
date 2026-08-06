## Description

The `Customers` table identifies customers by ID and name. The `Orders` table records an order ID, date, customer ID, and cost, with at most one order for a given customer on any one day.

For each customer who has placed orders, return their three most recent orders. If that customer has fewer than three orders, return every one of them. The result contains the customer name and ID together with the order ID and order date; cost is not returned.

Order the result first by `customer_name` in ascending order, then by `customer_id` in ascending order when names tie, and finally by `order_date` in descending order for the same customer.
