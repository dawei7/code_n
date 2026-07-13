# Actors and Directors Who Cooperated At Least Three Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1050 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [actors-and-directors-who-cooperated-at-least-three-times](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/).

### Goal
From a table of actor-director collaborations, return every actor and director pair that has worked together at least three times.

### Query Contract
**Input table**

- `ActorDirector(actor_id, director_id, timestamp)`: One row per collaboration event.

**Output columns**

- `actor_id`
- `director_id`

### Examples
**Example 1**

`ActorDirector`

| actor_id | director_id | timestamp |
|---:|---:|---:|
| 1 | 1 | 0 |
| 1 | 1 | 1 |
| 1 | 1 | 2 |
| 1 | 2 | 3 |
| 1 | 2 | 4 |
| 2 | 1 | 5 |
| 2 | 1 | 6 |

Output:

| actor_id | director_id |
|---:|---:|
| 1 | 1 |

---

## Solution
### Approach
Group rows by `(actor_id, director_id)` and keep only groups whose row count is at least `3`.

In SQL, this is a straightforward `GROUP BY actor_id, director_id` with `HAVING COUNT(*) >= 3`.

### Complexity Analysis
- **Time Complexity**: Depends on the database engine; logically, the query groups all rows in `ActorDirector`.
- **Space Complexity**: Depends on the database execution plan and indexes.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
