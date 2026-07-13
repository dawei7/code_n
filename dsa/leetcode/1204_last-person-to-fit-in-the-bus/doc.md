# Last Person to Fit in the Bus

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1204 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [last-person-to-fit-in-the-bus](https://leetcode.com/problems/last-person-to-fit-in-the-bus/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/last-person-to-fit-in-the-bus/).

### Goal
People enter a bus in `turn` order and the bus can carry at most `1000` total weight. Return the name of the last person who can board without exceeding the limit.

### Query Contract
**Input table**

- `Queue(person_id, person_name, weight, turn)`: Boarding order and passenger weights.

**Output column**

- `person_name`

### Examples
**Example 1**

`Queue`

| person_id | person_name | weight | turn |
|---:|---|---:|---:|
| 5 | Alice | 250 | 1 |
| 3 | Alex | 350 | 2 |
| 6 | John Cena | 400 | 3 |
| 2 | Marie | 200 | 4 |
| 4 | Bob | 175 | 5 |
| 1 | Winston | 500 | 6 |

Output:

| person_name |
|---|
| John Cena |

---

## Solution
### Approach
Order passengers by `turn` and compute a running weight sum. Keep rows where the running sum is at most `1000`, then choose the row with the largest `turn` among those rows.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, rows are ordered and a cumulative sum is computed.
- **Space Complexity**: Depends on the execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
