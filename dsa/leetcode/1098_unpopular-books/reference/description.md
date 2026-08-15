### 1. Description

Table: `Books`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| book_id        | int     |
| name           | varchar |
| available_from | date    |
+----------------+---------+
book_id is the primary key (column with unique values) of this table.
```

Table: `Orders`

```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| order_id       | int     |
| book_id        | int     |
| quantity       | int     |
| dispatch_date  | date    |
+----------------+---------+
order_id is the primary key (column with unique values) of this table.
book_id is a foreign key (reference column) to the Books table.
```

Write a solution to report the **books** that have sold **less than **`10` copies in the last year, excluding books that have been available for less than one month from today. **Assume today is **`2019-06-23`.

Return the result table in **any order**.

The result format is in the following example.

### 2. Function Contract

**Input tables**

- $Books(\text{book}_{id}, name, \text{available}_{from})$: the uniquely identified books and their availability dates.
- $Orders(\text{order}_{id}, \text{book}_{id}, quantity, \text{dispatch}_{date})$: uniquely identified orders whose $\text{book}_{id}$ values reference `Books`.

Let $B$ and $O$ be the numbers of rows in `Books` and `Orders`. A book is old enough when $\text{available}_{from} \le '2019-05-23'$. For such a book, its last-year sales are the sum of `quantity` over orders whose $\text{dispatch}_{date}$ lies in the closed interval from `2018-06-23` to `2019-06-23`. Orders before or after that interval do not contribute.

**Return value**

- $\text{book}_{id}$: the identifier of a sufficiently old book whose last-year quantity total is strictly less than 10.
- `name`: that book's name.

Return each qualifying book once, in any order. A qualifying book without an order in the interval has total zero. If no book qualifies, the result is empty.

### 3. Examples

#### Example 1

```
- **Input:** 
Books table:
+---------+--------------------+----------------+
| book_id | name               | available_from |
+---------+--------------------+----------------+
| 1       | "Kalila And Demna" | 2010-01-01     |
| 2       | "28 Letters"       | 2012-05-12     |
| 3       | "The Hobbit"       | 2019-06-10     |
| 4       | "13 Reasons Why"   | 2019-06-01     |
| 5       | "The Hunger Games" | 2008-09-21     |
+---------+--------------------+----------------+
Orders table:
+----------+---------+----------+---------------+
| order_id | book_id | quantity | dispatch_date |
+----------+---------+----------+---------------+
| 1        | 1       | 2        | 2018-07-26    |
| 2        | 1       | 1        | 2018-11-05    |
| 3        | 3       | 8        | 2019-06-11    |
| 4        | 4       | 6        | 2019-06-05    |
| 5        | 4       | 5        | 2019-06-20    |
| 6        | 5       | 9        | 2009-02-02    |
| 7        | 5       | 8        | 2010-04-13    |
+----------+---------+----------+---------------+
- **Output:** 
+-----------+--------------------+
| book_id   | name               |
+-----------+--------------------+
| 1         | "Kalila And Demna" |
| 2         | "28 Letters"       |
| 5         | "The Hunger Games" |
+-----------+--------------------+
```
