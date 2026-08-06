## Description

Table: `Sales`

```

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
Each row records a sale of a product in a given year.
A product may have multiple sales entries in the same year.
Note that the per-unit price.

```

Write a solution to find all sales that occurred in the <strong data-end="967" data-start="953">first year</strong> each product was sold.

<ul data-end="1234" data-start="992">
	<li data-end="1078" data-start="992">
	<p data-end="1078" data-start="994">For each <code data-end="1015" data-start="1003">product_id</code>, identify the earliest <code data-end="1045" data-start="1039">year</code> it appears in the <code data-end="1071" data-start="1064">Sales</code> table.

	</li>
	<li data-end="1140" data-start="1079">
	<p data-end="1140" data-start="1081">Return <strong data-end="1095" data-start="1088">all</strong> sales entries for that product in that year.

	</li>
</ul>

<p data-end="1234" data-start="1143">Return a table with the following columns: **product_id**,** first_year**, **quantity, **and** price**.

Return the result in any order.
