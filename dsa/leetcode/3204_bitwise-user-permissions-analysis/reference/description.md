## Description

Table: $\text{user}_{permissions}$

```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| user_id     | int     |
| permissions | int     |
+-------------+---------+
user_id is the primary key.
Each row of this table contains the user ID and their permissions encoded as an integer.
```

Consider that each bit in the `permissions` integer represents a different access level or feature that a user has.

Write a solution to calculate the following:

- common_perms: The access level granted to **all users**. This is computed using a **bitwise AND** operation on the `permissions` column.

- any_perms: The access level granted to **any user**. This is computed using a **bitwise OR** operation on the `permissions` column.

Return *the result table in **any** order*.

The result format is shown in the following example.

**Example:**

<div class="example-block">
**Input:**

user_permissions table:

```
+---------+-------------+
| user_id | permissions |
+---------+-------------+
| 1       | 5           |
| 2       | 12          |
| 3       | 7           |
| 4       | 3           |
+---------+-------------+
```

**Output:**

```
+-------------+--------------+
| common_perms | any_perms   |
+--------------+-------------+
| 0            | 15          |
+--------------+-------------+
```

**Explanation:**

- **common_perms:** Represents the bitwise AND result of all permissions:

		<li>For user 1 (5): 5 (binary 0101)

- For user 2 (12): 12 (binary 1100)

- For user 3 (7): 7 (binary 0111)

- For user 4 (3): 3 (binary 0011)

- Bitwise AND: 5 & 12 & 7 & 3 = 0 (binary 0000)

	</li>
- **any_perms:** Represents the bitwise OR result of all permissions:

		<li>Bitwise OR: 5 | 12 | 7 | 3 = 15 (binary 1111)

	</li>

</div>

### Function Contract

- Refer to method signature.