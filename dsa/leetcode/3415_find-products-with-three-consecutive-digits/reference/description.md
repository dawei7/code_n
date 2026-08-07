### 1. Description

Table: `Products`

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| name        | varchar |
+-------------+---------+
product_id is the unique key for this table.
Each row of this table contains the ID and name of a product.
```

Write a solution to find all **products** whose names contain a **sequence of exactly three consecutive digits in a row**.

Return *the result table ordered by* $\text{product}_{id}$ *in **ascending** order.*

The result format is in the following example.

### 2. Function Contract

- Refer to method signature.

### 3. Note

that the name may contain multiple such sequences, but each should have length three.

**Example:**

<div class="example-block">
**Input:**

products table:

```
+-------------+--------------------+
| product_id  | name               |
+-------------+--------------------+
| 1           | ABC123XYZ          |
| 2           | A12B34C            |
| 3           | Product56789       |
| 4           | NoDigitsHere       |
| 5           | 789Product         |
| 6           | Item003Description |
| 7           | Product12X34       |
+-------------+--------------------+
```

**Output:**

```
+-------------+--------------------+
| product_id  | name               |
+-------------+--------------------+
| 1           | ABC123XYZ          |
| 5           | 789Product         |
| 6           | Item003Description |
+-------------+--------------------+
```

**Explanation:**

- Product 1: ABC123XYZ contains the digits 123.

- Product 5: 789Product contains the digits 789.

- Product 6: Item003Description contains 003, which is exactly three digits.

### 4. Note

- Results are ordered by $\text{product}_{id}$ in ascending order.

- Only products with exactly three consecutive digits in their names are included in the result.

</div>