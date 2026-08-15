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
This table can have repeated rows.
product_id is a foreign key (reference column) to the Product table.
Each row of this table contains some information about one sale.
```

Write a solution that reports the best **seller** by total sales price, If there is a tie, report them all.

Return the result table in **any order**.

The result format is in the following example.

### 2. Function Contract

**Input tables**

- $Product(\text{product}_{id}, \text{product}_{name}, \text{unit}_{price})$: the referenced product catalog.
- $Sales(\text{seller}_{id}, \text{product}_{id}, \text{buyer}_{id}, \text{sale}_{date}, quantity, price)$: the sale records to aggregate.

The output grain is one row per seller tied for the greatest sum of `Sales.price`. The sample confirms that `price` is the recorded price for the whole sale: a quantity of `2` for a product with unit price `1000` has $price = 2000$. Therefore, add `price` directly rather than multiplying it by `quantity`. Product names and unit prices do not change the requested total.

Repeated `Sales` rows are permitted and each stored row contributes separately. If `Sales` is empty, there is no represented seller and the result is empty.

**Return value**

- One column named $\text{seller}_{id}$.
- Every represented seller whose sum of `price` is the maximum seller total.
- Result order is unrestricted.

### 3. Examples

#### Example 1

```
- **Input:** 
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
| 2         | 2          | 3        | 2019-06-02 | 1        | 800   |
| 3         | 3          | 4        | 2019-05-13 | 2        | 2800  |
+-----------+------------+----------+------------+----------+-------+
- **Output:** 
+-------------+
| seller_id   |
+-------------+
| 1           |
| 3           |
+-------------+
- **Explanation:** Both sellers with id 1 and 3 sold products with the most total price of 2800.
```
