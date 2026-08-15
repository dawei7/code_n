### 1. Description

Table: `Product`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
+---------------+---------+
product_id is the primary key (column with unique values) for this table.
product_name is the name of the product.
```

Table: `Sales`

```
+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| product_id          | int     |
| period_start        | date    |
| period_end          | date    |
| average_daily_sales | int     |
+---------------------+---------+
product_id is the primary key (column with unique values) for this table.
period_start and period_end indicate the start and end date for the sales period, and both dates are inclusive.
The average_daily_sales column holds the average daily sales amount of the items for the period.
The dates of the sales years are between 2018 to 2020.
```

Write a solution to report the total sales amount of each item for each year, with corresponding $\text{product}_{name}$, $\text{product}_{id}$, $\text{report}_{year}$, and $\text{total}_{amount}$.

Return the result table **ordered** by $\text{product}_{id}$ and $\text{report}_{year}$.

The result format is in the following example.

### 2. Function Contract

**Inputs**

- $Product(\text{product}_{id}, \text{product}_{name})$ contains $P$ products keyed by $\text{product}_{id}$.
- $Sales(\text{product}_{id}, \text{period}_{start}, \text{period}_{end}, average_daily_sales)$ contains $S$ product sales intervals keyed by $\text{product}_{id}$.

Both endpoints of every sales interval count as sales days. The only report years are 2018, 2019, and 2020.

**Return value**

Return a table with these columns:

- $\text{product}_{id}$: the product's primary-key ID.
- $\text{product}_{name}$: the name from the matching `Product` row.
- $\text{report}_{year}$: a year whose closed calendar interval overlaps the product's sales interval.
- $\text{total}_{amount}$: the number of overlapping calendar days multiplied by `average_daily_sales`.

Emit one row for each product-year overlap and no row for a product without a sales interval. Order rows by $\text{product}_{id}$ and then by $\text{report}_{year}$. Let $R$ be the number of returned rows.

### 3. Examples

#### Example 1

```
- **Input:** 
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 1          | LC Phone     |
| 2          | LC T-Shirt   |
| 3          | LC Keychain  |
+------------+--------------+
Sales table:
+------------+--------------+-------------+---------------------+
| product_id | period_start | period_end  | average_daily_sales |
+------------+--------------+-------------+---------------------+
| 1          | 2019-01-25   | 2019-02-28  | 100                 |
| 2          | 2018-12-01   | 2020-01-01  | 10                  |
| 3          | 2019-12-01   | 2020-01-31  | 1                   |
+------------+--------------+-------------+---------------------+
- **Output:** 
+------------+--------------+-------------+--------------+
| product_id | product_name | report_year | total_amount |
+------------+--------------+-------------+--------------+
| 1          | LC Phone     |    2019     | 3500         |
| 2          | LC T-Shirt   |    2018     | 310          |
| 2          | LC T-Shirt   |    2019     | 3650         |
| 2          | LC T-Shirt   |    2020     | 10           |
| 3          | LC Keychain  |    2019     | 31           |
| 3          | LC Keychain  |    2020     | 31           |
+------------+--------------+-------------+--------------+
- **Explanation:** LC Phone was sold for the period of 2019-01-25 to 2019-02-28, and there are 35 days for this period. Total amount 35*100 = 3500.
LC T-shirt was sold for the period of 2018-12-01 to 2020-01-01, and there are 31, 365, 1 days for years 2018, 2019 and 2020 respectively.
LC Keychain was sold for the period of 2019-12-01 to 2020-01-31, and there are 31, 31 days for years 2019 and 2020 respectively.
```
