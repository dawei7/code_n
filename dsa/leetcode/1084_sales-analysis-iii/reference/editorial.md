<!-- Don't delete this -->
[TOC]

# Solution

---

## pandas

<!-- h3 for approaches -->
### Approach 1: Filter `sales` and Merge with `product`

<!-- h4 for sections -->
#### Algorithm
The problem asks us to find all products that were sold **only** between `2019-01-01` and `2019-03-31`. This means that, for a given $\text{product}_{id}$, the following two conditions need to hold:
- the earliest date is larger or equal to '2019-01-01', $min(\text{sale}_{date}) \ge '2019-01-01'$
- the latest date is smaller or equal to '2019-03-31', $max(\text{sale}_{date}) \le '2019-03-31'$

Based on the above analysis, we begin by grouping the `sales` table according to the $\text{product}_{id}$ column. Next, we utilize the `filter` function to select groups (product ids) that meet the aforementioned two conditions.
```python
start_time = pd.to_datetime('2019-01-01')
end_time =  pd.to_datetime('2019-03-31')
df = sales.groupby('product_id').filter(lambda x:
    min(x['sale_date']) >= start_time and max(x['sale_date']) <= end_time
)
```
|seller_id|product_id|buyer_id|sale_date|quantity|price|
|---|---|---|---|---|---|
|1|1|1|2019-01-21|2|2000|

<br>

Now, we have a table (data frame) that contains all product ids of our interest but there might be duplicates. Therefore, we use the $\text{drop}_{duplicates}$ function to keep only one record for each $\text{product}_{id}$.
```python
df = df.drop_duplicates(subset = 'product_id')
```

Next, we merge with the `product` table to find the product name for each product id.
```python
df = df.merge(product, left_on = 'product_id', right_on = 'product_id')
```

|seller_id|product_id|buyer_id|sale_date|quantity|price|product_name|unit_price|
|---|---|---|---|---|---|---|---|
|1|1|1|2019-01-21|2|2000|S8|1000|

<br>

Finally, we simply return the $\text{product}_{id}$ and $\text{product}_{name}$ columns from the above table.
```python
return df[['product_id', 'product_name']]
```

<!-- h4 for sections -->
#### Implementation

```python
import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    start_time = pd.to_datetime('2019-01-01')
    end_time = pd.to_datetime('2019-03-31')
    df = sales.groupby('product_id').filter(lambda x:
        min(x['sale_date']) >= start_time and max(x['sale_date']) <= end_time
    )
    df = df.drop_duplicates(subset = 'product_id')
    df = df.merge(product, left_on = 'product_id', right_on = 'product_id')
    return df[['product_id', 'product_name']]
```

<br>
-----

## Database

<!-- h3 for approaches -->
### Approach 1: Group By and Use Having Clause

<!-- h4 for sections -->
#### Algorithm

We first join two tables `sales` and `product` on equal product ids. Then we group the table by the $\text{product}_{id}$ column.

```sql
SELECT DISTINCT p.product_id, p.product_name
FROM Sales s
LEFT JOIN Product p ON p.product_id = s.product_id
GROUP BY p.product_id
```

Note that we need to guarantee there are no duplicates, therefore we use the `SELECT DISTINCT` statement here.

Next, we use the `HAVING` clause to select groups (product ids) of interest that satisfy the following conditions:
- the earliest date is larger or equal to '2019-01-01', $MIN(\text{sale}_{date}) \ge '2019-01-01'$
- the latest date is smaller or equal to '2019-03-31', $MAX(\text{sale}_{date}) \le '2019-03-31'$

```sql
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31';
```

<!-- h4 for sections -->
#### Implementation

```sql
SELECT DISTINCT p.product_id, p.product_name
FROM Sales s
LEFT JOIN Product p ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31';
```

<br>