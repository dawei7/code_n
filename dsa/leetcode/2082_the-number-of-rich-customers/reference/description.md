### 1. Description

Table: `Store`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| bill_id     | int  |
| customer_id | int  |
| amount      | int  |
+-------------+------+
bill_id is the primary key (column with unique values) for this table.
Each row contains information about the amount of one bill and the customer associated with it.
```

Write a solution to report the number of customers who had **at least one** bill with an amount **strictly greater** than `500`.

The result format is in the following example.

### 2. Function Contract

**Database Schema**

**`Store`**

| Column | Type | Meaning |
|---|---|---|
| $\text{bill}_{id}$ | int | Unique bill identifier. |
| $\text{customer}_{id}$ | int | Customer identifier. |
| `amount` | int | Amount of the bill. |

**Return value**

Return a single-row table with column $\text{rich}_{count}$. $\text{rich}_{count}$ is the count of distinct $\text{customer}_{id}$ values having at least one bill with `amount > 500`.

### 3. Examples

#### Example 1

```
**Input:**
Store table:
+---------+-------------+--------+
| bill_id | customer_id | amount |
+---------+-------------+--------+
| 6       | 1           | 549    |
| 8       | 1           | 834    |
| 4       | 2           | 394    |
| 11      | 3           | 657    |
| 13      | 3           | 257    |
+---------+-------------+--------+
**Output:**
+------------+
| rich_count |
+------------+
| 2          |
+------------+
**Explanation:**
Customer 1 has two bills with amounts strictly greater than 500.
Customer 2 does not have any bills with an amount strictly greater than 500.
Customer 3 has one bill with an amount strictly greater than 500.
```