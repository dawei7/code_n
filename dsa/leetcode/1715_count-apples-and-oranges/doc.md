# Count Apples and Oranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1715 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/count-apples-and-oranges/) |

## Problem Description
### Goal

The `Boxes` table records the apples and oranges stored directly in every box. A box may also contain a chest, identified by `chest_id`; the `Chests` table records the fruit inside each chest type. A `NULL` chest identifier means that box contains no chest.

Find the total numbers of apples and oranges across all boxes, including the contents of a referenced chest each time that chest appears in a box. Chests not referenced by any box contribute nothing.

### Function Contract
**Inputs**

- `Boxes(box_id, chest_id, apple_count, orange_count)`: one row per box, with nullable `chest_id`
- `Chests(chest_id, apple_count, orange_count)`: fruit counts for each chest identifier

Let $B$ be the number of box rows, $C$ the number of chest rows, and $R=B+C$.

**Return value**

One row with columns `apple_count` and `orange_count`, containing the direct box totals plus the fruit from every chest joined to a box.

### Examples
**Example 1**

- Input: seven boxes, six of which reference chests `14`, `3`, `2`, `6`, `6`, and `14`
- Output: `(151, 123)`

The boxes directly contain 74 apples and 79 oranges. Their referenced chest occurrences contribute another 77 apples and 44 oranges.

**Example 2**

- Input: one box with 4 apples, 6 oranges, and no chest
- Output: `(4, 6)`

A missing chest contributes zero of each fruit.

**Example 3**

- Input: two boxes both referencing a chest containing 3 apples and 5 oranges
- Output: both boxes' direct fruit plus two occurrences of that chest's contents

The same chest identifier is joined once for each box row that references it.
