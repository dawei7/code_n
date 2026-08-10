​
<!-- Don't delete this -->
​
# Solution
​
---
​
## pandas

<!-- h3 for approaches -->
### Approach: Get Aggregated Sum by Using groupby and sum()

<!-- h4 for sections -->
#### Algorithm

<!-- Describe your approach to solving the problem. -->
To get the total quantity sold for every product id, we need the two columns `quantity` and $\text{product}_{id}$, and both of them are stored in the DataFrame `sales`. Since one $\text{product}_{id}$ might have multiple sales records, we need to calculate the aggregated sum of `quantity` for each $\text{product}_{id}$.

```python
pd = sales.groupby(['product_id'], as_index = False)['quantity'].sum()
```

In the code above, we pass the parameter [as_index](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) so it will return an object with group labels ($\text{product}_{id}$) as the index.

Now there is only one step left from the final output. We want to update the column name from `quantity` to $\text{total}_{quantity}$ as per requested. Here we use the function [rename](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) to achieve this.

```python
pd = sales.groupby(['product_id'], as_index = False)['quantity'].sum().rename(columns = {'quantity': 'total_quantity'})
```

<!-- h4 for sections -->
#### Implementation

```python
import pandas as pd
​
def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    pd = sales.groupby(['product_id'], as_index = False)['quantity'].sum().rename(columns = {'quantity': 'total_quantity'})

    return pd
```

----
​
## Database

<!-- h3 for approaches -->
### Approach: Get Aggregated Sum by Using GROUP BY and SUM()

<!-- h4 for sections -->
#### Algorithm​
<!-- Describe your approach to solving the problem. -->
To get the total quantity sold for every product id, we need the two columns `quantity` and $\text{product}_{id}$. Since both are stored in the table `Sales`, we only need to use this one table and calculate the aggregated sum of `quantity` for each $\text{product}_{id}$. To get the final output, we also need to rename the column name to $\text{total}_{quantity}$.
​
<!-- h4 for sections -->
#### Implementation

```sql
SELECT product_id,
       SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id
```
​
<!-- an empty line to separate approaches -->
<br>