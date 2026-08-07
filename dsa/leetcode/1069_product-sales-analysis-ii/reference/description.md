### 1. Description

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
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
```

Table: `Product`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
```

Write a solution that reports the total quantity sold for every product id.

Return the resulting table in **any order**.

The result format is in the following example.

### 2. Function Contract

**Input tables**

- $Sales(\text{sale}_{id}, \text{product}_{id}, year, quantity, price)$: the sale records whose quantities are aggregated.
- $Product(\text{product}_{id}, \text{product}_{name})$: the referenced product metadata table.

The output grain is one row for each distinct $\text{product}_{id}$ occurring in `Sales`. Product metadata and per-unit price do not change the requested quantity total, and a product with no sale row contributes no output group.

**Return value**

- Columns $\text{product}_{id}$ and $\text{total}_{quantity}$, where $\text{total}_{quantity}$ is the sum of `quantity` over all `Sales` rows for that $\text{product}_{id}$.
- Result order is unrestricted.

### 3. Examples

#### Example 1

```
**Input:**
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
**Output:**
+--------------+----------------+
| product_id   | total_quantity |
+--------------+----------------+
| 100          | 22             |
| 200          | 15             |
+--------------+----------------+
```