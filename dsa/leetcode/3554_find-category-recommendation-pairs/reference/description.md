## Description

Table: `ProductPurchases`

```

+-------------+------+
| Column Name | Type | 
+-------------+------+
| user_id     | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(user_id, product_id) is the unique identifier for this table. 
Each row represents a purchase of a product by a user in a specific quantity.

```

Table: `ProductInfo`

```

+-------------+---------+
| Column Name | Type    | 
+-------------+---------+
| product_id  | int     |
| category    | varchar |
| price       | decimal |
+-------------+---------+
product_id is the unique identifier for this table.
Each row assigns a category and price to a product.

```

Amazon wants to understand shopping patterns across product categories. Write a solution to:

<ol>
	<li>Find all **category pairs** (where `category1` < `category2`)</li>
	<li>For **each category pair**, determine the number of **unique** **customers** who purchased products from **both** categories</li>
</ol>

A category pair is considered **reportable** if at least `3` different customers have purchased products from both categories.

Return *the result table of reportable category pairs ordered by **customer_count** in **descending** order, and in case of a tie, by **category1** in **ascending** order lexicographically, and then by **category2** in **ascending** order.*

The result format is in the following example.
