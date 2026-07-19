# Actors and Directors Who Cooperated At Least Three Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1050 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/) |

## Problem Description

### Goal

The `ActorDirector` table records collaborations using `actor_id`, `director_id`, and a unique `timestamp`. Each row represents one occasion on which that actor and director worked together.

Find every distinct `(actor_id, director_id)` pair having at least three collaboration rows. The timestamp values distinguish events but do not need to be consecutive. Return the two identifier columns; the platform permits the qualifying pairs in any order.

### Function Contract

**Inputs**

- `ActorDirector(actor_id, director_id, timestamp)`: $R$ collaboration rows whose `timestamp` values are unique.

**Return value**

- One `actor_id, director_id` row for each pair appearing at least three times.
- Result order is unrestricted; the local reference orders both identifiers ascending for deterministic validation.

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

Only actor `1` and director `1` have collaborated three times.
