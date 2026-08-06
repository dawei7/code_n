## Description

Table: `stores`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| store_id    | int     |
| store_name  | varchar |
| location    | varchar |
+-------------+---------+
store_id is the unique identifier for this table.
Each row contains information about a store and its location.

```

Table: `inventory`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| inventory_id| int     |
| store_id    | int     |
| product_name| varchar |
| quantity    | int     |
| price       | decimal |
+-------------+---------+
inventory_id is the unique identifier for this table.
Each row represents the inventory of a specific product at a specific store.

```

Write a solution to find stores that have **inventory imbalance** - stores where the most expensive product has lower stock than the cheapest product.

<ul>
	<li>For each store, identify the **most expensive product** (highest price) and its quantity</li>
	<li>For each store, identify the **cheapest product** (lowest price) and its quantity</li>
	<li>A store has inventory imbalance if the most expensive product's quantity is **less than** the cheapest product's quantity</li>
	<li>Calculate the **imbalance ratio** as (cheapest_quantity / most_expensive_quantity)</li>
	<li>**Round** the imbalance ratio to **2** decimal places</li>
	<li>Only include stores that have **at least **`3`** different products**</li>
</ul>

Return *the result table ordered by imbalance ratio in **descending** order, then by store name in **ascending** order*.

The result format is in the following example.
