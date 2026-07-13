# Article Views I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1148 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [article-views-i](https://leetcode.com/problems/article-views-i/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/article-views-i/).

### Goal
Return the ids of authors who viewed at least one of their own articles.

### Query Contract
**Input table**

- `Views(article_id, author_id, viewer_id, view_date)`: Article view records.

**Output columns**

- `id`: Author id.

### Examples
**Example 1**

`Views`

| article_id | author_id | viewer_id | view_date |
|---:|---:|---:|---|
| 1 | 3 | 5 | 2019-08-01 |
| 1 | 3 | 6 | 2019-08-02 |
| 2 | 7 | 7 | 2019-08-01 |
| 2 | 7 | 6 | 2019-08-02 |

Output:

| id |
|---:|
| 7 |

---

## Solution
### Approach
Filter rows where `author_id = viewer_id`, then select distinct author ids and sort them ascending.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query filters view rows and deduplicates author ids.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
