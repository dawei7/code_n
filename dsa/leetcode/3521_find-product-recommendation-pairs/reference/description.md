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
(user_id, product_id) is the unique key for this table.
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
product_id is the primary key for this table.
Each row assigns a category and price to a product.

```

Amazon wants to implement the **Customers who bought this also bought...** feature based on **co-purchase patterns**. Write a solution to :

<ol>
	<li>Identify **distinct** product pairs frequently **purchased together by the same customers** (where `product1_id` < `product2_id`)</li>
	<li>For **each product pair**, determine how many customers purchased **both** products</li>
</ol>

**A product pair **is considered for recommendation **if** **at least** `3` **different** customers have purchased **both products**.

Return *the **result table ordered by **customer_count** in **descending** order, and in case of a tie, by *`product1_id`* in **ascending** order, and then by *`product2_id`* in **ascending** order*.

The result format is in the following example.
