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

### Required Complexity

- **Time:** $O(U + R + U\log U)$
- **Space:** $O(U)$

<details>
<summary>Approach</summary>

#### General

Left join every user to rides on the user identifier. Group by the user's identifier and name, sum ride distances, and replace the null aggregate for an unmatched user with zero.

The left join contributes every matching ride to exactly its user while preserving one null-extended row for a user without rides. Summation therefore gives each true total, and `COALESCE` gives exactly zero only for the no-ride case. Grouping by the identifier keeps different users separate even if names happen to match.

Finally order by the computed total descending and `name` ascending to apply both required ranking keys.

#### Complexity detail

With indexed or hash joining, reading $U$ users and $R$ rides and aggregating by user takes $O(U + R)$ time and $O(U)$ grouping space. Sorting the $U$ output rows adds $O(U\log U)$ time.

#### Alternatives and edge cases

- **Correlated sum per user:** A scalar subquery is concise but can rescan all $R$ rides for each user, costing $O(UR)$ without an effective index.
- **Inner join:** It incorrectly removes users who have no rides.
- **Null aggregate:** Convert it to integer zero with `COALESCE`.
- **Several rides:** Sum every distance for the user rather than selecting one row.
- **Equal totals:** Apply name ascending as the secondary ordering key.
- **Equal names:** Group by user ID as well as name so separate user records are not merged.

</details>
