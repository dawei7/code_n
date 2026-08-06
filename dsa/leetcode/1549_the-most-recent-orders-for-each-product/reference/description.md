## Description

The database contains customers, products, and individual orders. Every order records its date, customer, and product, and a customer cannot order the same product more than once on one day.

For each product that has at least one order, find the latest date on which that product was ordered and return every order placed for it on that date. A product can therefore contribute multiple rows when different customers placed orders on its most recent day. Products with no orders are omitted. Sort the result by product name, then product identifier, then order identifier, all in ascending order.
