# Top Travellers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1407 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open Problem](https://leetcode.com/problems/top-travellers/) |

## Problem Description

### Goal

The `Users` table identifies travelers and gives their names. Each row of `Rides` associates a traveled distance with one user. A user may have several rides or none.

For every user, report their name and the total distance across all of their rides. Users without rides must still appear with total distance zero. Sort results by traveled distance in descending order; when totals tie, sort names in ascending lexicographic order.

### Function Contract

**Inputs**

- `Users(id, name)`: $U$ user rows.
- `Rides(id, user_id, distance)`: $R$ ride rows.

**Return value**

- A relation with columns `name` and `travelled_distance`, containing all $U$ users in the required distance-descending, name-ascending order.

### Examples

**Example 1**

- Input: Ann has rides of distances `10` and `15`; Bob has one ride of `20`.
- Output: Ann with `25`, followed by Bob with `20`.

**Example 2**

- Input: Cara has no rides.
- Output: Cara with `travelled_distance = 0`.

**Example 3**

- Input: Amy and Zoe both travel `12`.
- Output: Amy precedes Zoe because their totals tie.
