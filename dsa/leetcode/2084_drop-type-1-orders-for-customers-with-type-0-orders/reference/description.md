## Description

The `Orders` table records orders with a unique order identifier, a customer identifier, and an order type that is either 0 or 1.

Report orders customer by customer under one priority rule. If a customer has at least one type 0 order, retain all of that customer's type 0 orders and discard every type 1 order from that customer. If the customer has no type 0 order, retain all of their type 1 orders. Return the selected original rows in any order.
