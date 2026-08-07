### 1. Description

Table: `Product`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the name and the price of each product.
```

Table: `Sales`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+
This table might have repeated rows.
product_id is a foreign key (reference column) to the Product table.
buyer_id is never NULL.
sale_date is never NULL.
Each row of this table contains some information about one sale.
```

Write a solution to report the **buyers** who have bought *S8* but not *iPhone*. Note that *S8* and *iPhone* are products presented in the `Product` table.

Return the result table in **any order**.

The result format is in the following example.

### 2. Function Contract

**Input tables**

- $Product(\text{product}_{id}, \text{product}_{name}, \text{unit}_{price})$: the product catalog used to resolve names.
- $Sales(\text{seller}_{id}, \text{product}_{id}, \text{buyer}_{id}, \text{sale}_{date}, quantity, price)$: the purchase history associated with buyers.

The output grain is one row per qualifying $\text{buyer}_{id}$. Eligibility depends only on whether the buyer's joined purchase history contains at least one `S8` name and contains no `iPhone` name. Seller, date, quantity, price, unit price, and purchases of other product names do not alter those two existence conditions.

Repeated `Sales` rows are permitted but do not create repeated output buyers. If `Sales` is empty, or if every buyer either lacks an `S8` purchase or has an `iPhone` purchase, the result is empty.

**Return value**

- One column named $\text{buyer}_{id}$.
- One row for every buyer with at least one `S8` purchase and zero `iPhone` purchases.
- Result order is unrestricted.

### 3. Examples

#### Example 1

```
**Input:**
Product table:
+------------+--------------+------------+
| product_id | product_name | unit_price |
+------------+--------------+------------+
| 1          | S8           | 1000       |
| 2          | G4           | 800        |
| 3          | iPhone       | 1400       |
+------------+--------------+------------+
Sales table:
+-----------+------------+----------+------------+----------+-------+
| seller_id | product_id | buyer_id | sale_date  | quantity | price |
+-----------+------------+----------+------------+----------+-------+
| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
| 2         | 1          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 3        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
**Output:**
+-------------+
| buyer_id    |
+-------------+
| 1           |
+-------------+
**Explanation:** The buyer with id 1 bought an S8 but did not buy an iPhone. The buyer with id 3 bought both.
```