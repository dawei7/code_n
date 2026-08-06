## Description

Table: `customer_transactions`

```

+------------------+---------+
| Column Name      | Type    | 
+------------------+---------+
| transaction_id   | int     |
| customer_id      | int     |
| transaction_date | date    |
| amount           | decimal |
| transaction_type | varchar |
+------------------+---------+
transaction_id is the unique identifier for this table.
transaction_type can be either 'purchase' or 'refund'.

```

Write a solution to find **loyal customers**. A customer is considered **loyal** if they meet ALL the following criteria:

<ul>
	<li>Made **at least** `<font face="monospace">3</font>` purchase transactions.</li>
	<li>Have been active for **at least** `30` days.</li>
	<li>Their **refund rate** is less than `20%` .</li>
</ul>

*Refund rate* is the proportion of transactions that are refunds, calculated as the number of refund transactions divided by the total number of transactions (purchases plus refunds).

Return *the result table ordered by* `customer_id` *in **ascending** order*.

The result format is in the following example.
