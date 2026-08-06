## Description

Table: `Accounts`

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.

```

 

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

<ul>
	<li>`"Low Salary"`: All the salaries **strictly less** than `$20000`.</li>
	<li>`"Average Salary"`: All the salaries in the **inclusive** range `[$20000, $50000]`.</li>
	<li>`"High Salary"`: All the salaries **strictly greater** than `$50000`.</li>
</ul>

The result table **must** contain all three categories. If there are no accounts in a category, return `0`.

Return the result table in **any order**.

The result format is in the following example.
