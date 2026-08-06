## Description

The `Salesperson` table identifies salespeople, `Customer` assigns each customer to a salesperson, and `Sales` records the price of each sale made by a customer. Calculate each salesperson's influence as the sum of all prices paid by every customer assigned to that salesperson.

Report every salesperson, including those without customers and those whose customers have no recorded sales. Their total must be `0` rather than `NULL`. Return the salesperson identifier, name, and computed total; the problem permits the result rows in any order.
