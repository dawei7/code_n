# Reformat Department Table

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1179 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [reformat-department-table](https://leetcode.com/problems/reformat-department-table/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/reformat-department-table/).

### Goal
Pivot monthly department revenue rows into one row per department id, with one revenue column for each month from January through December.

### Query Contract
**Input table**

- `Department(id, revenue, month)`: Revenue value for a department and month.

**Output columns**

- `id`
- `Jan_Revenue`, `Feb_Revenue`, `Mar_Revenue`, `Apr_Revenue`, `May_Revenue`, `Jun_Revenue`, `Jul_Revenue`, `Aug_Revenue`, `Sep_Revenue`, `Oct_Revenue`, `Nov_Revenue`, `Dec_Revenue`

### Examples
**Example 1**

`Department`

| id | revenue | month |
|---:|---:|---|
| 1 | 8000 | Jan |
| 2 | 9000 | Jan |
| 3 | 10000 | Feb |
| 1 | 7000 | Feb |
| 1 | 6000 | Mar |

Output:

| id | Jan_Revenue | Feb_Revenue | Mar_Revenue |
|---:|---:|---:|---:|
| 1 | 8000 | 7000 | 6000 |
| 2 | 9000 | null | null |
| 3 | null | 10000 | null |

The full result also includes the remaining month columns through `Dec_Revenue`.

---

## Solution
### Approach
Group by `id` and use conditional aggregation for each month, such as `SUM(CASE WHEN month = 'Jan' THEN revenue END)`.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, department rows are grouped once by id.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
