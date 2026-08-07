### 1. Description

Table: `Submissions`

```
+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| sub_id        | int      |
| parent_id     | int      |
+---------------+----------+
This table may have duplicate rows.
Each row can be a post or comment on the post.
parent_id is null for posts.
parent_id for comments is sub_id for another post in the table.
```

Write a solution to find the number of comments per post. The result table should contain $\text{post}_{id}$ and its corresponding `number_of_comments`.

The `Submissions` table may contain duplicate comments. You should count the number of **unique comments** per post.

The `Submissions` table may contain duplicate posts. You should treat them as one post.

The result table should be **ordered** by $\text{post}_{id}$ in **ascending order**.

The result format is in the following example.

### 2. Function Contract

**Input table**

$Submissions(\text{sub}_{id}, \text{parent}_{id})$ may contain duplicate rows. Null $\text{parent}_{id}$ values identify post rows; non-null values identify the parent post of a comment row.

Let $r$ be the total number of rows in `Submissions`.

**Return value**

- Return exactly the columns $\text{post}_{id}$ and `number_of_comments`.
- Produce one row for every distinct $\text{sub}_{id}$ appearing on a row where $\text{parent}_{id} IS NULL$.
- Count distinct comment $\text{sub}_{id}$ values separately for each matching $\text{parent}_{id}$.
- Return zero for a post with no matching comments and ignore comments whose parent post is absent.
- Order the rows by $\text{post}_{id}$ in ascending order.

### 3. Examples

#### Example 1

```
**Input:**
Submissions table:
+---------+------------+
| sub_id  | parent_id  |
+---------+------------+
| 1       | Null       |
| 2       | Null       |
| 1       | Null       |
| 12      | Null       |
| 3       | 1          |
| 5       | 2          |
| 3       | 1          |
| 4       | 1          |
| 9       | 1          |
| 10      | 2          |
| 6       | 7          |
+---------+------------+
**Output:**
+---------+--------------------+
| post_id | number_of_comments |
+---------+--------------------+
| 1       | 3                  |
| 2       | 2                  |
| 12      | 0                  |
+---------+--------------------+
**Explanation:**
The post with id 1 has three comments in the table with id 3, 4, and 9. The comment with id 3 is repeated in the table, we counted it **only once**.
The post with id 2 has two comments in the table with id 5 and 10.
The post with id 12 has no comments in the table.
The comment with id 6 is a comment on a deleted post with id 7 so we ignored it.
```