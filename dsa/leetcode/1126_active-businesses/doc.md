# Active Businesses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1126 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [active-businesses](https://leetcode.com/problems/active-businesses/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/active-businesses/).

### Goal
A business is active if it has more than one event type whose occurrence count is above the average occurrence count for that same event type across all businesses. Return the active business ids.

### Query Contract
**Input table**

- `Events(business_id, event_type, occurrences)`: Occurrence counts for each business and event type.

**Output columns**

- `business_id`

### Examples
**Example 1**

`Events`

| business_id | event_type | occurrences |
|---:|---|---:|
| 1 | reviews | 10 |
| 1 | ads | 20 |
| 2 | reviews | 5 |
| 2 | ads | 5 |
| 3 | reviews | 1 |
| 3 | ads | 15 |

Output:

| business_id |
|---:|
| 1 |

---

## Solution
### Approach
Compute the average `occurrences` for each `event_type`, then join those averages back to the original rows. For each business, count how many event types have `occurrences` greater than that event type's average.

Keep businesses whose above-average count is greater than `1`.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query groups by event type and then groups by business.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
