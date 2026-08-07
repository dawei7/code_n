[TOC]

## Solution

---

### Overview

We want to find the followers for each user in this problem.
> (user_id, follower_id) is the primary key for this table.

This implies that there will be unique combinations of $\text{user}_{id}$ and $\text{follower}_{id}$ in the table. For example, you cannot have the following table:
```
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
|    1    |      2      |
|    1    |      2      |
+---------+-------------+
```
The same combination of $\text{user}_{id}$ and $\text{follower}_{id}$ cannot occur multiple times.

In the table below, user `1` has three followers.

```
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
|    1    |      2      |
|    1    |      3      |
|    1    |      4      |
|    3    |      2      |
|    3    |      5      |
+---------+-------------+
```

Next, we need to ensure that our output users are ordered by $\text{user}_{id}$ in ascending order.

For the example shared above the output should look like:

```
+---------+-----------------+
| user_id | followers_count |
+---------+-----------------+
|    1    |        3        |
|    3    |        2        |
+---------+-----------------+
```
---

### Approach: `COUNT` and `GROUP BY`

#### Intuition

We essentially need to count the number of times a particular $\text{user}_{id}$ occurs in the $\text{user}_{id}$ column and this count will be equal to the follower count. This is because each $(\text{user}_{id}, \text{follower}_{id})$ combination is unique. We can try to use the `COUNT` function to count the occurences of a single $\text{user}_{id}$. Remember, `COUNT` is an aggregate function, you will have to tell it which field to aggregate by. This can be done using the `GROUP BY` clause. Since we want to print the $\text{user}_{id}$ and its count in the table, we can do $GROUP BY \text{user}_{id}$.

Lastly, we can use the `ORDER BY` clause to order the result by $\text{user}_{id}$.

#### Algorithm

1. $SELECT \text{user}_{id}, COUNT(\text{user}_{id}) AS \text{followers}_{count}$: This part specifies the columns to be selected in the result set. Here, we want to retrieve the $\text{user}_{id}$ and the count of followers for each user. The $COUNT(\text{user}_{id})$ function is used to count the number of rows in the followers table, which represents the number of followers for a particular user. The result of this count is aliased as $\text{followers}_{count}$ to match the output requirements of the problem.

2. `FROM followers`: This part specifies the table from which the data is being retrieved.

3. $GROUP BY \text{user}_{id}$: This part groups the rows based on the $\text{user}_{id}$ column. By using `GROUP BY`, the query will calculate the count of followers for each unique $\text{user}_{id}$. The result set will have one row for each unique $\text{user}_{id}$.

4. $ORDER BY \text{user}_{id} ASC$: This part orders the result set based on the $\text{user}_{id}$ column in ascending order. `ASC` stands for ascending. Please note, the default ordering done by the `ORDER BY` clause is ascending. So removing `ASC` from the query will also work.

#### Implementation

##### SQL

```sql
SELECT user_id, COUNT(user_id) AS followers_count
FROM followers
GROUP BY user_id
ORDER BY user_id ASC;
```