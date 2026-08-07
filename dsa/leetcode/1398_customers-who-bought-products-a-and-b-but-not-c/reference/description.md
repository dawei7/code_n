### 1. Description

Table: `Customers`

```
+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| customer_id         | int     |
| customer_name       | varchar |
+---------------------+---------+
customer_id is the column with unique values for this table.
customer_name is the name of the customer.
```

Table: `Orders`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| product_name  | varchar |
+---------------+---------+
order_id is the column with unique values for this table.
customer_id is the id of the customer who bought the product "product_name".
```

Write a solution to report the customer_id and customer_name of customers who bought products **"A"**, **"B"** but did not buy the product **"C"** since we want to recommend them to purchase this product.

Return the result table **ordered** by $\text{customer}_{id}$.

The result format is in the following example.

### 2. Function Contract

**Inputs**

- $Customers(\text{customer}_{id}, \text{customer}_{name})$ contains $C$ customer rows, with unique $\text{customer}_{id}$ values.
- $Orders(\text{order}_{id}, \text{customer}_{id}, \text{product}_{name})$ contains $O$ purchase rows, with unique $\text{order}_{id}$ values.

**Return value**

Return exactly the columns $\text{customer}_{id}$ and $\text{customer}_{name}$. A customer qualifies if and only if all three conditions hold:

- at least one of that customer's orders has $\text{product}_{name} = "A"$;
- at least one has $\text{product}_{name} = "B"$;
- none has $\text{product}_{name} = "C"$.

Other product names and repeated purchases do not change those presence conditions. Customers without orders or without either required product do not qualify. Order the result rows by $\text{customer}_{id}$. Let $R$ be the number of qualifying customers.

### 3. Examples

#### Example 1

```
**Input:**
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Diana         |
| 3           | Elizabeth     |
| 4           | Jhon          |
+-------------+---------------+
Orders table:
+------------+--------------+---------------+
| order_id   | customer_id  | product_name  |
+------------+--------------+---------------+
| 10         |     1        |     A         |
| 20         |     1        |     B         |
| 30         |     1        |     D         |
| 40         |     1        |     C         |
| 50         |     2        |     A         |
| 60         |     3        |     A         |
| 70         |     3        |     B         |
| 80         |     3        |     D         |
| 90         |     4        |     C         |
+------------+--------------+---------------+
**Output:**
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 3           | Elizabeth     |
+-------------+---------------+
**Explanation:** Only the customer_id with id 3 bought the product A and B but not the product C.
```