
<!-- Don't delete this -->

# Solution

---

## pandas

<!-- h3 for approaches -->
### Approach: rank() First and Build the Condition Using np.where()

<!-- h4 for sections -->
#### Algorithm

To later decide whether the brand of the second item sold by each user is their favorite brand, we first need to rank the orders for each seller by $\text{order}_{date}$ and then identify the second item.

```python
orders["rank"] = orders.groupby("seller_id")["order_date"].rank()
```

We then join the updated `orders` table to the `items` table on $\text{item}_{id}$ to get the $\text{item}_{brand}$.

```python
orders_and_items = orders.merge(items, on = 'item_id')
```

Since we only need to compare the $\text{item}_{brand}$ of the second order sold with the $\text{favorite}_{brand}$ of each user, we filter the DataFrame to only the second order.

```python
second_item = orders_and_items[orders_and_items['rank'] == 2]
```

We then merge the DataFrame `users` with the resulting DataFrame $\text{second}_{item}$ to compare the $\text{item}_{brand}$ with the $\text{favorite}_{brand}$ for each user. Since there might be users who don't have a second order, we apply a `left join` to the `users` DataFrame to retain all users, even if they have no matching rows in the $\text{second}_{item}$ DataFrame.

```python
users_and_second_item = users.merge(second_item, left_on = 'user_id', right_on = 'seller_id', how = 'left')
```

Here we can apply a lambda function to establish the condition: when $\text{item}_{brand}$ is equivalent to $\text{favorite}_{brand}$, the function yields `yes`; otherwise (in cases of non-matches or null results), the function yields `no` instead.

```python
users_and_second_item['2nd_item_fav_brand'] = (users_and_second_item['favorite_brand'] == users_and_second_item['item_brand']).apply(lambda x: 'yes' if x else 'no')
```

Lastly, we select the columns needed for the final output and modify the column name as per request.

```python
final_output = users_and_second_item[['user_id', '2nd_item_fav_brand']].rename(columns = {'user_id': 'seller_id'})
```

<!-- h4 for sections -->
#### Implementation

```python
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:

    orders["rank"] = orders.groupby("seller_id")["order_date"].rank()

    orders_and_items = orders.merge(items, on = 'item_id')

    second_item = orders_and_items[orders_and_items['rank'] == 2]

    users_and_second_item = users.merge(second_item, left_on = 'user_id', right_on = 'seller_id', how = 'left')

    users_and_second_item['2nd_item_fav_brand'] = (users_and_second_item['favorite_brand'] == users_and_second_item['item_brand']).apply(lambda x: 'yes' if x else 'no')

    final_output = users_and_second_item[['user_id', '2nd_item_fav_brand']].rename(columns= {'user_id': 'seller_id'})

    return final_output
```

---


## Database
<!-- h3 for approaches -->
### Approach: Using Window Function to Rank
<!-- h4 for sections -->
#### Algorithm
<!-- Describe your approach to solving the problem. -->
Firstly, we want to find the second order for each seller by ranking $\text{order}_{date}$ by each $\text{seller}_{id}$ using `RANK()` in a subquery.

```sql
SELECT seller_id,
       item_id,
       RANK() OVER (PARTITION BY seller_id ORDER BY order_date ASC) AS rnk
FROM Orders
```

We then select the $\text{item}_{brand}$ from the `Items` table to the subquery created earlier to later compare it with the $\text{favorite}_{brand}$ for each user. We also filter to only the second order since that's all we need for the comparison.

```sql
SELECT a.seller_id, a.item_id, i.item_brand
FROM (
    SELECT seller_id,
           item_id,
           RANK() OVER (PARTITION BY seller_id ORDER BY order_date ASC) AS rnk
    FROM Orders) a
JOIN Items i
ON a.item_id = i.item_id
WHERE a.rnk = 2
```

Lastly, we select $\text{user}_{id}$ from the `Users` table and `LEFT JOIN` the subquery created in the previous step on the $\text{user}_{id}$ so the final output will include all users. The condition is built using `CASE WHEN` so only the matched records ($\text{favorite}_{brand}$ = $\text{item}_{brand}$) will return `yes`, and all the other scenarios, not matched or null results (for users who don't have a second order), will return `no` instead. The column names are also updated accordingly.

<!-- h4 for sections -->
#### Implementation

```sql
SELECT u.user_id AS seller_id,
       CASE WHEN u.favorite_brand = b.item_brand THEN 'yes' ELSE 'no' END AS 2nd_item_fav_brand
FROM Users u
LEFT JOIN(
    SELECT a.seller_id, a.item_id, i.item_brand
    FROM (
        SELECT seller_id,
               item_id,
               RANK() OVER (PARTITION BY seller_id ORDER BY order_date ASC) AS rnk
        FROM Orders) a
    JOIN Items i
    ON a.item_id = i.item_id
    WHERE a.rnk = 2) b
ON u.user_id = b.seller_id
```

<!-- an empty line to separate approaches -->
<br>