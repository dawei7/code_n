## Description

Table: `sales`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_id       | int     |
| product_id    | int     |
| sale_date     | date    |
| quantity      | int     |
| price         | decimal |
+---------------+---------+
sale_id is the unique identifier for this table.
Each row contains information about a product sale including the product_id, date of sale, quantity sold, and price per unit.

```

Table: `products`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| category      | varchar |
+---------------+---------+
product_id is the unique identifier for this table.
Each row contains information about a product including its name and category.

```

Write a solution to find the most popular product category for each season. The seasons are defined as:

<ul>
	<li>**Winter**: December, January, February</li>
	<li>**Spring**: March, April, May</li>
	<li>**Summer**: June, July, August</li>
	<li>**Fall**: September, October, November</li>
</ul>

The **popularity** of a **category** is determined by the **total quantity sold** in that **season**. If there is a **tie**, select the category with the highest **total revenue** (`quantity × price`). If there is still a tie, return the lexicographically smaller category.

Return *the result table ordered by season in **ascending** order*.

The result format is in the following example.
