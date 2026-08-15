### 1. Description

Table: `Sales`

```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| sale_id      | int     |
| product_name | varchar |
| sale_date    | date    |
+--------------+---------+
sale_id is the column with unique values for this table.
Each row of this table contains the product name and the date it was sold.
```

Since table Sales was filled manually in the year `2000`, $\text{product}_{name}$ may contain leading and/or trailing white spaces, also they are case-insensitive.

Write a solution to report

- $\text{product}_{name}$ in lowercase without leading or trailing white spaces.

- $\text{sale}_{date}$ in the format `('YYYY-MM')`.

- `total` the number of times the product was sold in this month.

Return the result table ordered by $\text{product}_{name}$ in **ascending order**. In case of a tie, order it by $\text{sale}_{date}$ in **ascending order**.

The result format is in the following example.

### 2. Function Contract

**Inputs**

- `Sales`: A table with columns $\text{sale}_{id}$ (int), $\text{product}_{name}$ (varchar), $\text{sale}_{date}$ (date).

**Return value**

Return a table with columns $\text{product}_{name}$ (varchar), $\text{sale}_{date}$ (varchar `YYYY-MM`), and `total` (int). Results must be grouped by normalized $\text{product}_{name}$ and $\text{sale}_{date}$ month, and ordered ascending by $\text{product}_{name}$ then $\text{sale}_{date}$.

### 3. Examples

#### Example 1

```
- **Input:** 
Sales table:
+---------+--------------+------------+
| sale_id | product_name | sale_date  |
+---------+--------------+------------+
| 1       | LCPHONE      | 2000-01-16 |
| 2       | LCPhone      | 2000-01-17 |
| 3       | LcPhOnE      | 2000-02-18 |
| 4       | LCKeyCHAiN   | 2000-02-19 |
| 5       | LCKeyChain   | 2000-02-28 |
| 6       | Matryoshka   | 2000-03-31 |
+---------+--------------+------------+
- **Output:** 
+--------------+-----------+-------+
| product_name | sale_date | total |
+--------------+-----------+-------+
| lckeychain   | 2000-02   | 2     |
| lcphone      | 2000-01   | 2     |
| lcphone      | 2000-02   | 1     |
| matryoshka   | 2000-03   | 1     |
+--------------+-----------+-------+
- **Explanation:** In January, 2 LcPhones were sold. Please note that the product names are not case sensitive and may contain spaces.
In February, 2 LCKeychains and 1 LCPhone were sold.
In March, one matryoshka was sold.
```
