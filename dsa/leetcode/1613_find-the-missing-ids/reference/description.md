### 1. Description

Table: `Customers`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| customer_name | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
Each row of this table contains the name and the id customer.
```

Write a solution to find the missing customer IDs. The missing IDs are ones that are not in the `Customers` table but are in the range between `1` and the **maximum** $\text{customer}_{id}$ present in the table.

### 2. Function Contract

**Inputs**

- `Customers`: Table with columns $\text{customer}_{id}$ (int), $\text{customer}_{name}$ (varchar).

**Return value**

Return a table with single column `ids` (int) containing all missing integers in $[1, \max(\text{customer\\_id})]$ sorted ascending.

### 3. Notice

that the maximum $\text{customer}_{id}$ will not exceed `100`.

Return the result table ordered by `ids` in **ascending order**.

The result format is in the following example.

### 4. Examples

#### Example 1

```
- **Input:** 
Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Alice         |
| 4           | Bob           |
| 5           | Charlie       |
+-------------+---------------+
- **Output:** 
+-----+
| ids |
+-----+
| 2   |
| 3   |
+-----+
- **Explanation:** The maximum customer_id present in the table is 5, so in the range [1,5], IDs 2 and 3 are missing from the table.
```
