## Description

The `Transactions` table records each purchase's customer, product, date, and amount. The `Products` table maps every product identifier to a category and listed price. Produce one purchasing-behavior summary for every customer who has a transaction.

For each customer, report the rounded total spend, transaction count, number of distinct purchased categories, and rounded average transaction amount. Also report the category purchased most often; if several categories have the same purchase count, choose the category whose most recent transaction is latest. Compute the loyalty score as transaction count times $10$ plus total spend divided by $100$, rounded to two decimal places.

Order customers by loyalty score descending, breaking equal scores by customer identifier ascending.
