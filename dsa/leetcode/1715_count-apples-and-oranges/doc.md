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

### Required Complexity

- **Time:** $O(R)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Preserve every box with a left join**

Left-join `Boxes` to `Chests` on `chest_id`. An inner join would discard boxes without a chest, losing their direct fruit. For an unmatched or `NULL` chest identifier, replace each joined chest count with zero using `COALESCE`.

**Aggregate direct and nested fruit together**

For each joined box row, add its direct apple count to the joined chest apple count, and do the same for oranges. Sum these per-box expressions across the entire join.

Each box produces exactly one joined row because a chest identifier uniquely identifies its `Chests` record. Therefore direct fruit is counted once per box. A referenced chest contributes once through every box occurrence, while an unreferenced chest creates no joined row and contributes nothing. These are exactly the required totals.

#### Complexity detail

A hash join can build a lookup from the $C$ chest rows in $O(C)$ time and space, then scan and aggregate the $B$ boxes in $O(B)$ time. Total time is $O(B+C)=O(R)$ and auxiliary join space is $O(C)$.

#### Alternatives and edge cases

- **Inner join:** boxes without a chest disappear, incorrectly removing their direct fruit.
- **Sum the tables independently:** adding every chest row includes unreferenced chests and fails to repeat a chest referenced by several boxes.
- **Correlated chest lookup:** searching `Chests` separately for every box can take $O(BC)$ time without an index.
- **No chest:** `NULL` must contribute zero rather than making the per-row addition `NULL`.
- **Repeated chest identifier:** include its fruit once for each referencing box row.
- **Unreferenced chest:** it contributes nothing because no box contains it.
- **Zero fruit counts:** zero remains a valid contribution and must not be confused with a missing row.
- **Output shape:** return one aggregate row with the two required column names.

</details>
