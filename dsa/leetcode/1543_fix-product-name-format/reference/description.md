## Description

The `Sales` table records individual sales with a unique sale identifier, a product name, and a sale date. Product names are case-insensitive and may contain spaces at the beginning or end, so differently written values can denote the same product.

Normalize every product name by trimming its surrounding spaces and converting it to lowercase. Combine all sales for the same normalized product and calendar month, report the month in `YYYY-MM` form, and return the number of sales in each group. Sort the result first by normalized product name and then by month, both in ascending order.
