# Fix Names in a Table

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1667 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/fix-names-in-a-table/) |

## Problem Description
### Goal
The `Users` table stores a unique integer identifier and a name for every user. Each name is nonempty and contains only uppercase and lowercase English letters, but its existing capitalization may be arbitrary: the first letter can be lowercase and any later letter can be uppercase.

Normalize every name so that its first character is uppercase and all remaining characters are lowercase. Return every user's `user_id` together with the corrected value under the column name `name`, ordering the result by `user_id` in ascending order.

### Function Contract
**Input table**

`Users`

| Column | Type | Meaning |
|---|---|---|
| `user_id` | integer | Unique identifier and primary key. |
| `name` | varchar | Nonempty alphabetic name whose capitalization may be inconsistent. |

Let $R$ be the number of rows in `Users`.

**Return value**

Return columns `user_id` and `name` for all users. In each returned name, uppercase exactly the first character and lowercase the suffix. Sort rows by `user_id` ascending.

### Examples
**Example 1**

- Input: `Users = [[1, "aLice"], [2, "bOB"]]`
- Output: `[[1, "Alice"], [2, "Bob"]]`
