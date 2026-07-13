# Article Views II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1149 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [article-views-ii](https://leetcode.com/problems/article-views-ii/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/article-views-ii/).

### Goal
Return viewers who viewed more than one distinct article on the same date.

### Query Contract
**Input table**

- `Views(article_id, author_id, viewer_id, view_date)`: Article view records.

**Output columns**

- `id`: Viewer id.

### Examples
**Example 1**

`Views`

| article_id | author_id | viewer_id | view_date |
|---:|---:|---:|---|
| 1 | 3 | 5 | 2019-08-01 |
| 3 | 4 | 5 | 2019-08-01 |
| 2 | 7 | 6 | 2019-08-01 |
| 2 | 7 | 6 | 2019-08-02 |

Output:

| id |
|---:|
| 5 |

---

## Solution
### Approach
Group by `viewer_id` and `view_date`, count distinct `article_id` values, and keep groups whose count is greater than `1`. Select distinct viewer ids from those groups and sort them ascending.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query groups view rows by viewer and date.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
