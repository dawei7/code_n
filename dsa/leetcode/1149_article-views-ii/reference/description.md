## Description

Table: `Views`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
This table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date.
Note that equal author_id and viewer_id indicate the same person.
```

Write a solution to find all the people who viewed more than one article on the same date.

Return the result table sorted by `id` in ascending order.

The result format is in the following example.
### Function Contract

**Input table**

- $Views(\text{article}_{id}, \text{author}_{id}, \text{viewer}_{id}, \text{view}_{date})$: article-view events. Duplicate rows are permitted, and an author may also be the viewer.

Let $R$ be the number of rows in `Views`.

A person qualifies if there is at least one $\text{view}_{date}$ on which that $\text{viewer}_{id}$ is associated with two or more distinct $\text{article}_{id}$ values. Author identity does not affect qualification.

**Return value**

- A one-column table named `id` containing each qualifying $\text{viewer}_{id}$ exactly once, in ascending order. If no person qualifies, return the same column with no rows.

### Examples

#### Example 1

```
**Input:**
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 3          | 4         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
**Output:**
+------+
| id   |
+------+
| 5    |
| 6    |
+------+
```