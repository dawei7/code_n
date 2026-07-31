# Total Traveled Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2837 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/total-traveled-distance/) |

## Problem Description
### Goal

The `Users` table identifies every user and stores their name. The `Rides` table records completed rides, including the user responsible for each ride and its traveled distance. A user may have several ride rows, while some users may have no completed ride at all.

Produce one result row for every user. Report the user's identifier, name, and the sum of all their ride distances under the column name `traveled distance`. A user with no matching ride must receive a distance of `0`, not be omitted. Sort the final rows by `user_id` in ascending order.

### Function Contract
**Inputs**

- `Users(user_id, name)`: `user_id` is unique; each row associates a user identifier with a name.
- `Rides(ride_id, user_id, distance)`: `ride_id` is unique; each row records one ride, its user, and the traveled distance.

Let $U$ be the number of rows in `Users` and $R$ the number of rows in `Rides`.

**Return value**

Return a table with columns `user_id`, `name`, and `traveled distance`. Include every user, use `0` when that user has no rides, and order rows by `user_id` ascending.

### Examples
**Example 1**

- Input: `Users = [(17, "Addison"), (14, "Ethan"), (4, "Michael"), (2, "Avery"), (10, "Eleanor")]`, with rides totaling `160`, `186`, `416`, `393`, and no rides for user `10` respectively.
- Output: `[(2, "Avery", 393), (4, "Michael", 416), (10, "Eleanor", 0), (14, "Ethan", 186), (17, "Addison", 160)]`
- Explanation: Ride distances are summed per user, Eleanor is retained with zero, and the rows are sorted by identifier.
