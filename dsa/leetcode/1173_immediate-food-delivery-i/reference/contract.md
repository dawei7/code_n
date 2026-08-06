## Function Contract

**Input table**

- `Delivery`: Food-delivery orders and their requested dates. Let $n$ be the number of rows in this table.

Classification is per delivery row, even when one customer has placed several orders. Exact date equality is immediate; a preferred date after the order date is scheduled.

**Return value**

Return one row with one column:

- `immediate_percentage`: The number of immediate deliveries divided by $n$, multiplied by $100$, and rounded to two decimal places.
