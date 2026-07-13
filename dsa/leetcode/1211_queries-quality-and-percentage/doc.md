# Queries Quality and Percentage

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1211 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [queries-quality-and-percentage](https://leetcode.com/problems/queries-quality-and-percentage/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/queries-quality-and-percentage/).

### Goal
For each query name, calculate its average quality and the percentage of poor results. Quality for a row is `rating / position`; a poor result has `rating < 3`. Round both metrics to two decimal places.

### Query Contract
**Input table**

- `Queries(query_name, result, position, rating)`: Search query result rows.

**Output columns**

- `query_name`
- `quality`
- `poor_query_percentage`

### Examples
**Example 1**

`Queries`

| query_name | result | position | rating |
|---|---|---:|---:|
| Dog | Golden Retriever | 1 | 5 |
| Dog | German Shepherd | 2 | 5 |
| Dog | Mule | 200 | 1 |
| Cat | Shirazi | 5 | 2 |
| Cat | Siamese | 3 | 3 |
| Cat | Sphynx | 7 | 4 |

Output:

| query_name | quality | poor_query_percentage |
|---|---:|---:|
| Dog | 2.50 | 33.33 |
| Cat | 0.66 | 33.33 |

---

## Solution
### Approach
Group by `query_name`. Use `AVG(rating / position)` for quality and a conditional average or count ratio for rows where `rating < 3`, multiplied by `100`.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, rows are grouped by query name.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
